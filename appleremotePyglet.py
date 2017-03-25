#!/usr/bin/env python
from pynput.keyboard import Key, Controller
import sys
import pyglet

# The keyboard controller
keyboard1 = Controller()

# The AppleRemote controller
window = pyglet.window.Window(visible=False)
remote = pyglet.input.get_apple_remote()
if not remote:
    print('Apple IR Remote not available.')
    sys.exit(0)
# To avoid the volume/itunes buttons
remote.open(window, exclusive=True)


# All the events:
@remote.select_control.event
def on_press():
    print('Press select')

@remote.menu_control.event
def on_press():
    print('Finishing the app')
    sys.exit(0)

@remote.up_control.event
def on_press():
    print('Press up')
    keyboard1.press(Key.up)

@remote.down_control.event
def on_press():
    print('Press down')
    keyboard1.press(Key.down)

@remote.left_control.event
def on_press():
    print('Press left')
    keyboard1.press(Key.left)

@remote.right_control.event
def on_press():
    print('Press right')
    keyboard1.press(Key.right)



@remote.select_control.event
def on_release():
    print('Release select')

@remote.menu_control.event
def on_release():
    print('Release menu')

@remote.up_control.event
def on_release():
    print('Release up')
    keyboard1.release(Key.up)

@remote.down_control.event
def on_release():
    print('Release down')
    keyboard1.release(Key.down)

@remote.left_control.event
def on_release():
    print('Release left')
    keyboard1.release(Key.left)

@remote.right_control.event
def on_release():
    print('Release right')
    keyboard1.release(Key.right)



print('Listening Apple Remote Control IR ...')
print('Press MENU to exit.')

pyglet.app.run()
