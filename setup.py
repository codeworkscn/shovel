#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import os.path
import sys
import shutil

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'shovel'
DESCRIPTION = "Tools suite for DevOps, build by Python"
URL = ''
EMAIL = 'codeworkscn@gmail.com'
AUTHOR = 'codeworkscn'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = [
    'jsonpickle',
    'pyyaml',
    'p4python',
    'gitpython',
    'elasticsearch>=6.0.0,<7.0.0'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

try:
    config_file_template_path = os.path.join(
        here, 'shovel_config_template.yaml')
    #config_file_path = os.path.join(here, 'shovel_config.yaml')
    print('config_file_path=%s' % config_file_path)
    if not os.path.exists(config_file_path):
        shutil.copyfile(config_file_template_path, config_file_path)
        print('copy config file from template, config_file_path=%s' %
              config_file_path)
except Exception as e:
    print("Exception: " + str(e))

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    data_files=[
        ('config', ['shovel_config_template.yaml',
                    'shovel_config.yaml',
                    'shovel_logging_config.ini'])],
    scripts=['scripts/p4integratebyjob.py',
             'scripts/elasticsearchcompare.py']
)
