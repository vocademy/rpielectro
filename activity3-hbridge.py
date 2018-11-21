# Motor control written by Simon Monk
# Comments by Brian Cox
# Updated 11/8/18
# Expects Python 3

import RPi.GPIO as GPIO    # Loads the module to support for the RPi's GPIO and gives it the name GPIO
import time                # Loads Python time support

#Defines and sets variable for GPIO pins
enable_pin = 18
in1_pin = 23
in2_pin =24

GPIO.setmode(GPIO.BCM)  # Sets board numbersing using the Broadcom SOC numbering scheme. As opposed to BOARD which refers to the pin numbers on the P1 header of the RPi's board
#Sets all pins as outputs
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

pwm = GPIO.PWM(enable_pin, 500) # Loads PWM support and sets the frequency at 500Hz
pwm.start(0) # Starts PWM and sets the duty cycle to 0. (range is 0 to 100)

#Creates a function to drive the motor forward
def clockwise():
    GPIO.output(in1_pin, True)    
    GPIO.output(in2_pin, False)

#Creates a function to drive the motor backward 
def counter_clockwise():
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin, True)

#Placing this section in a try/except construct helps us avoid exceptions (program errors)
try:
    while True:    #Continues looping through the statements in the while section forever. (until CTRL-C is pressed) 
        cmd = input("Command, f/r 0..9, E.g. f5 :") #takes input from user and places user's entry in the variable cmd
        direction = cmd[0] #Sets variable for direction based on first character of user's input
        if direction == "f": #Calls the function clockwise if user's input was f
              clockwise()    
        else:                #any other character from user results in a call to the function for reverse
              counter_clockwise()
        speed = int(cmd[1]) * 10 #Sets a variable for the speed by multiplying the input by 10. This gives a range of 0 to 100, which is the range for duty cycle
        pwm.ChangeDutyCycle(speed)  #Changes the duty cycle for the enable pin, therefore controlling the speed of the motor
except KeyboardInterrupt:        #Catches CTRL-C and allows program to exit cleanly
    pass                         #pass is a null operation. It acts as a placeholder.
finally:                         #This clause is always excuted before leaving the try statement.
    GPIO.cleanup()               #Only effects GPIO pins used in existing program. Sets those pins as False and removes their assignments.