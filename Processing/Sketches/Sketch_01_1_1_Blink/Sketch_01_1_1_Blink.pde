/*****************************************************
 * Filename    : Sketch_01_1_1_Blink
 * Description : Make an led blinking.
 * auther      : www.freenove.com
 * modification: 2020/12/07
 *****************************************************/
import processing.io.*;

int ledPin = 17;    //define ledPin
boolean ledState = false;    //define ledState

void setup() {
  size(100, 100);
  frameRate(1);        //set frame rate
  GPIO.pinMode(ledPin, GPIO.OUTPUT);    //set the ledPin to output mode  
}

void draw() {
  ledState = !ledState;
  if (ledState) {
    GPIO.digitalWrite(ledPin, GPIO.HIGH);    //led on 
    background(0,0,255); //set the fill color of led on
  } else {
    GPIO.digitalWrite(ledPin, GPIO.LOW);    //led off
    background(102); //set the fill color of led off
  }
}
