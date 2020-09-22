#  SHBSIC001 and NHMCLA003
#  Turning on a LED ON and OFF
#  EEE2095S

#importing GPIO for input and time for delay
import RPi.GPIO as GPIO
from time import sleep


#set the type of pin numbering system to be used
GPIO.setmode(GPIO.BOARD)

#switch off all  warnings 
GPIO.setwarnings(False)

#state variable to indicate the current sate of the LED


def my_callback(channel):
	#check current state of the LED
	if GPIO.input(8)==GPIO.LOW:
		#Turn on the LED
		GPIO.output(8,GPIO.HIGH)
		state=1
	
	else:
		#Switch off the LED
		GPIO.output(8,GPIO.LOW)
		state=0

def main():
	#Setup the OUTPUT pin for the Led and set default to low
	GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)

	#SETUP input pin  and  use a PULL DOWN resitor as  we want to set the default input to 0
	GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

	#Detect when the user presses a button and  avoid switch debouncing
	GPIO.add_event_detect(37, GPIO.RISING, callback=my_callback, bouncetime=200)
	try:
		#loop  indefinetly until the user cancels the program
		while True:
			sleep(1)
			
			
	except KeyboardInterrupt:
		#cleanup all pins used
        	GPIO.cleanup()	


if __name__=="__main__":
	main()
