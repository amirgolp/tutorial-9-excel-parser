# NOMAD's parser example plugin

## Getting started

### Fork the project

Go to the github project page https://github.com/nomad-coe/nomad-parser-plugin-example, hit
fork (and leave a star, thanks!). Maybe you want to rename the project while forking!

### Clone your fork

Follow the github instructions. The URL and directory depends on your user name or organization and the
project name you choose. But, it should look somewhat like this:

```
git clone git@github.com:markus1978/my-nomad-parser.git
cd my-nomad-parser
```

### Install the dependencies

You should create a virtual environment. You will need the `nomad-lab` package (and `pytest`).
You need at least Python 3.9.

```
python3 -m venv .pyenv
source .pyenv/bin/activate
pip install -r requirements.txt --index-url https://gitlab.mpcdf.mpg.de/api/v4/projects/2187/packages/pypi/simple
```

**Note!**
Until we have a proper NOMAD release with the plugins functionality. Follow the instructions
in `requirements.txt` to make it work.

### Run the tests

Make sure the current directory is in your path, e.g. with bash: "`export PYTHONPATH=.`".

You can run automated tests with `pytest`:

```
pytest -svx tests
```

You can parse an example archive that uses the schema with `nomad`
(installed via `nomad-lab` Python package):

```
nomad parse tests/data/test.archive.yaml --show-archive
```

## Developing your schema

You can now start to develop you schema. Here are a few things that you might want to change:

- The metadata in `nomad_plugin.yaml`.
- The name of the Python package `nomadparserexample`. If you want to define multiple plugins, you can nest packages.
- The name of the example section `MyLabExcelSection`. You will also want to define more than one section.
- When you change module and class names, make sure to update the `nomad_plugin.yaml` accordingly.

To learn more about plugins, how to add them to an Oasis, how to publish them, read our
documentation on plugins: https://nomad-lab/prod/v1/docs/plugins.html
