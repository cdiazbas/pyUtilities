#!/usr/bin/env python
from iremote import IRemote, listener
from pynput.keyboard import Key, Controller

keyboard1 = Controller()

def mylistener(event):
    print(event)
    if event == "0x18 depressed":
        print('NEXT',event)
        # Press and release
        keyboard1.press(Key.right)
        keyboard1.release(Key.right)
    
    if event == "0x19 depressed":
        print('PREV',event)
        # Press and release
        keyboard1.press(Key.left)
        keyboard1.release(Key.left)
    
    if event == "0x1f depressed":
        print('UP',event)
        # Press and release
        keyboard1.press(Key.up)
        keyboard1.release(Key.up)

    if event == "0x20 depressed":
        print('DOWN',event)
        # Press and release
        keyboard1.press(Key.down)
        keyboard1.release(Key.down)


print('Listening Apple Remote Control IR ...')
print('Ctrl+C to exit.')
iremote = IRemote()
iremote.add_listener(mylistener)
iremote.start()