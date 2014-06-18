pistol
======

A python package utility to make packaging, sharing, installing, and managing
libraries simpler.

Using Pip and requirements.txt has sufficed for python development thus far,
though is lacking in comparison to tools such as Gem and NPM. For example,
NPM allows a developer to distinguish between production and development
dependancies. This functionality is not conveniently baked into Pip. Pistol
is driven by a `package.yaml` file that contains a map of `tag`s to lists of
dependencies. Dependencies may then be installed using
`pistol install[=tag] [package]`.

## Commands

### init

Creates a basic pistol python package.

### install

Installs a python package from PyPi.

`pistol install[=tag] [package] --save=[tag]``

#### Arguements

- --save=[key]

### uninstall

Removes a Python package.

## Installation

`pip install pistol`
