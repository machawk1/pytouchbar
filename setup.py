#!/usr/bin/env python

from setuptools import setup
from touchbar import __version__

#long_description = open('README.rst').read()
desc = """Touchbar"""

setup(
    name='touchbar',
    version=__version__,
    url='https://github.com/machawk1/pytouchbar',
    download_url="https://github.com/machawk1/pytouchbar",
    author='Mat Kelly',
    author_email='mkelly@cs.odu.edu',
    description=desc,
    packages=['touchbar'],
    license='MIT',
    #long_description=long_description,
    provides=[
        'touchbar'
    ],
    setup_requires=[
        "pyobjc-framework-Cocoa"
    ],
    entry_points = """
        [console_scripts]
        touchbar = touchbar.__main__:main
    """,
)

# Publish to pypi:
#   rm -rf dist; python setup.py sdist bdist_wheel; twine upload dist/*
