import os

from setuptools import setup, find_packages
from sphinx_yaml_metadata import __version__

with open('./README.md', 'r') as ff:
    readme_text = ff.read()

setup(
    name='sphinx-yaml-metadata',
    version=__version__,
    description="Add a copy button to each of your code cells.",
    long_description=readme_text,
    long_description_content_type='text/markdown',
    author='Chris Holdgraf',
    author_email='choldgraf@berkeley.edu',
    url="https://github.com/choldgraf/sphinx-yaml-metadata",
    license='MIT License',
    packages=find_packages(),
    package_data={'sphinx_yaml_metadata': ['_static/copybutton.css',
                                        '_static/copybutton.js_t',
                                        '_static/copy-button.svg',
                                        '_static/clipboard.min.js']},
    classifiers=["License :: OSI Approved :: MIT License"],
    install_requires=[
        "sphinx>=1.8",
        "ruamel.yaml"
    ]
)
