import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="clickup-python",
    version="1.0.0",
    description="Python developed library for ClickUp API",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/GearPlug/clickup-python",
    author="Johan Cardenas",
    author_email="jcardenas@gearplug.io",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests"],
    zip_safe=False,
)
