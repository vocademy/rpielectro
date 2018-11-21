# servo written by Simon Monk
# comments by Brian Cox
# Updated 11-6-18
# Expects Python 3


from Tkinter import *       #Load Python's GUI package
import RPi.GPIO as GPIO     #Load module to support RPi's GPIO pins and create object called GPIO
import time                 #Load module that allows RPi to work with time

GPIO.setmode(GPIO.BCM)      #Configures GPIO numbering system
GPIO.setup(18, GPIO.OUT)    #Configures GPIO pin 18 as an output
pwm = GPIO.PWM(18, 100)     # Loads PWM support and sets the frequency at 100Hz
pwm.start(5)                #Starts PWM on pin 24 and sets the duty cycle to 0. (range is 0 to 100)

class App:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5   
        pwm.ChangeDutyCycle(duty)     # Changes duty cycle of PWM based on the position of the slider, which moves the servo
        
    def Exit(self):              # Creates exit button which will clean the GPIO pins and close the window
        GPIO.cleanup()
        root.destroy()

## Sets parmeters for the main window
root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x80+0+0")
root.mainloop()
