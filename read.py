import evdev
import time

from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event3')

print(gamepad)

bad_codes = [0, 3, 4, 16, 17, 318, 317, 304, 305, 307, 308, 314, 315, 310, 311]

for event in gamepad.read_loop():

    if event.code not in bad_codes:
        print(event)
   
    #if event.code == 4:
    #    print(event)
    #elif event.code == 3:
    #    print(event)
        
    #if event.type == ecodes.EV_KEY:
    #    print(event)
    #else:
    #    print("\t", event)
    # time.sleep(.2)
    # print(categorize(event))
