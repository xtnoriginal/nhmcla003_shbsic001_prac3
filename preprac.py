#importing GPIO for input and time for delay
import RPi.GPIO as GPIO
from time import sleep


#set the type of pin numbering system to be used
GPIO.setmode(GPIO.BOARD)

#switch off all  warnings 
GPIO.setwarnings(False)


def main():
	GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	try:
		state=0;
		while True:
			
			if GPIO.input(37):
		
				if state==0:
					GPIO.output(8,GPIO.HIGH)
					state=1
				else:
					GPIO.output(8,GPIO.LOW)
					state=0
			
			
	except KeyboardInterrupt:
        	GPIO.cleanup()	


if __name__=="__main__":
	main()
