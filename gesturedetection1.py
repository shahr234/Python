import time


def loop():
    while(True):
        distance = device.getSonar() # get distance
        print ("The distance is : %.2f cm"%(distance))
        time.sleep(0.1)

usingRaspberryPi = False # change to true if running on actual Pi
        
if __name__ == '__main__':     # Program entrance
    if usingRaspberryPi:
        import UltrasonicRangerInterface as device
    else:
        import SonarSim as device
    print ('Program is starting...')
    device.setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        device.cleanup()
        print ('Bye...')
