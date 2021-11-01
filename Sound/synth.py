if False:
    from lib.Processing3 import *
    from lib.libraries.sound import *
add_library('sound')

sine = SinOsc(this)



def setup():
    size(900, 900)
    background(255)

    # Create the sine oscillator
    sine = SinOsc(this)
    sine.play(1000, 1)

def draw():
    pass
