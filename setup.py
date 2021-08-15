from setuptools import setup, find_packages
import os

readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
with open(readme_path) as readme:
    long_description = readme.read()

setup(name='bitnesslib',
      description='Given a binary, determine its bitness',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/ramikg/bitnesslib',
      version='0.1.0',
      packages=find_packages(),
      classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
      ])
