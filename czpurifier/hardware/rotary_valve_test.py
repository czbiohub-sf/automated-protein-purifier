# Script to test/debug the rotary valve in the protein PurifierHardwareSetup
# Rafael Gomez-Sjoberg
# 2021-05-07

""" Default configuration Parameters
ROTARY_STEPS_REV    = 200
ROTARY_MICROS       = 8
ROTARY_MOTOR_CURR   = 25
ROTARY_HOME_DIR     = rev
ROTARY_ENCODE_PIN   = TX
ROTARY_THRESH_L     = 0x3000
ROTARY_THRESH_U     = 0xDF00
ROTARY_NUM_PORTS    = 8
ROTARY_PORT_1       = WASH
ROTARY_PORT_2       = LOAD_BUFFER
ROTARY_PORT_3       = ELUTION
ROTARY_PORT_4       = BASE
BUS                 = 3
ROTARY_ADDR         = 0x10
"""

from rotary_controller import RotaryControllerTic
from pymotors import TicStepper, TicStage

bus = 3
addr = 0x10
steps_rev = 12000
micros = 8
home_dir = 'rev'
encoder_pin = 'TX'
motor_current = 25
th_lower = 0x3000
th_upper = 0xDF00
num_ports = 8
port_names = ['WASH', 'LOAD_BUFFER', 'ELUTION', 'BASE', 'NONE', 'NONE', 'NONE', 'NONE']
seek_speed = 200000 # 2000000
motor_curr = 2

motor = TicStepper(com_type='I2C', port_params=bus, address=addr,
    input_steps_per_rev=steps_rev, input_rpm=60)
motor.microsteps = 1 / micros

rotary = RotaryControllerTic(MotorObj=motor, home_dir=home_dir,
    analog_pin=encoder_pin, motor_current=motor_current,
    thresh_lower=th_lower, thresh_upper=th_upper,
    seek_vel=seek_speed)

#exec(open("rotary_valve_test.py").read())
#rotary._seekPort(True)
