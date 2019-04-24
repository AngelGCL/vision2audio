# Main vision2audio Script
# Developed by Angel & Hector
from MIDIFactory import *

# get from arguments
targetImage = 'image.png'
#
# imageProcessor = ImageProcessor(targetImage)
midiFactory = MIDIFactory(targetImage)

try:
    midiFactory.image2midi()
    print ('Done, new MIDI file saved successfully!')
except Exception:
    print('FATAL: Script got error while parsing image. Try again!')
