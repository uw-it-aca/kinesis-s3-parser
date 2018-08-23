import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/kinesis-s3-parser>`_.
"""

# The VERSION file is created by travis-ci, based on the tag name
version_path = 'restclients_core/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/kinesis-s3-parser"
setup(
    name='Kinesis-s3-parser',
    version=VERSION,
    packages=['parser'],
    author="UW-IT AXDD",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[],
    license='Apache License, Version 2.0',
    description=('A parser for Caliper events stored in s3'),
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)

