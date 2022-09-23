### Hexlet tests and linter status:
[![Actions Status](https://github.com/GregTMJ/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/GregTMJ/python-project-49/actions)


## Getting Started

#### Clone the current repository via command:
```git clone https://github.com/GregTMJ/python-project-49.git```

#### Check your pip version with the following command:
```python -m pip --version```

#### Make sure that pip is always up to date. If not, use the following:
```python -m pip install --upgrade pip```

#### Next install poetry on your OS. (the link is below)
[Poetry installation](https://python-poetry.org/docs/)


## Makefile

#### Using the Makefile you can generate all the needed packages for you virtual environment
```make install``` to install poetry packages. \
```make build``` to build your packages inside your project. \
```make publish``` It will let us execute the publish command knowing exactly what is going into the build. \
```make package-install``` installs the built package from our OS, so we can start using simple shell commands.

#### test your application by adding ```brain-games``` to the command line
