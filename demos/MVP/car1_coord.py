import motorControl, servoControl, xbeeControl 
from time import sleep
import sys

# Instantiate object
motor = motorControl.MotorControl()
xbee = xbeeControl.XbeeControl()

if len(sys.argv) is not 2:
    print('''
    Usage: python car1_coord.py [options]
    Mode options: 1        (Scenario #1)
                  2        (Scenario #2)
    Examples:
    python car1_coord.py 1 (Demo Scenario #1)
    python car1_coord.py 2 (Demo Scenario #2)
        ''')
    sys.exit()

try:
    # Scenario #1
    if(sys.argv[1] == '1'):
        print(sys.argv[1], "Scenario #1")
        motor.forward()
        sleep(3)
        xbee.send("1", "C")
        motor.stop()
        motor.cleanup()
        sys.exit(1)

    # Scenario #2
    if(sys.argv[1] == '2'):
        print(sys.argv[1], "Scenario #2")
        motor.forward()
        sleep(3)
        xbee.send("2", "C")
        motor.forward()
        sleep(3)
        motor.stop()
        motor.cleanup()
        sys.exit(1)

except KeyboardInterrupt:
    motor.stop()
    motor.cleanup()
    sys.exit(1)


    