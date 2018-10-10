import os
import setuptools

from pacyam.pacyam import __version__


name = 'pacyam'
version = __version__
author = 'Daniel Starner'
email = 'starner.daniel5@gmail.com'
description = 'Command line program that makes designing and developing of multi-environment Packer images a breeze.'
repository = 'https://github.com/dstarner/pacyam'
keywords = ['Packer', 'Vagrant', 'Virtualbox']

def _strip_comments(l):
    return l.split('#', 1)[0].strip()


def _pip_requirement(req):
    if req.startswith('-r '):
        _, path = req.split()
        return reqs(*path.split('/'))
    return [req]


def _reqs(*f):
    return [
        _pip_requirement(r) for r in (
            _strip_comments(l) for l in open(
                os.path.join(os.getcwd(), *f)).readlines()
        ) if r]


def reqs(*f):
    """Parse requirement file.
    Example:
        reqs('default.txt')          # requirements/default.txt
        reqs('extras', 'redis.txt')  # requirements/extras/redis.txt
    Returns:
        List[str]: list of requirements specified in the file.
    """
    return [req for subreq in _reqs(*f) for req in subreq]


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=repository,
    keywords=keywords,
    packages=setuptools.find_packages(exclude=('tests', 'pacyam.tests', 'pacyam/tests')),
    install_requires=reqs('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': ['pacyam=pacyam.pacyam:main'],
    }
)