# PacYam

[![Build Status](https://travis-ci.org/dstarner/pacyam.svg?branch=master)](https://travis-ci.org/dstarner/pacyam)

PacYam is a command line program that makes designing and developing of multi-environment Packer images a breeze. 

One of the major issues that I had with Packer was that the image description files got way too out of hand way too quickly. JSON adds up and nests very quickly, and this is not helped by the fact that comments are not allowed. It led to a very unsatisfying experience.

PacYam is the bridge between your development cycle and Packer. It allows you to define your machine images in YAML, which makes your descriptions easier to read. It also allows for multiple **template** and **variable** files to be used, meaning that each independent part of the image can stay organized and free of unrelated templates.

If we wanted to create an Ubuntu 18.04 image for example, we could have the following project structure:

```
. (ubuntu-18.04)
├── builders
│   ├── docker.yaml
│   ├── qemu.yaml
│   └── virtualbox.yaml
├── config.json
├── post-processors
│   ├── compress.yaml
│   └── vagrant.yaml
└── variables
    ├── default.yaml
    ├── dev-override.yaml
    └── prod-override.yaml
```

As long as everything is defined in `config.json`, which is explained below, you can break down your project into as small of components as desired. This also allows for reusable Packer descriptions, for common actions like exporting to a cloud registry or Vagrantfile.

## Core Concepts

Packer expects one final JSON file to build the image from. PacYam allows you to break down components of this JSON file into smaller, more managable YAML templates, which it will then compile and build together for you. There are three major keywords for PacYam: **templates**, **variables**, and the **config.json**.

### Templates

Templates are the individual YAML components that will end up building the build manifest. You can break these templates out representing specific environments, components (such as `builders` or `post-processors`), or in any way that suits your needs!

The keys and structure of these components get transformed into the Packer JSON file 1 --> 1. Whatever your YAML structure will be, the JSON will be identical. If multiple templates define the same top level keys, such as `builders`, these components will be intelligently merged together to represent the entire template. This means each unrelated `builder` can be placed in its own template file, cleaning up the project structure and thought process.

Templates are YAML files that can include [Jinja2](http://jinja.pocoo.org/docs/2.10/) rendering tags. This means that you have access to built in formatting functions, conditionals, loops, and more. These tags allow you to manage components and templates in every situation. Along with functions and control flow, these tags can also be **variables**, described in the next section.

Being YAML, these templates provide another major improvement over basic Packer templates; **comments**! Explain what stuff is, why it is, and more, by placing comments around your components.

```yaml
builders:
# Virtualbox build
- type: "virtualbox-iso"
  vm_name: "Example Box"
  iso_url: "ftp://.../...ubuntu.iso"
  # ... And whatever else you need
```

### Variables

Variables are configurable values that can be plugged into templates during compilation. Variables allow your team to build clean, declaritive templates that can still be flexible for multiple environments and configurations. Variables are defined in YAML files as top level values, and can be substituted in templates using [Jinja2](http://jinja.pocoo.org/docs/2.10/) rendering tags.

When using variables in templates, it is recommended to surround it with double quotes ("), so that your syntax highlighter reads the whole tag as a string value, instead of giving funky outputs.

**Variable File:**
```yaml
vm_name: "ubuntu-18.04"
vm_version: "v0.1"

iso_url: ""ftp://.../...ubuntu.iso""
```

**Template File:**
```yaml
builders:
# Virtualbox build
- type: "virtualbox-iso"
  vm_name: "{{ vm_name }}-{{ vm_version }}"
  iso_url: "{{ iso_url }}"
  # ... And whatever else you need
```

These variables can be found using the `config.json`, described below.

### Configuration

PacYam expects a `config.json` configuration file to locate and determine which files to use during compilation. Currently, there are two keys that are required in this configuration file; `"templates"` and `"variables"`. These need to be present, even if they are empty arrays (`[]`).

Use the `"templates"` key to list all of the template file paths that you wish to add to the Packer manifest. If there are any conflicting keys, then **priority will go to whichever template is listed last.** This does not include lists, where the lists are simply concatenated together.

Use the `"variables"` key to list all of the variable file paths that you wish to render the individual templates with. If there are any conflicting keys amongst files, then **priority will go to whichever variable file is listed last.**

For all file paths listed in `config.json`, they can be included either using the absolute path, *OR* the relative path from the location of the `config.json` file.

An example of the `config.json` file would be:

```
{
    "templates": [
        "builders/virtualbox.yaml"
    ],
    "variables": [
        "variables/default.yaml",
        "variables/overrides.yaml"
    ]
}
```


## Getting Started Guide

This guide assumes you already have experience writing [Packer template files](https://www.packer.io/intro/getting-started/build-image.html) and are familiar with the [PacYam Core Concepts](#core-concepts). 

First, install the package, either globally or in a virtual environment.

```python
# Recommended. Locally install
$ pip install pacyam

# Not recommended, but acceptable if desired globally.
$ sudo -H pip install pacyam
# OR 
$ sudo -H pip3 install pacyam
```

All commands can be viewed through running `pacyam -h`.

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
$ pylint pacyam
```

## Deploying to Pypi

Only Dan has access to do this, so its not worth your while to read...

**Update the version!!**

```bash
$ python3 setup.py sdist bdist_wheel
$ twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```