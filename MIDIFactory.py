# using matplotlib
import matplotlib.image as img

# using statistics to import median
# for median calculation
from statistics import median, mean

import math

# import midiutil to generate midi tracks
from midiutil import MIDIFile


class MIDIFactory:
    def __init__(self, target_image_path):
        self.target = target_image_path

    def im_processor(self):
        return

    def midi_from_array(self, note_array):
        degrees = note_array                        # MIDI note number
        track = 0                                   # Track (default 0)
        channel = 0                                 # Channel (default 0)
        time = 0                                    # In beats
        duration = 1                                # In beats
        tempo = 120                                 # In BPM
        volume = 100                                # 0-127, as per the MIDI standard

        output = MIDIFile(1)
        output.addTempo(track, time, tempo)

        for e in note_array:
            output.addNote(track, channel, e[0], e[1], e[2], volume)

        with open("test.mid", "wb") as output_file:
            output.writeFile(output_file)
