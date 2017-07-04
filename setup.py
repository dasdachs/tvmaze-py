import os
import re

from distutils.core import setup


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.

    A simple trick borrowe from Tom Christie's APISTAR
    """
    init_py = open(os.path.join('mongoschema', '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


setup(
    name='TvmazePy',
    version=get_version(),
    author='Jani Šumak',
    author_email='jani.sumak@gmail.com',
    url='https://github.com/dasdachs/mongoschema',
    packages=['tvmaze',],
    license='MIT',
    description='Tvmaze wrapper in Python',
    long_description=open('README.rst').read(),
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          # 'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python',
          'Topic :: API',
    ],
    keywords=[
    ],

    # Requirements 
    install_requires=[
        "requests", # Specify version
    ],

    # CLI tool
    entry_points={
        'console_scripts':""
    },
)
