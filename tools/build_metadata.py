# coding: utf-8
import os
from os.path import join, getctime, getmtime, splitext, basename
from concurrent.futures import ThreadPoolExecutor
import glob
import time
import json
import subprocess
from string import Template
from urllib.parse import quote
from collections import OrderedDict


import begin


sitemap_template = Template('''<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>http://pythonomicon.com/</loc>
      <changefreq>weekly</changefreq>
   </url>
$items
</urlset>
''')

sitemap_entry_template = Template('''    <url>
        <loc>http://pythonomicon.com/?post=$postname</loc>
        <changefreq>weekly</changefreq>
    </url>''')


@begin.start
def process(notebook_folder, output_folder):
    """ This command will process all IPython Notebook files found
    in Notebook Folder and will place the output html files into
    the output folder. Metadata json files will also be created and
    will contain items like the creation date of each notebook file."""
    metadata = {}
    cmds = []
    # Walk over all the IPython Notebook files
    for nbfile in glob.glob(join(notebook_folder, '*.ipynb')):
        timestamp = getctime(nbfile)  # Get the notebook creation time
        timestamp_modified = getmtime(nbfile)
        creation_date = time.ctime(timestamp)  # as a string
        modified_date = time.ctime(timestamp_modified)
        nbbasefile = basename(nbfile)
        print('Processing "{}"...'.format(nbbasefile))
        postname, ext = splitext(nbbasefile)
        metadata[postname] = OrderedDict([
            ('timestamp',timestamp),
            ('creation_date',creation_date),
            ('timestamp_modified',timestamp_modified),
            ('modified_date',modified_date),
        ])

        # Check if there has already been metadata written into the output
        # folder for this post
        md_filename = join(output_folder, postname+'.json')
        if os.path.exists(md_filename):
            # Load the previously-written metadata
            with open(md_filename, 'r') as f:
                md = json.load(f)
            # We want to never change a creation date, so intercept what has
            # previously been stored for creation date, and use that to
            # overwrite what we have just read.  There are some circumstances
            # in which the creation time of the file might have been changed.
            if 'timestamp' in md:
                metadata[postname].update(
                    (k, md[k]) for k in ('timestamp', 'creation_date'))

        # Convert the notebook file to plain HTML, add to posts/ folder
        tmpl = '. activate github_blog && jupyter nbconvert --to html --template basic "{}" --stdout > "{}"'
        cmd = tmpl.format(
            nbfile,
            join(output_folder, postname+'.html'),
        )
        cmds.append(cmd)

    def run_conversion(cmd):
        return subprocess.check_call(cmd, shell=True)
    with ThreadPoolExecutor(max_workers=len(cmds)) as executor:
        futures = [executor.submit(run_conversion, cmd) for cmd in cmds]
        result = [f.result() for f in futures]
        print(result)

    # Move through the list, building up the cross links
    # Posts are sorted by creation timestamp
    sorted_posts = list(sorted(metadata, key=lambda x: metadata[x]['timestamp']))
    data_sitemap = []
    for i, postname in enumerate(sorted_posts):
        # For the first post, set its "previous post" link to None.
        if i == 0:
            previous_post = None
        else:
            previous_post = sorted_posts[i - 1]

        # For the last post, set its "next post" link to None
        if i == len(sorted_posts) - 1:
            next_post = None
            last_post = postname
        else:
            next_post = sorted_posts[i + 1]

        # Link up the post with 'previous' and 'next'
        metadata[postname]['previous_post'] = previous_post
        metadata[postname]['next_post'] = next_post

        print(postname)

        # Write out the new metadata for this post
        with open(join(output_folder, postname+'.json'), 'w') as f:
            json.dump(metadata[postname], f, indent=4)

        data_sitemap.append(sitemap_entry_template.substitute(
            postname=quote(postname)
        ))

    # Rebuild the sitemap to include all the posts
    with open('sitemap.xml', 'w') as f:
        f.write(sitemap_template.substitute(
            items='\n'.join(data_sitemap)
        ))

    # Store the most recent post. This is used when the page is first loaded.
    # TODO: there must be a way to make it so that index.html automatically
    # contains the most recent post data. This would make the initial page
    # load much faster.
    with open(join(output_folder, 'latest.json'), 'w') as f:
        json.dump(dict(post=last_post), f, indent=4)



