# sphinx-yaml-config

[![PyPI](https://img.shields.io/pypi/v/sphinx-yaml-config.svg)](https://pypi.org/project/sphinx_yaml_config/) | [![Documentation](https://readthedocs.org/projects/sphinx-yaml-config/badge/?version=latest)](https://sphinx-yaml-config.readthedocs.io/en/latest/?badge=latest)

A small sphinx extension to add a "copy" button to code blocks.

See [the sphinx-yaml-config documentation](https://sphinx-yaml-config.readthedocs.io/en/latest/) for more details!

![](doc/_static/copybutton.gif)

## Installation

You can install `sphinx-yaml-config` with `pip`:

```
pip install sphinx-yaml-config
```

## Usage

In your `conf.py` configuration file, add `sphinx_yaml_config` to your extensions list.
E.g.:

```
extensions = [
    ...
    'sphinx_yaml_config'
    ...
]
```

When you build your site, your code blocks should now have little copy buttons to their
right. Clicking the button will copy the code inside!

## Customization

If you'd like to customize the look of the copy buttons, you can over-write any of the
CSS rules specified in the sphinx-yaml-config CSS file ([link](sphinx_yaml_config/_static/copybutton.css))
