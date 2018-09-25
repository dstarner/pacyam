# PacYam

PacYam is a command line program that makes designing and developing of multi-environment Packer images a breeze. 

One of the major issues that I had with Packer was that the image description files got way too out of hand way too quickly. JSON adds up and nests very quickly, and this is not helped by the fact that comments are not allowed. It led to a very unsatisfying experience.

PacYam is the bridge between your development cycle and Packer. It allows you to define your machine images in YAML, which makes your descriptions easier to read. It also allows for multiple **template** and **variable** files to be used, meaning that each independent part of the image can stay organized and free of unrelated templates.

## Development

Getting started with development is achieved by cloning the repository, and getting `virtualenv` set up.

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r dev-requirements.txt
```

## Running Tests

Run tests with the following:

```bash
$ pytest
```

## Running the Linter

Run the linter with the following:

```bash
$ pylint scripts tests
```