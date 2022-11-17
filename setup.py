from setuptools import setup
from distutils.core import setup

import sys

# if len(args) < 2:
#     print(args[0], '<version>')
#     sys.exit(1)

# version = "0.0.0"
# if "--version" in sys.argv:    
    # get the value after --version

OUR_VERSION = "0.2.0"
# OUR_VERSION = str(sys.argv[-1]) # todo:WHY DOES THIS NOT WORK??
# sys.argv.remove(str(OUR_VERSION))



setup(
    name = 'python-ibc',    
    version = f'{str(OUR_VERSION)}',
    description = 'A library to make developing python based programs on cosmos chains easier',  
    py_modules = ["pyibc"],
    package_dir = {'':'src'},
    packages = [
        'pyibc_api',
        'pyibc_price',
        'pyibc_chain',
        'pyibc_utils',
    ],
    author = 'Reece Williams',
    author_email = 'reecepbcups@gmail.com',
    # long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description = open('README.md').read() + '\n\n',
    long_description_content_type = "text/markdown",
    url='https://github.com/Reecepbcups/pyibc',
    include_package_data=True,
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: BSD License",
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Text Processing',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
    ],
    install_requires = [        
        'requests>=2.20.0',
    ],
    keywords = ['Cosmos Blockchain', 'Cosmoshub', "atom token"],
)