@default:
    just -l

# Launch Jupyter Notebook
start:
    jupyter notebook notebooks/

# Regenerate all blog posts from Jupyter notebooks
regenerate:
    bash run.sh
