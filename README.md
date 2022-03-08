**Content of the source code documentation**  

1. Name and short description of the software, authors, date of initial development
1. Main features
1. Main requirements
1. Further information:
    1. [Input examples and explanations, step-by-step tutorial](doc/input.md)
    1. [More detailed description of scientific approach and input variables reference](doc/method.md)
    1. [Validity range of the parameters](doc/parameters.md)
    1. [License, bug tracker, references, citations](doc/further.md)
    1. [Source code description](doc/sphinxdoc.md) - functions and classes, modules, variables

# python-project-template

This is a template for your software project. The example code calculates the side length of a square or a pentagon, that contains the same area as a circle of given radius r.

*Scientific Software Center, Heidelberg University, 12/2020*

The code can compute side lengths of two geometric objects - of a square and a pentagon. You have to select either one, output of both objects is currently not implemented. For usage see [input](doc/input.md). The methods are described in [method](doc/method.md). Details on the input parameters are given in [parameters](doc/parameters.md). A detailed source code description is given through the sphinx documentation (here will be the link to the doc).

The program requires a working python environment with `numpy` installed. 
The documentation requires `sphinx` to be installed on your system.

For installation, run  
`source setup.sh`

This will pip-install sphinx on your system.

If you want to run the test module manually, execute  
`python -m unittest`  
in the `src/` directory.

## github actions

This repository contains a github action in `./github/workflows/`. This will run linting, unit tests and update the documentation upon push to the master branch and upon pull request. The action can also be run manually in the "Actions" tab on the github website.

### Linting
The linter (in this case, `flake8` will point out potential bugs, errors, styling issues, and suspicious code.

### Testing
You should always test your code against a reference. In this template, we used `unittest` which is a python core module, but `pytest` is also a popular option (it needs to be pip installed though).

So far, only *unit tests* are included in the code template (that is, tests of a specific component of the software), but as you develop your software, you should also add `integration tests` that check the overall behaviour of your code.

In the github action, the tests are performed under ubuntu, windows and mac operating systems to ensure that the code runs in different environments. Also, two different python versions are tested right now, 3.8 and 3.9.

### Source Code Documentation: Functions, modules, classes, ...
The documentation should be updated as you update your code. Include appropriate method descriptions in your code and `sphinx` will update the documentation html for your functions, classes, etc. The documentation is build using `make html` in the `doc` folder. On your local machine, you can navigate to `doc/build/index.html` and check the styling.
If your code is in a public repository, you can push your sphinx documentation to [Read the docs](https://ssc-hd-python-project-template.readthedocs.io/en/latest/?).
