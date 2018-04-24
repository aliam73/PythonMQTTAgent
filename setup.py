#!/usr/bin/env python

try:
    with open('package_description.rst', 'r') as file_description:
		description = file_description.read()
except IOError:
    description = "https://github.com/aliam73/PythonMQTTAgent"

from setuptools import setup, find_packages

import CloudingThings4Pi

setup(
    name = "CloudingThingsPythonAgent",
    version = "0.1.0",

    description = "Python module used to create Mqtt agents for Clouding"\
                  "Things use case prototyping platform",
    long_description = description,

    author = "Clouding Things",
    author_email = "founders@clouding-things.com",

    license = 'MIT',
    classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url = "https://github.com/https://github.com/aliam73/PythonMQTTAgent",

    keywords = ['iot', 'internet of things', 'prototyping',
                'clouding things'],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires = ['paho-mqtt']
)
