"""A small sphinx extension to let you configure a site with YAML metadata."""
from pathlib import Path

__version__ = "0.0.1dev0"

from yaml import safe_load

def add_yaml_config(app, config):
    """Load all of the key/vals in a config file into the HTML page context"""
    path_yaml = app.config['yaml_config_path']

    # If no path is given we'll just skip
    if len(path_yaml) == 0:
        return

    # Load the YAML and update our site's configuration
    path_yaml = Path(path_yaml)
    if not path_yaml.exists():
        raise ValueError(f"Could not find YAML configuration file at path {path_yaml}")
    yaml_config = safe_load(path_yaml.open())
    for key, val in yaml_config.items():
        app.config[key] = val

def setup(app):
    # configuration for this tool
    app.add_config_value("yaml_config_path", "", "html")

    # Add configuration value to the template
    app.connect('config-inited', add_yaml_config)

    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
