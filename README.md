# cjrh.github.io

I am building a static site around the IPython Notebook.  Each posts is a notebook `.ipynb` file and 
some tooling (included) converts the notebooks into basic HTML fragments, and creates metadata that
is used to configure navigation between posts in the HTML view of the site. 

HTML and javascript have been set up to load the posts, and navigate between them. The styling has
all been done using [Sass/Compass](http://compass-style.org/) and I intend to structure the styling
such that a simple theme format will be possible.

## Development

The Python environment is managed with [uv](https://docs.astral.sh/uv/); dependencies live in
`pyproject.toml` and are pinned in `uv.lock`. Task shortcuts are defined in the `justfile` (run
`just` with no arguments to list them).

```sh
just sync         # create/update the .venv from pyproject.toml + uv.lock
just start        # launch JupyterLab in notebooks/ to write or edit posts
just regenerate   # rebuild posts/, sitemap.xml and rss.xml from the notebooks
just serve        # serve the site locally (requires miniserve)
```

Each post is a notebook under `notebooks/`. After editing, run `just regenerate` to convert the
notebooks to HTML fragments and refresh the navigation metadata, then commit and push (the site is
served from this repo via GitHub Pages). `regenerate` skips notebooks whose content is unchanged;
pass `--force-recreate` to `tools/build_metadata.py` to rebuild everything.

Rust code cells use the [evcxr](https://github.com/evcxr/evcxr) Jupyter kernel — run
`just install_evcxr` once to install it.
