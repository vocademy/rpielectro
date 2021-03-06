# Original gui_slider written by Simon Monk
# Updates and comments by Brian Cox
# Updated 11-20-18
# Expects Python 3

from tkinter import *            # Loads Python's GUI package
import RPi.GPIO as GPIO          # Loads the module to support for the RPi's GPIO and gives it the name GPIO
import time                      # Loads Python time support

GPIO.setmode(GPIO.BCM)           # Sets board numbering using the Broadcom SOC numbering scheme. As opposed to BOARD which refers to the pin numbers on the P1 header of the RPi's board
GPIO.setup(24, GPIO.OUT)         # Sets GPIO pin 24 as an output
pwm = GPIO.PWM(24, 500)          # Loads PWM support on pin 24 and sets the frequency at 500Hz
pwm.start(0)                     # Starts PWM on pin 24 and sets the duty cycle to 0. (range is 0 to 100)


# Setup support for window and slider
class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        bt1 = Button(master, text="Exit", command=self.Exit)
        bt1.pack()
        scale = Scale(frame, from_=0, to=100,
                      orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))          # Changes duty cycle of PWM based on the position of the slider

    def Exit(self):                               # Creates exit button which will clean the GPIO pins and close the window
        GPIO.cleanup()
        root.destroy()


# Sets parmeters for the main window
root = Tk()
root.wm_title('Motor Speed')
app = App(root)
root.geometry("400x80+0+0")
root.mainloop()
