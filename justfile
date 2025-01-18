@default:
    just -l

# Launch Jupyter Notebook
start:
    jupyter notebook notebooks/

# Regenerate all blog posts from Jupyter notebooks
regenerate:
    bash run.sh

install_evcxr:
    # https://github.com/evcxr/evcxr/blob/main/evcxr_jupyter/README.md
    cargo install --locked evcxr_jupyter
    evcxr_jupyter --install
    # :dep evcxr_input
    # let name = evcxr_input::get_string("Name?");
    # let password = evcxr_input::get_password("Password?");
