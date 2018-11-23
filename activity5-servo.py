#Servo demonstration. GUI slider code by Simon Monk. Servo control by Brian and Chris Cox
#Updated 11/23/18
from tkinter import *     # Loads Python's GUI package
import RPi.GPIO as GPIO   # Loads the module to support for the RPi's GPIO and gives it the name GPIO
import time               # Loads Python time support

GPIO.setmode(GPIO.BCM)    # Sets board numbering using the Broadcom SOC numbering scheme. As opposed to BOARD which refers to the pin numbers on the P1 header of the RPi's board
GPIO.setup(18, GPIO.OUT)  # Sets GPIO pin as an output
pwm = GPIO.PWM(18, 50)    # Loads PWM support and sets the frequency at 50Hz
pwm.start(2.5)            # Starts PWM and sets inital duty cycle at 2.5 (0 degrees for the servo)

class App:
    #Define variables that will be used to calculate duty cycle
    in1 = 0
    in2 = 180        
    out1 = 2.5
    out2 = 12.5
    fltOffset = 10 #Determined by (out2 - out1)
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        bt1 = Button(master, text="Exit", command=self.Exit)
        bt1.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        #The formula below determines the duty cycle it by taking the angle selected by the user (0 to 180) and matching it to a number in the range needed for the duty cycle (2.5 to 12.5).
        #A duty cycle of 2.5 is interpreted as 0 degrees by the servo. A duty cycle of 12.5 is interpreted as 180 by the servo.
        #Inspired by the map() function in Arduino C. Actual formula is duty = (angle-in1)/(in2-in1)*(out2-out1)+out1
        duty = ((float(angle) / self.in2) * self.fltOffset) + self.out1 
        #Sends duty cycle to servo
        pwm.ChangeDutyCycle(duty)
                
    def Exit(self):                               # Creates exit button which will clean the GPIO pins and close the window
        GPIO.cleanup()
        root.destroy()    

# Sets parmeters for the main window
root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("400x80+0+0")
root.mainloop()


