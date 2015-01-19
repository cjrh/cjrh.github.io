# coding: utf-8
import os
from os.path import join, getctime, splitext, basename
import sys
import begin
import glob
import time
import json


@begin.start
def process(notebook_folder, output_folder):
    """ This command will process all IPython Notebook files found
    in Notebook Folder and will place the output html files into
    the output folder. Metadata json files will also be created and
    will contain items like the creation date of each notebook file."""
    metadata = {}
    for nbfile in glob.glob(join(notebook_folder, '*.ipynb')):
        timestamp = getctime(nbfile)
        creation_date = time.ctime(getctime(nbfile))
        nbbasefile = basename(nbfile)
        print 'Processing "{}"...'.format(nbbasefile)
        postname, ext = splitext(nbbasefile)
        metadata[postname] = dict(
                timestamp=timestamp,
                creation_date=creation_date
                )
        tmpl = 'ipython nbconvert --to html --template basic "{}" --stdout > "{}"'
        os.system(tmpl.format(nbfile, join(output_folder, postname+'.html')))
        print creation_date

    # Move through the list, building up the cross links
    sorted_posts = list(sorted(metadata, key=lambda x: metadata[x]['timestamp']))
    for i, postname in enumerate(sorted_posts):
        if i == 0:
            previous_post = None
        else:
            previous_post = sorted_posts[i - 1]

        if i == len(sorted_posts) - 1:
            next_post = None
        else:
            next_post = sorted_posts[i + 1]

        metadata[postname]['previous_post'] = previous_post
        metadata[postname]['next_post'] = next_post

        print postname
        with open(join(output_folder, postname+'.json'), 'w') as f:
            json.dump(metadata[postname], f, indent=4)



