###
 # John Park
 # data.py
 # 02-28-2017
 ##


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

input_pins = [25]
output_pins = []

# setup the input pins
GPIO.setup(input_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(output_pins, GPIO.OUT, initial=GPIO.LOW)


def main():
    read_25 = GPIO.input(25)
    
    print(read_25)

    GPIO.cleanup()
###




#############################
if __name__ == "__main__":  #
    main()                  #
#############################
