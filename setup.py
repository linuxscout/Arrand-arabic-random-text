#!/usr/bin/python
# -*- coding=utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()

setup (name='arrand', version='0.1',
      description="Arrand: random Arabic text generator",
      long_description = readme(),      

      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://arrand.sourceforge.net/',
      license='GPL',
      package_dir={'arrand': 'arrand'},
      packages=['arrand'],
      install_requires=[ "pyarabic>=0.6.8",
            ],         
      include_package_data=True,
      package_data = {
        'arrand': ['doc/*.*','doc/html/*', 'data/*.sqlite', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

