#!/usr/bin/env python3
#############################################################################
# Filename    : Softlight.py
# Description : Control RGBLED with Potentiometer 
# Author      : www.freenove.com
# modification: 2021/1/1
########################################################################
import RPi.GPIO as GPIO
import time
from ADCDevice import *

ledRedPin = 29      # define 3 pins for RGBLED
ledGreenPin = 31
ledBluePin = 33
adc = ADCDevice(0x48) # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = ADS7830(0x48)
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
        
    global p_Red,p_Green,p_Blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledRedPin,GPIO.OUT)      # set RGBLED pins to OUTPUT mode
    GPIO.setup(ledGreenPin,GPIO.OUT)
    GPIO.setup(ledBluePin,GPIO.OUT)
    
    p_Red = GPIO.PWM(ledRedPin,1000)    # configure PMW for RGBLED pins, set PWM Frequence to 1kHz
    p_Red.start(0)
    p_Green = GPIO.PWM(ledGreenPin,1000)
    p_Green.start(0)
    p_Blue = GPIO.PWM(ledBluePin,1000)
    p_Blue.start(0)
    
def loop():
    while True:     
        value_Red = adc.analogRead(4)       # read ADC value of 3 potentiometers
        value_Green = adc.analogRead(3)
        value_Blue = adc.analogRead(2)
        p_Red.ChangeDutyCycle(100-value_Red*100/255)  # map the read value of potentiometers into PWM value and output it 
        p_Green.ChangeDutyCycle(100-value_Green*100/255)
        p_Blue.ChangeDutyCycle(100-value_Blue*100/255)
    
        # print read ADC value
        print ('ADC Value value_Red: %d ,\tvlue_Green: %d ,\tvalue_Blue: %d'%(value_Red,value_Green,value_Blue))
        time.sleep(0.01)

def destroy():
    adc.close()
    GPIO.cleanup()
    
if __name__ == '__main__': # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
