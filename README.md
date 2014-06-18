# [pistol](https://pypi.python.org/pypi/pistol)

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

#### Aliases

- load


### uninstall

Removes a Python package.

#### Aliases

- unload
- whip


### publish

Upload a package to PyPi.


### update

Look through packages for higher versions.

#### Aliases

- reload


### link

Similar to NPM link for linking development libraries.  

#### Arguements

- --user=[pypi_username]
- --pass=[pypi_password]


### search

Search PyPi for a package.

#### Aliases

- scope


## Installation

`pip install pistol`


## package.yaml

The `package.yaml` is structured as follows.

```yaml
name: pistol
version: 0.0.1
description: >
  A python package utility to make packaging, sharing, installing, and managing
  libraries simpler.
dependencies:

  common: # Here are common required dependancies.
    - pip
  develop:

  test:

```
