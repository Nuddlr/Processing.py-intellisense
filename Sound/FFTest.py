if False:
    from lib.Processing3 import *
add_library('sound')

fft = FFT
song = SoundFile
bands = 128
spectrum = [i for i in range(bands)]

def setup():
    size(512, 360)
    background(255)
    
    song = SoundFile(this, "Loop.wav")
    song.loop()

    fft = FFT(this, bands)
    fft.input(song)


def draw():
    background(255)
    fft.analyze(spectrum)

    for i in range(bands):
        line(i, height, i, height - spectrum[i]*height*5)