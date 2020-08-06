# ProteinPurifier

## Introduction
This repository contains the Python application and custom **czpurifier** package that have been designed for the automated protein purification project undertaken by the CZ Biohub Bioengineering team. All utilities support Python 3.7+.

## Contents

### Classes
/hardware/
* __HardwareController__ - Interfaces with hardware peripherals
* __PurifierHardwareSetup__ - Configures hardware peripherals according to specified file
* __PumpController__ - Base class for a pump controller
* __PumpControllerTic__ - Valve controller for use with a Tic stepper driver
* __RotaryController__ - Base class for a rotary valve
* __RotaryControllerTic__ - Rotary valve for use with a Tic stepper driver
* __ValveController__ - Base class for a valve controller
* __ValveControllerI2c__ - Valve controller utilizing the I2C protocol

/middleware/
* __ControllerInterface__ - Links user interface to communication interface
* __DeviceInterface__ - Links communication interface to hardware interface

/ui/
* __UICommands__ - Command wrappers to simplify controller-device communication

### Scripts
* __device_setup.py__ - Called by Linux service to activate purifier software
* __test_script.py__ - Example purification protocol

## Dependencies
PurifierHardwareSetup :: pymotors<br>
PurifierHardwareSetup :: pyconfighandler<br>
ValveControllerI2c :: smbus2<br>
ControllerInterface :: zmq<br>
DeviceInterface :: zmq<br>


## Installation and Use
### Installing Module
1. Create and/or activate a virtual environment in a convenient location with Python3
2. Download / clone this repository
3. Navigate to the base of the repository
4. Install setuptools (__pip install setuptools__)
5. Install module (__pip install .__)

NOTE: Developers may want to install the module with __pip install -e .__ so that changes they make to the module are immediately reflected when subsequently imported.

### Installing without cloning the repository
1. Create and/or activate a virtual environment in a convenient location with Python3
2. Install module (__pip install git+https://github.com/czbiohub/ProteinPurifier__)

NOTE: It is unclear that module can be tested for completeness if directly installed.

### Updating Module from Repository
1. Pull changes from remote repository
2. Activate virtual environment with previous install
3. Navigate to the module directory
4. Update module (__pip install . --upgrade__)

### Updating Without Cloning
1. Update module (__pip install git+https://github.com/czbiohub/ProteinPurifier --upgrade__)

### Using Module
1. Edit files to include `import czpurifier` or a variant such as `from czpurifier import ValveControllerI2c`
2. Activate virtual environment with module installed
3. Execute python script or application

### Using Module
1. Edit files to include `import czpurifier` or a variant such as `from czpurifier import {class_name}`
2. Activate virtual environment with module installed
3. Execute python script or application

## Usage
The user interface was designed to simplify operation and strips away most arguments needed to operate the machine. A list of methods and basic examples of how to use them can be found at: https://github.com/czbiohub/ProteinPurifier/tree/master/czpurifier/ui

Scripts that have been used for set up, clean up or various experiments can be found at: https://github.com/czbiohub/ProteinPurifier/tree/master/scripts
