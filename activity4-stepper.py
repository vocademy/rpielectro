#Stepper program by Simon Monk
#Expects Python 3

import RPi.GPIO as GPIO    # Loads the module to support for the RPi's GPIO and gives it the name GPIO
import time                # Loads Python time support

GPIO.setmode(GPIO.BCM)     # Sets board numbersing using the Broadcom SOC numbering scheme. As opposed to BOARD which refers to the pin numbers on the P1 header of the RPi's board

#Set variables for GPIO pins
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

#Set all pins as outputs
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#Set the L293's enable pin to high so the H-Bridge is active
GPIO.output(enable_pin, 1)

#Setup function for a set of four steps forward
def forward(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    
#Setup funcion for a set of four steps backward
def backwards(delay, steps):  
  for i in range(0, steps):
    setStep(1, 0, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 0, 1)
    time.sleep(delay)
    setStep(0, 1, 1, 0)
    time.sleep(delay)
    setStep(1, 0, 1, 0)
    time.sleep(delay)

#Setup function to send out to all for GPIO pins based on the current step
def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

#Placing this section in a try/except construct helps us avoid exceptions (program errors)
try:
    while True:        #Continues looping through the statements in the while section forever. (until CTRL-C is pressed) 
        delay = input("Delay between steps (milliseconds)?")
        steps = input("How many sets of steps forward? ")
        forward(int(delay) / 1000.0, int(steps))
        steps = input("How many sets of steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))
except KeyboardInterrupt: #Catches CTRL-C and allows program to exit cleanly
    pass                  #pass is a null operation. It acts as a placeholder.
finally:                  #This clause is always excuted before leaving the try statement.
    GPIO.cleanup()        #Only effects GPIO pins used in existing program. Sets those pins as False and removes their assignments.