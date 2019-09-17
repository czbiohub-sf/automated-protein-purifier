# Contributing to PyCapper

For ease of use, modules should follow the formatting guidelines listed below. Doing so will ensure thorough documentation, seamless importation, effective version control, and minimal code-breaking revisions. Pull requests that do not annotate changes in CHANGES.md and increment the version in setup.py will not be merged.


### Repository Format
This module contains files for pip installing, the source code, and tests to evaluate the health of the source code.
```
ThisRepository
|-- README.md
|-- CHANGES.md
|-- LICENSE
|-- Makefile
|-- setup.py
|-- application
    |--- app.py
    |--- __main__.py
    |--- __init__.py
    |--- src
         |---- __init__.py
         |---- file_a.py
         |---- file_b.py
    |--- tests
         |---- __init__.py
         |---- fake_module.py
         |---- test_file_a.py
         |---- test_file_b.py
```
### File Formats

#### README.md
README.md is a long format description of the module. It should annotate the purpose of the module, the public classes and functions available if imported as well as dependencies.

```markdown
# module_name

## Overview
The purpose of this module is to provide ____
utilities for applications including ____. Other
useful information is also included here.

## Contents

Class1:
* Purpose

Class2:
* Purpose

function1:
* Purpose

## Requirements
In order for this module to function, the following
packages will be installed:
* dependency1
* dependency2
* dependency3
```

#### setup.py
setup.py allows for modules and their dependencies to be imported via pip. It also permits for version controlling of modules in use.
```python
import setuptools

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject/module",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=['docutils>=0.3'],
    test_suite="tests",
    classifiers=[
        "Your Classifiers :: Go Here",
    ],
)
```
#### Makefile
The Makefile benefits both module users and module contributors by testing the associated module and indicating errors that may have been introduced in a recent revision. For contributors, using the Makefile is similar to using continuous integration in that it allows contributors to validate an interface and confirm that everything is working as it is expected to.

__How to use:__
Before making a change, run the makefile to confirm that everything is functional. If it isn't identify the errors and correct them so that all tests pass. Once all tests pass, make your desired change and run the makefile to see your changes have broken the code. If the code is broken, fix the errors before pushing the changes to the repo. If adding more functionality to the code base, make unit tests that confirm that the interface is behaving as expected. Also check edge cases to weed out odd behavior.

#### src/init
`__init__.py` in the src directory contains aliases for public classes and functions so that they do not need to be imported as `module.file_name.Class` and can be imported as `module.Class`. The file is formatted as such:
```
from .file_a import Class1
from .file_b import functionName

```
#### src/file_a and file_b
Python classes and functions that are tightly coupled should be combined into one file. If they are not tightly coupled, consider putting them in separate files. IE - a file containing an implementation specific motor driver class should also include the implementation specific communication protocol class if it is unlikely that one would be used without the other.

#### tests/init

`__init__.py` in the tests directory is required for automatically discovering the unit tests. It should be an empty file.

#### tests/fake_module
`fake_module.py` in the tests directory is used to mock classes that are not available during testing or would greatly impede testing. IE - if testing a class that interfaces with AWS data, it would make sense to fake the interface to AWS so that communicating with the server isn't required each time a test is executed.

#### tests/test_file_a and test_file_b
Each test file in the tests directory contains a battery of tests that are used to evaluate the interface and inner workings of the source code. They should check the interface as it is expected to be used and edge cases where odd behavior might arise.

#### CHANGES.md
Every pull request must increment the release version and appended a summary of notable changes in the CHANGES file.
