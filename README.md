# ProteinPurifier

## Introduction
This repository contains the Python application and custom **czpurifier** package that have been designed for the automated protein purification project undertaken by the CZ Biohub Bioengineering team. All utilities support Python 3.7+.

## Contents

### Classes for Advanced Programming
/hardware/
* __HardwareController__ - Interfaces with hardware peripherals
* __PurifierHardwareSetup__ - Configures hardware peripherals according to specified file
* __PumpController__ - Base class for a pump controller
* __PumpControllerTic__ - Valve controller for use with a Tic stepper driver
* __RotaryController__ - Base class for a rotary valve
* __RotaryControllerTic__ - Rotary valve for use with a Tic stepper driver
* __ValveController__ - Base class for a valve controller
* __ValveControllerMCP23017__ - Valve controller utilizing the I2C protocol
* __MockHardwareSetup__ - Interface with hardware simulators

/middleware/
* __ControllerInterface__ - Links user interface to communication interface
* __DeviceInterface__ - Links communication interface to hardware interface
* __SimulatorInterface__ - Links communication interface to simulator

/ui/
* __UICommands__ - Command wrappers to simplify controller-device communication

### Configuration Files
* __autopurifier_hardware.config__ - Hardware parameters and selectable configurations for initialization
* __gui_purification_parameters.json__ - Holds the default parameters for purification window and calibration settings
* __logger_client.config__ - Parameters for the logs generated by clients
* __logger_server.config__ - Parameters for the logs generated by the server


### Scripts
* __device_setup.py__ - Called by Linux service to activate purifier software
* __test_script.py__ - Example purification protocol

## Dependencies
* czbiohub :: pymotors
* czbiohub :: pyconfighandler
* smbus2
* zmq
* vext.pyqt5


## Installation and Use
### Installing Module
1. Install PyQt5 globally (required to access pyqt5 package on the virtual environment). Run the command:
    >> sudo apt-get update<br>
    >> sudo apt-get install python3-pyqt5<br>
2. Create and activate a virtual environment in a convenient location with Python3
3. Clone or download this repository
4. Navigate to the base of the repository
5. Install setuptools (__pip install setuptools__)
6. Install module (__pip install .__)

NOTE: Developers may want to install the module with __pip install -e .__ so that changes they make to the module are immediately reflected in the next import.

### Updating Module from Repository
1. Pull changes from remote repository
2. Activate virtual environment with previous install
3. Navigate to the module directory
4. Update module (__pip install . --upgrade__)

### Using GUI
1. If running the GUI for the first time, locate ProteinPurifier/czpurifier/ui/purification_parameters.json and update the PURIFIER_IP to refer to the ip of the instrument.
2. Go to the base of the directory and run:
    >> python3 czpurifier/ui/main_window_gui.py

### Using Module
1. Edit files to include `import czpurifier` or a variant such as `from czpurifier import {class_name}`
2. Activate virtual environment with module installed
3. Execute python script or application

## Usage
The user interface was designed to simplify operation and strips away most arguments needed to operate the machine. A list of methods and basic examples of how to use them can be found at: https://github.com/czbiohub/ProteinPurifier/tree/master/czpurifier/ui

Scripts that have been used for set up, clean up or various experiments can be found at: https://github.com/czbiohub/ProteinPurifier/tree/master/scripts
