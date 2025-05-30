import board
import digitalio
from kmk import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Layer
from kmk.modules.macros import Press, Tap, Release

macros = Macros()
keyboard.modules.append(macros)

keyboard = KMKKeyboard()


switch1 = digitalio.DigitalInOut(board.D11)
switch1.switch_to_input(pull=digitalio.Pull.UP)

switch2 = digitalio.DigitalInOut(board.D10)
switch2.switch_to_input(pull=digitalio.Pull.UP)

switch3 = digitalio.DigitalInOut(board.D9)
switch3.switch_to_input(pull=digitalio.Pull.UP)

switch4 = digitalio.DigitalInOut(board.D8)
switch4.switch_to_input(pull=digitalio.Pull.UP)

switch5 = digitalio.DigitalInOut(board.D4)
switch5.switch_to_input(pull=digitalio.Pull.UP)

switch6 = digitalio.DigitalInOut(board.D5)
switch6.switch_to_input(pull=digitalio.Pull.UP)

switch7 = digitalio.DigitalInOut(board.D6)
switch7.switch_to_input(pull=digitalio.Pull.UP)

switch8 = digitalio.DigitalInOut(board.D7)
switch8.switch_to_input(pull=digitalio.Pull.UP)


keyboard.pins = {
    board.D11: KC.MACRO(Tap(KC.G), Tap(KC.1)), 
    board.D10: KC.MACRO(Tap(KC.G), Tap(KC.2)),
    board.D9: KC.MACRO(Tap(KC.G), Tap(KC.3)),
    board.D8: KC.MACRO(Tap(KC.G), Tap(KC.4)),
    board.D4: KC.F,
    board.D5: KC.MACRO(Tap(KC.a), Tap(KC.N0)),
    board.D6: KC.MACRO(Tap(KC.a), Tap(KC.50)),
    board.D7: KC.MACRO(Press(KC.LALT), Tap(KC.E), Release(KC.LALT)),
}


if __name__ == "__main__":
    while True:
        keyboard.poll()
