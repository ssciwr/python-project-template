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

This repository contains a github action in `./github/workflows/'. This will run unit tests and update the documentation upon push to the master branch. It will also run unit tests upon pull request.