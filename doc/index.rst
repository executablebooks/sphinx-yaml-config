=================
sphinx-yaml-metadata
=================

.. image:: https://readthedocs.org/projects/sphinx-yaml-metadata/badge/?version=latest
   :target: https://sphinx-yaml-metadata.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation

.. image:: https://img.shields.io/pypi/v/sphinx-yaml-metadata.svg
   :target: https://pypi.org/project/sphinx_yaml_metadata
   :alt: PyPi page

sphinx-yaml-metadata allows you to add configuration key/values to your Sphinx
site with YAML. It basically mimics declaring ``key=value`` pairs in your
``conf.py`` file.

To use it, create a YAML file with the configuration options you'd like.
In your ``conf.py`` file, add a configuration option like so:

.. code-block:: python

    yaml_config_path = "<path-relative-to-conf.py>"

When you build your site, all of your configuration values will be updated
with the key/value pairs in your yaml file.

Installation
============

You can install ``sphinx-yaml-metadata`` with ``pip``:

.. code-block:: bash

   pip install sphinx-yaml-metadata

`Here's a link to the sphinx-yaml-metadata GitHub repository <https://github.com/choldgraf/sphinx-yaml-metadata>`_.
