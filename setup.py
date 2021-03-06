#!/usr/bin/env python
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):
    """
    This class is necessary because numpy won't be installed at import time.
    """
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())


VERSION = '0.0.1'
DESCRIPTION = "PDS: Simple Probabilistic Data Structure"
LONG_DESCRIPTION = ""
CLASSIFIERS = ['Intended Audience :: Developers',
               'License :: OSI Approved :: MIT License'
               'Programming Language :: Python',
               'Operating System :: OS Independent',
               'Topic :: Utilities',
               'Topic :: Database :: Database Engines/Servers',
               'Topic :: Software Development :: Libraries :: Python Modules']

setup(
    name="pds",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=('data structures', 'bloom filter', 'bloom', 'filter',
              'probabilistic', 'set', 'hyperloglog', 'countmin sketch'),
    author="Parse.ly",
    author_email="martin@parse.ly",
    url="https://github.com/Parsely/python-pds",
    license="MIT License",
    packages=find_packages(exclude=['ez_setup']),
    platforms=['any'],
    zip_safe=False,
    install_requires=['numpy', 'cython', 'bitarray', 'smhasher'],
    setup_requires=['numpy'],
    cmdclass={'build_ext':build_ext},
    ext_modules=[Extension("maintenance", ["pds/maintenance.c"])],
)
