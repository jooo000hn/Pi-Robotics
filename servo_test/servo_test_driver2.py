# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# https://github.com/adafruit/Adafruit_Python_PCA9685
# Install (python2.7): sudo pip install adafruit-pca9685 
# Install (python 3+): sudo pip3 install adafruit-pca9685

from __future__ import division 
import time
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 250  # Min pulse length out of 4096
servo_max = 520  # Max pulse length out of 4096

_PAN_SERVO_CHANNEL = 2
_TILT_SERVO_CHANNEL = 3

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
try: 
    while True:
        # Move servo on channel O between extremes.
        pwm.set_pwm(_PAN_SERVO_CHANNEL, 0, servo_min)
        time.sleep(1)
        pwm.set_pwm(_PAN_SERVO_CHANNEL, 0, servo_max)
        time.sleep(1)
except KeyboardInterrupt:
    # Reset servo to center
    pwm.set_pwm(_PAN_SERVO_CHANNEL, 0, 385)
    pwm.set_pwm(_TILT_SERVO_CHANNEL, 0, 605)
    exit(1)

