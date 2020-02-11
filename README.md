# sphinx-yaml-metadata

[![PyPI](https://img.shields.io/pypi/v/sphinx-yaml-metadata.svg)](https://pypi.org/project/sphinx_yaml_metadata/) | [![Documentation](https://readthedocs.org/projects/sphinx-yaml-metadata/badge/?version=latest)](https://sphinx-yaml-metadata.readthedocs.io/en/latest/?badge=latest)

A small sphinx extension to add a "copy" button to code blocks.

See [the sphinx-yaml-metadata documentation](https://sphinx-yaml-metadata.readthedocs.io/en/latest/) for more details!

![](doc/_static/copybutton.gif)

## Installation

You can install `sphinx-yaml-metadata` with `pip`:

```
pip install sphinx-yaml-metadata
```

## Usage

In your `conf.py` configuration file, add `sphinx_yaml_metadata` to your extensions list.
E.g.:

```
extensions = [
    ...
    'sphinx_yaml_metadata'
    ...
]
```

When you build your site, your code blocks should now have little copy buttons to their
right. Clicking the button will copy the code inside!

## Customization

If you'd like to customize the look of the copy buttons, you can over-write any of the
CSS rules specified in the sphinx-yaml-metadata CSS file ([link](sphinx_yaml_metadata/_static/copybutton.css))
