@default:
    just -l

# Install/sync the Python environment from pyproject.toml + uv.lock
sync:
    uv sync

# Launch Jupyter Notebook
start:
    uv run jupyter lab notebooks/

# Regenerate all blog posts from Jupyter notebooks
regenerate:
    bash run.sh

# Install evcxr Jupyter kernel for Rust cells
install_evcxr:
    # https://github.com/evcxr/evcxr/blob/main/evcxr_jupyter/README.md
    cargo install --locked evcxr_jupyter
    evcxr_jupyter --install
    # :dep evcxr_input
    # let name = evcxr_input::get_string("Name?");
    # let password = evcxr_input::get_password("Password?");

# Serve the current directory
serve:
    miniserve --index index.html
