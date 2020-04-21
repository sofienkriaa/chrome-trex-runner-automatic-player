from pynput.keyboard import Key, Controller
import time
import serial

keyboard = Controller()

ser = serial.Serial('COM5', 9600, timeout=0,parity=serial.PARITY_EVEN, rtscts=1)

while True:
    s = ser.read(1)
    print(s)
    if s == b'c':
        keyboard.press(Key.space);
        keyboard.press(Key.space);
        keyboard.release(Key.space);