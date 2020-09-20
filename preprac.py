#importing GPIO for input and time for delay
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def main():
	GPIO.setup(8,GPIO.OUT,initial=GPIO.HIGH)
	GPIO.output(8,GPIO.HIGH)
	sleep(1)
        GPIO.cleanup()	


if __name__=="__main__":
	main()
