#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Adil Zouitine <adilzouitinegm@gmail.com

"""

from setuptools import setup, find_packages
import pyFeel

setup(name='pyFeel',
      version=pyFeel.__version__,
      description='French sentiment analysis',
      url='https://github.com/AdilZouitine/pyFeel',
      author='Adil Zouitine',
      author_email='adilzouitine@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=['numpy>=1.19.1'],
      include_package_data=True,
      zip_safe=False)
