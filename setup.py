from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Metatrader5 mock for Mac developers'
PACKAGE_NAME = 'MMetaTrader5'
AUTHOR = 'Javier Gonzalez Moya'
EMAIL = 'javigonzmoya@gmail.com'
GITHUB_URL = ''

setup(
    name = 'MMetaTrader5',
    packages = [PACKAGE_NAME],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = 'Javier Gonzalez Moya',
    author_email = 'javigonzmoya@gmail.com',
    url = GITHUB_URL,
    keywords = [],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)