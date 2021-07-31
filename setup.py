from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent / 'README.md'

setup(name='bitnesslib',
      description='Given a binary, determine its bitness',
      long_description=readme_path.read_text(encoding='utf-8'),
      long_description_content_type="text/markdown",
      url='https://github.com/ramikg/bitnesslib',
      version='0.1',
      packages=find_packages(),
      python_requires='>=3',
      classifiers=[
        "Programming Language :: Python :: 3 :: Only"
      ])
