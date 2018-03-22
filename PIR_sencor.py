import RPi.GPIO as GPIO
import time

def setup(GPIOnum):
  GPIO.setmode(GPIO.board)
  GPIO.setup(GPIOnum, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
def motion(GPIOnum):
    global counter

    if GPIO.input)=(GPIOnum):
        counter += 1
        print("Motion detected {0}".format(counter))

    else:
        print("Motion not detected")

try:
    setup(14)
    GPIO.add_event_detect(14, GPIO.BOTH, callback=motion, bouncetime=200)
    while True:
        time.sleep(5)
except:
    GPIO.cleaup()
