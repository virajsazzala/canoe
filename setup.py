import setuptools

from setuptools import find_packages
from distutils.core import setup

setup(
    name="canoe",
    version='0.0.1',
    package_dir={'':"."},
    packages=find_packages(),
    scripts=[
        "scripts/canoe"
    ],
    python_requires= ">=3.10"
)