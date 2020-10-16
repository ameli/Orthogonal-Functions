#!/usr/bin/env python

# =======
# Imports
# =======

from __future__ import print_function
import os
import sys
import setuptools
import codecs

# =========
# Read File
# =========

def ReadFile(Filename):
    with codecs.open(Filename, 'r', 'latin') as File:
        return File.read()

# ================
# Read File to RST
# ================

def ReadFileToRST(Filename):
    try:
        import pypandoc
        rstname = "{}.{}".format(os.path.splitext(Filename)[0], 'rst')
        pypandoc.convert(read(Filename), 'rst', format='md', outputfile=rstname)
        with open(rstname, 'r') as f:
            rststr = f.read()
        return rststr
        #return read(rstname)
    except ImportError:
        return read(Filename)

# ====
# Main
# ====

def main(argv):

    # Read version
    version_dummy = {}
    exec(read('OrthogonalFunctions/__version__.py'),version_dummy)
    __version__ = version_dummy['__version__']
    del version_dummy

    # Long description
    LongDescription =
    """
Please refer to the github homepage for detailed instructions on installation and usage.
    """

    # Setup
    setuptools.setup(
        name = 'OrthogonalFunctions',
        version = __version__,
        author = ReadFileToRSF('AUTHORS.txt'),
        author_email = 'sameli@berkeley.edu',
        description = 'Generate orthogonal set of functions',
        long_description = LongDescription,
        long_description_content_type = 'text/markdown',
        keywords = 'orthogonal-functions regression sympy computer-algebra gram-schmidt',
        url = 'https://github.com/ameli/Orthogonal-Functions',
        download_url = 'https://github.com/ameli/Orthogonal-Functions',
        packages=setuptools.find_packages(),
        classifiers = [
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Natural Language :: English',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        python_requires='>=3.6',
    )

# ===========
# System Main
# ===========

if __name__ == "__main__":
    main(sys.argv)