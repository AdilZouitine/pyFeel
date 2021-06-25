#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adil Zouitine <adilzouitinegm@gmail.com

"""

from setuptools import setup, find_packages
import os

with open(os.path.join('pyFeel', 'version.py')) as fobj:
    exec(fobj.read())

setup(name='pyFeel',
      version=__version__,
      description='French sentiment analysis',
      url='https://github.com/AdilZouitine/pyFeel',
      author='Adil Zouitine',
      author_email='adilzouitine@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy>=1.19.1', 'nltk>=3.6'],
      include_package_data=True,
      zip_safe=False)
