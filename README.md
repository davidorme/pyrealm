# The `pyrealm` package

These are development notes for the package, user documentation can be found at:

https://pyrealm.readthedocs.io/

## Overview

This a Python 3 package intended to provide a common framework for a number of
related models of plant productivity, growth and demography.


## Code development

The codebase is developed in `git` with a repository at:

https://github.com/davidorme/pyrealm

It uses the `git flow` model for development and release. Briefly:

* All code development should happen on the general `develop` branch or on specific 
  `feature/feature_name` branches.
* Candidate release versions should be made on specific `release/x.y.z` branches
  and these are then committed to the `master` branch only after final checking.
* The `master` branch should only ever contain commits representing new release
  versions - do not work on the `master` branch.

## Continuous integration

The project uses continuous integration on the Travis platform to check that the
package is building correctly as changes are committed to Github. The status of 
builds can be seen at:

[https://travis-ci.com/github/davidorme/pyrealm](https://travis-ci.com/github/davidorme/pyrealm)

## Documentation

The `pyrealm` package is documented using `sphinx`, with source material in the
`source` directory. 

The documentation in `source` uses [Myst Markdown](https://myst-parser.readthedocs.io/en/latest/)
rather than the standard `sphinx` reStructuredText (`.rst`) format. This is 
because the documentation uses the `myst_nb` extension to `sphinx` that supports
running documentation as a Jupyter notebook: the built documentation includes
examples of running code and output plots to demonstrate the use and behaviour 
of the package.

The `sphinx` configuration includes the `sphinx.ext.mathjax`
extension to support mathematical notation. This has been configured to also 
load the `mhchem` extension, supporting the rendering of chemical notation.

### Docstrings

The module codes uses docstrings written in the 
[Google style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
Unlike the main documentation pages, the docstrings in code are written using 
reStructuredText because the `autodoc` functions in `sphinx` rely on `rst` 
inputs. This allows the function documentation to be stored alongside the code
and included simply into the documentation. 

### Building the documentation

Additional python packages given in `source/requirements.txt` are needed
to build the documentation. To actually build the documentation, use
`make` in the package root, which will use the `Makefile` created by
`sphinx-quickstart`. 

```bash
make html
```

### Online documentation

TODO - change this to github deployment?

The documentation for the package is hosted at:

https://pyrealm.readthedocs.io/en/develop/pmodel.html

This has been configured to build commits to the `master` branch, which should
generate version specific sets of documentation.



### Referencing

The documentation uses the `sphinxcontrib-bibtex` package to support citations.
This uses Latex like citation keys in the documentation to insert references and
build a bibliography. The reference library in `source/refs.bib` needs to be
kept up to date with the literature for the project.

At present, that package uses a rather ugly citation style. I'm hoping the
`sphinx_astrorefs` package will help out, but there is currently an issue
getting that package to load.

## Testing

### Developer installation

Use the local directory as an editable installation of the package

```
pip install -e .
```

### Using `doctest`

The package docstrings contain `doctest` examples of code use. These are
intended to demonstrate use and to validate a reference set of inputs against
expected outputs. They do not provide extensive unit testing! To run the
docstring tests, use:

```bash
python -m doctest pyrealm/pmodel.py

``` 

### Using `pytest`

The `test` directory contains `pytest` modules to provide greater testing of
different input combinations (scalars and arrays) and to check errors are
raised correctly.

```bash
pytest
```

### Reference values for testing

The sources of the reference inputs and outputs are:

`pmodel` module: 
    Benjamin Stocker's [`rpmodel`](https://github.com/stineb/rpmodel/tree/master/R)
    implementation of the P-model in R. The `test` directory contains a YAML 
    file of inputs (`test_inputs.yaml`) and an `R` script (`test_output_rpmodel.R`)
    that are used to generate a larger YAML file (`test_outputs_rpmodel.R`) that
    are loaded and validated against {mod}`pyrealm.pmodel` by `test_pmodel.py`.


## Continuous Integration

## Git flow

### Configure `git`

It is easier if `git` is configured to push new tags along with commits. This essentially just means that new releases can be sent with a single commit, which is simpler and saves Travis from building both the the code commit and then the tagged version. This only needs to be set once.

```bash
set git config --global push.followTags true
```


Using git-flow and travis

Use git flow to create a release 

```bash
git flow release start 0.3.0
```

and then bump the version number in `version.py`.

Check the package builds and installs locally:


```bash
python setup.py sdist bdist_wheel
```

and use

```
git flow release publish x.y.z
```

to get the branch onto the origin and hence into Travis

### Use twine to check it passes onto testpypi

Remembering to change the version number, use `twine` to test:

```
twine upload -r testpypi dist/*x.y.z*
```

### Check the documentation builds

Go to RTD and select the  release branch in advanced admin and try and build.


## PyPi

To upload the new version to testpypi, checkout master and run

```
python setup.py sdist bdist_wheel
```

Remembering to change the version number, you can then create an account at pypi and testpypi and use `twine` to test:

```
twine upload -r testpypi dist/*x.y.z*
```



Once all seems well,  finish the release, go to the master branch and push it to create the tagged version on github.

```bash
git flow release finish x.y.z
```

## PyPi again

To upload the new version to testpypi, checkout master and run

```
python setup.py sdist bdist_wheel
```
release the distribution for use via `pip`

```
twine upload dist/*x.y.z*
```

Once that is done, switch back to `develop` and bump the version number to add `.post9000` to show the code is in development again.
