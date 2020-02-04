# Purifier Command Cheatsheet

#### Notes
**bold** is a command name.
*italic* is an optional argument.
Examples are provided at the end of the document.

#### Machine Commands

1. **connect**(config_mode, device_address, *number_of_pumps*) - Connect to and reset the machine.
2. **disconnect**() - Disconnect from the machine.
3. **getMachineStatus**() - Retrieve state of machine connected to.
4. **resetConnection**(device_address) - Force the machine to become available for connection.
5. **resetMachine**() - Rehome the machine  and put into a known working state.
6. **setStandby**() - Put the machine into a known working state.

#### Waste Valve Commands
1. **openAllWaste**() - Pass all input to waste.
2. **closeAllWaste**() - Pass all input to fraction collector.
3. **openPreColumnWaste**() - Pass buffer/load above column to waste.
4. **closePreColumnWaste**() - Pass buffer/load through the column.
5. **openPostColumnWaste**() - Pass column flow-through to waste.
6. **closePostColumnWaste**() - Pass column flow-through to fraction collector.

#### Input Valve Commands
1. **selectBuffers**() - Flow the buffers and not the load.
2. **selectLoad**() - Flow the load and not the buffers.
3. **selectPort**(PORT_NAME) - Select buffer at PORT_NAME.
  1. WASH
  2. LOAD_BUFFER
  3. ELUTION
  4. BASE

#### Fraction Collector Commands
1. **selectFraction**(Position) - Move fraction collector to position.
   1. Frac1
   2. Frac2
   3. Frac3
   4. Frac4
   5. Frac5
   6. Frac6
   7. Frac7
   8. Frac8
   9. Frac9
   10. Frac10
   11. Flow1
   12. Flow2
   13. Flow3
   14. Flow4
   15. Safe

#### Pump Commands
1. **pump**(column_volumes) - Pump the specified volume out of the input buffer/load reservoir.

## Example

### Purge bubbles from wash line and then flow to post column waste

`from czpurifier.ui import UICommands`

`ui = UICommands()`

`ui.connect("1mL", "pure1")`

`ui.selectPort("WASH")`

`ui.pump(0.5)`

`ui.closePreColumnWaste()`

`ui.pump(0.5)`

### Flow elution to fraction collector with 2 pumps

`from czpurifier.ui import UICommands`

`ui = UICommands()`

`ui.connect("1mL", "pure1", 2)`

`ui.selectPort("ELUTION")`

`ui.pump(0.5)`

`ui.closeAllWaste()`

`ui.selectFraction("Frac1")`

`ui.pump(1)`

`ui.selectFraction("Frac2")`

`ui.pump(1)`

`ui.selectFraction("Safe")`
