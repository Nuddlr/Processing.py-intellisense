if False:
    from lib.Processing3 import *

add_library('minim')

minim = Minim
player = AudioPlayer
inPut = AudioInput

def setup():
    size(100, 100)

    minim = Minim(this)
    player = minim.loadFile('Revolve.m4a')
    inPut = minim.getLineIn()

def draw():
    pass