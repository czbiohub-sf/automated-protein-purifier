# ProteinPurifier

## Introduction
This repository contains the Python application and custom **czbiohub.purifier** package that have been designed for the automated protein purification project undertaken by the CZ Biohub Bioengineering team. All utilities support Python 3.7+.

## Contents

* __RotaryController__ - Base class for a rotary valve
* __RotaryControllerTic__ - Rotary valve for use with a Tic stepper driver
* __ValveController__ - Base class for a valve controller
* __ValveControllerI2c__ - Valve controller utilizing the I2C protocol

## Dependencies
ValveControllerI2c :: smbus2


## Installation and Use
### Installing Module
1. Create and/or activate a virtual environment in a convenient location with Python3
2. Download / clone this repository
3. Navigate to the base of the repository
4. Install setuptools (__pip install setuptools__)
5. Test the module for completeness (__python setup.py test__)
6. Install module (__pip install .__)

### Updating Module from Repository
1. Pull changes from remote repository
2. Activate virtual environment with previous install
3. Test the module for completeness (__python setup.py test__)
3. Update module (__pip install . --upgrade__)

### Using Module
1. Edit files to include `import czbiohub.purifier` or a variant such as `from czbiohub.purifier import {class_name}`
2. Activate virtual environment with module installed
3. Execute python script or application


## How to Contribute
If you would like to contribute to PyMotors, please review the guidelines described in [CONTRIBUTING.md](https://github.com/czbiohub/capper-decapper/blob/master/CONTRIBUTING.md).
