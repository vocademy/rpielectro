#Basic on/off relay control
#Expects Python 3
import RPi.GPIO as GPIO          #Loads the module to support for the RPi's GPIO and gives it the name GPIO
GPIO.setmode(GPIO.BCM)           #Sets board numbersing using the Broadcom SOC numbering scheme. As opposed to BOARD which refers to the pin numbers on the P1 header of the RPi's board
GPIO.setup(24,GPIO.OUT)          #Sets GPIO pin 24 as an output   
status = False                   #Establishes the variable 'status' and assigns it a value of 'False'. This will ensure that the relay stays off until the variable is set to True by the user.
try:                             #Placing this section in a try/except construct helps us avoid exceptions (program errors)
    while True:                  #Continues looping through the statements in the while section forever. (until CTRL-C is pressed) 
        GPIO.output(24, status)  #Controls pin 24 based on the value of the variable status. False sinks pin 24 to ground. True sources pin 24 to 3v3.
        input('Press [Enter] to toggle relay ' + ('Off' if status else 'On')) #Waits for the user to press enter. If 'status' is 'True', it adds the word'On' to the sentance. IF 'False', it adds 'Off'
        status = not status      #This line executes as soon as the user presses enter. It is a boolean operation that switches the variable from False to True or vice versa.
except KeyboardInterrupt:        #Catches CTRL-C and allows program to exit cleanly
    pass                         #pass is a null operation. It acts as a placeholder.
finally:                         #This clause is always excuted before leaving the try statement.
    GPIO.cleanup()               #Only effects GPIO pins used in existing program. Sets those pins as False and removes their assignments.
