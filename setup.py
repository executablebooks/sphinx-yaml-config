import os

from setuptools import setup, find_packages
from sphinx_yaml_config import __version__

with open('./README.md', 'r') as ff:
    readme_text = ff.read()

setup(
    name='sphinx-yaml-config',
    version=__version__,
    description="Configure your Sphinx repository with YAML.",
    long_description=readme_text,
    long_description_content_type='text/markdown',
    author='Chris Holdgraf',
    author_email='choldgraf@berkeley.edu',
    url="https://github.com/choldgraf/sphinx-yaml-config",
    license='MIT License',
    packages=find_packages(),
    classifiers=["License :: OSI Approved :: MIT License"],
    install_requires=[
        "sphinx>=1.8",
        "pyyaml"
    ],
    extras_require={
        "sphinx": ["myst-parser"],
    },
)
