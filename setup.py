from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = "0.0.1"
DESCRIPTION = "Metatrader5 mock for Mac developers"
PACKAGE_NAME = "MMetaTrader5"
AUTHOR = "Javier Gonzalez Moya"
EMAIL = "javigonzmoya@gmail.com"
GITHUB_URL = "https://github.com/jgonzmoya/m_metatrader_5"

setup(
    name="MMetaTrader5",
    packages=[PACKAGE_NAME],
    version=VERSION,
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Javier Gonzalez Moya",
    author_email="javigonzmoya@gmail.com",
    url=GITHUB_URL,
    keywords=[],
    install_requires=[
        "numpy",
    ],
    setup_requires=[
        "setuptools>=65.5.0",  # Require a modern setuptools version compatible with Python 3.13
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
