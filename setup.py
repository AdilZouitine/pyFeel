from setuptools import setup, find_packages
import pyFeel

setup(name='pyFeel',
      version=pyFeel.__version__,
      description='French sentimental analysis',
      url='https://github.com/AdilZouitine/pyFeel',
      author='Adil Zouitine',
      author_email='adilzouitine@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False)
