#!/usr/bin/python
"""The package that helps to upload videos on YouTube using Selenium"""
from distutils.core import setup

setup_kwargs = {
    "name": "youtube_uploader_selenium",
    "version": "0.1.1",
    "description": "Upload videos to Youtube with Selenium",
    "author": "Kostya Linou",
    "author_email": "linouk23@gmail.com",
    "url": "https://github.com/linouk23/youtube_uploader_selenium",
    "packages": ["youtube_uploader_selenium"],
    "data_files": [],
    "scripts": ["upload.py"],
    "license": "MIT",
    "long_description": " ".join(__doc__.strip().splitlines()),
    "python_requires": ">=3",
    "classifiers": [
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    "entry_points": {
        'console_scripts': [
            'youtube-upload-selenium = upload:cli_main'
        ],
    },
    "install_requires":[]
}

setup(**setup_kwargs)
