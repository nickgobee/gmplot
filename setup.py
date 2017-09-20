import os
from setuptools import setup, find_packages

__version__ = '1.1.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'gmplot_spike',
    version = __version__,
    author = 'Nick Settje (originally Michael Woods)',
    author_email = 'nick.settje@gobee.bike',
    url = 'https://github.com/nickgobee/gmplot',
    description = 'Improve a matplotlib like interface to plotting data with Google Maps',
    long_description=read('README.rst'),
    license='MIT',
    keywords='python wrapper google maps',
    packages = find_packages(),
    include_package_data=True,
    package_data = {
        'gmplot_spike': ['markers/*.png'],
    },
    install_requires=['requests'],
)
