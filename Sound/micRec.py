if False:
    from lib.Processing3 import *
add_library('sound')

# GLOBALS #
song = SoundFile
fft = FFT(this)

# FFT bands number
bands = int(128)

# Smoothing factor
smoothFactor = float(0.2)

# Create a vector to store smoothed spectrum data
spectrum = [i+1 for i in range(bands)]
print(spectrum)

# VARIABLES FOR DRAWING SPECTRUM #
# Declare a scaling factor for adjusting the heigth of the rectangles
scale = int(5)
# Declare a drawing variable for calculating the width of the rectangles
barWidth = float(0.0)


def setup():
    size(500, 500)
    background(255)

    #############
    # AUDIO SETUP 
    def audioSetup():
        # Start listening to microphone
        # Create Audio input and grab the 1st channel
        inn = AudioIn(this, 0)

        # Start the Audio Input
        inn.start()

        # Create a new Amplotude analyzer
        global rms
        rms = Amplitude(this)

        # Patch the input to a volume analyzer
        rms.input(inn)
    audioSetup()

    ################
    # ANALYZER SETUP
    # Calculate the width of the rects depending 
    # on how many bands we have
    barWidth = width/float(bands)

    # Load and play a soundfile and loop it
    song = SoundFile(this, "Loop.wav")
    song.loop()

    # Create the FFT analyzer and connect the playing soundfile to it
    fft = FFT(this, bands)
    fft.input(song)



def draw():
    def soundEllipse():
        background(255)

        # Get the overall volume (0 - 1.0)
        vol = rms.analyze()
        fill(127)
        stroke(0)

        # Draw an ellipse with size based on volume
        eW = (vol*1000)**1.5
        eH = (vol*1000)**1.5
        print(eW, eH)
        ellipse(width/2, height/2, 50+eW, 50+eH)

    background(125, 255, 125)
    fill(255, 0, 150)
    noStroke()
    # Perform the analysis
    fft.analyze(spectrum)

    for i in range(bands):
        # Smooth the FFT scpectrum data by smoothing factor
        spectrum[i] += (fft.spectrum[i] - spectrum[i]) * smoothFactor

        # Draw the rectangles, adjust their height using the scale factor
        rect(i*barWidth, height, barWidth, -spectrum[i]*height*scale)