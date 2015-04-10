# import RPi.GPIO as GPIO         Import GPIO library
import time                                #Import time library
# GPIO.setmode(GPIO.BCM)                     #Set GPIO pin numbering 
Output = [False, False, False, False]
Trig = [23,27,17,22]                                  #Associate  TRIG
Echo = [24,25,16,12]                                  #Associate ECHO
car_check = 0
def checkSensor():
  print "Distance measurement in progress"
  for i in range(len(Trig)):
    GPIO.setup(Trig[i],GPIO.OUT)                  #Set pin as GPIO out
    GPIO.setup(Echo[i],GPIO.IN)                   #Set pin as GPIO in

    try:
      while True:
        for i in range(len(Trig)):
          GPIO.output(Trig[i], False)                 #Set TRIG as LOW
          print "Waitng For Sensor To Settle"
          time.sleep(2)                            #Delay of 2 seconds

          GPIO.output(Trig[i], True)                  #Set TRIG as HIGH
          time.sleep(0.00001)                      #Delay of 0.00001 seconds
          GPIO.output(Trig[i], False)                 #Set TRIG as LOW

          while GPIO.input(Echo[i])==0:               #Check whether the ECHO is LOW
            pulse_start = time.time()              #Saves the last known time of LOW pulse

          while GPIO.input(Echo[i])==1:               #Check whether the ECHO is HIGH
            pulse_end = time.time()                #Saves the last known time of HIGH pulse

          pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
          distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
          distance = round(distance, 2)            #Round to two decimal points

          if distance > 2 and distance < 100:      #Check whether the distance is within range
            print "Sensor:",i," Distance:",distance - 0.5,"cm have car"  #Print
            #distance with 0.5 cm calibration
            Output[i] = True
          else:
            print "Sensor:",i,"Don't have car"                   #display out of
            #range
            Output[i] = False

    except KeyboardInterrupt:
      GPIO.cleanup()  
