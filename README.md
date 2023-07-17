# ProteinPurifier

## Introduction
This repository contains the Python application and custom **czpurifier** package that have been designed for automated protein purification by the CZ Biohub - SF Bioengineering team. All utilities support Python 3.7.

*This is a public snapshot of the automated protein purification repo as described in our 2023 preprint **PREPRINT LINK**.*

Maintenance of this repo is the responsibility of Robert Puccinelli. Please direct any communication to Robert Puccinelli via creation of an [issue](https://github.com/czbiohub-sf/automated-protein-purifier/issues).

This source describes Open Hardware, which is licensed under the CERN-OHL-W v2. 

Electronics hardware is described in the supplementary information of the publication.

CAD designs are provided in Onshape **ONSHAPE PUBLIC LINK**.

Software is licensed under BSD 3-Clause.

Copyright Chan Zuckerberg Biohub - San Francisco 2023.

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
* __MockHardwareSetup__ - Interface with the hardware simulators
* __RotaryControllerSim__ - Mocks the responses of the Rotary valve
* __PumpControllerSim__ - Mocks  the responses of the pump
* __ValveControllerSim__ - Mocks the responses of the valve controller
* __FractionCollectorSim__ - Mocks the responses of the fraction collector
* __TicStepperSim__ - Mocks the responses of the tic stepper driver

/middleware/
* __ControllerInterface__ - Links user interface to communication interface
* __DeviceInterface__ - Links communication interface to hardware interface
* __SimulatorInterface__ - Inherits DeviceInterface and links communication interface to simulator

/ui/
* __UICommands__ - Command wrappers to simplify controller-device communication
* __GUI_Controller__ - Controls communication between controller interface and GUI, connects to simulator, holds common GUI classes and accesses default parameters
* __FractionsSelected__ - Controls and maintains the fraction and flow columns selected for each step
* __Ui_MainWindow__ - The UI initialization and backend code for the window that pops up first
* __Ui_Purification__ - UI and backend for the basic purification window
* __Ui_CustomProtocol__ - UI and backend for custom protocol window
* __AddStep__ - UI and backend for each step added on the custom protocol window
* __Ui_FractionColumn__ - UI to show the fraction or flow selected
* __Ui_BuffersWindow__ - UI to display the buffers needed and adjust calibration
* __RunPurification__ - Runs the purifier using the inputs from the purification window
* __RunCustomProtocol__ - Runs the purifier using the inputs from the custom protocol window

### Data Files
* __purification_parameters.json__ - Holds the default parameters for purification window and default calibration settings

### Scripts
* __device_setup.py__ - Called by Linux service to activate purifier software
* __test_script.py__ - Example purification protocol

## Installation and Use
### Installing Module
1. Install PyQt5 globally (required to access pyqt5 package on the virtual environment). Run the command:
    >> sudo apt-get update<br>
    >> sudo apt-get install python3-pyqt5<br>
2. Create and/or activate a virtual environment in a convenient location with Python3
3. Download / clone this repository
4. Navigate to the base of the repository
5. Install setuptools (__pip install setuptools__)
6. Install module (__pip install .__)

NOTE: Developers may want to install the module with __pip install -e .__ so that changes they make to the module are immediately reflected when subsequently imported.

### Installing without cloning the repository
1. Install PyQt5 globally (required to access pyqt5 package on the virtual environment). Run the command:
    >> sudo apt-get update<br>
    >> sudo apt-get install python3-pyqt5<br>
2. Create and/or activate a virtual environment in a convenient location with Python3
3. Install module (__pip install git+https://github.com/czbiohub/ProteinPurifier__)

NOTE: It is unclear that module can be tested for completeness if directly installed.

### Updating Module from Repository
1. Pull changes from remote repository
2. Activate virtual environment with previous install
3. Navigate to the module directory
4. Update module (__pip install . --upgrade__)

### Updating Without Cloning
1. Update module (__pip install git+https://github.com/czbiohub/ProteinPurifier --upgrade__)

### Using GUI
1. If running the GUI for the first time, locate ProteinPurifier/czpurifier/ui/purification_parameters.json and update the PURIFIER_IP to refer to the ip of the device
2. Go to the base of the directory and run:
    >> python3 czpurifier/ui/main_window_gui.py

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
