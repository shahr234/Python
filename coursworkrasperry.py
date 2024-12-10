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

def loop():
    low_threshold = 15  # threshold for LowPass and LowHold
    high_threshold = 25  # threshold for HighPass and HighHold
    low_hold_counter = 0  # counter for LowHold
    high_hold_counter = 0  # counter for HighHold
    pull_up_counter = 0  # counter for PullUp
    push_down_counter = 0  # counter for PushDown
    movements = deque([], maxlen=10)  # deque to store movements, max length of 10

commands = {
    ('LowPass', 'LowPass'): 'Skip forward',
    ('HighPass', 'HighPass'): 'Skip backward',
    ('LowPass', 'LowHold'): 'Power off',
    ('HighPass', 'HighHold'): 'Reset',
    ('PullUp', 'HighPass', 'LowHold'): 'ActivateAutoMode',
    ('PushDown', 'LowPass', 'HighHold'): 'DisableAutoMode'
}


if len(movements) == movements.maxlen:
    command = commands.get(tuple(movements), 'Unknown sequence')
    print(f'{list(movements)}: {command}')
    movements.clear()
while True:
    distance = device.getSonar() # get distance

    if distance <= low_threshold:
        low_hold_counter += 1
        high_hold_counter = 0  # reset HighHold counter
        pull_up_counter = 0  # reset PullUp counter
        push_down_counter = 0  # reset PushDown counter

        if low_hold_counter >= 10:  # low hold for 1 second
            movements.append('LowHold')
            low_hold_counter = 0  # reset LowHold counter

    elif distance >= high_threshold:
        high_hold_counter += 1
        low_hold_counter = 0  # reset LowHold counter
        pull_up_counter = 0  # reset PullUp counter
        push_down_counter = 0  # reset PushDown counter

        if high_hold_counter >= 10:  # high hold for 1 second
            movements.append('HighHold')
            high_hold_counter = 0  # reset HighHold counter

    else:
        low_hold_counter = 0  # reset LowHold counter
        high_hold_counter = 0  # reset HighHold counter

        if distance > low_threshold and pull_up_counter > 0:  # PullUp
            movements.append('PullUp')
            pull_up_counter = 0  # reset PullUp counter

        elif distance < high_threshold and push_down_counter > 0:  # PushDown
            movements.append('PushDown')
            push_down_counter = 0  # reset PushDown counter

        else:
            if distance > low_threshold:  # LowPass
                pull_up_counter += 1

            elif distance < high_threshold:  # HighPass
                push_down_counter += 1

    if len(movements) == movements.maxlen:  # check if deque is full
        command = commands.get(tuple(movements), 'Unknown sequence')
        print(f'{list(movements)}: {command}')
        movements.clear()  # clear deque

    print("The distance is : %.2f cm" % (distance))
    time.sleep(0.1)
