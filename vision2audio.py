from PIL import Image
from midiutil import MIDIFile
from statistics import median


m = Image.open("./scaler/turtle.jpg")
rgb_im = m.convert('RGB')

w, h = m.size
print(w)
print(h)


track = 0  # Track (default 0)
channel = 0  # Channel (default 0)
time = 0  # In beats
tempo = 90  # In BPM
volume = 100
duration = 1

output_arr = list()

output = MIDIFile(1)
output.addTempo(track, time, tempo)

chunk = (h*w)*0.1
print('chunk is size %i' % chunk)
arrR = []
arrB = []
arrG = []
iter = 0

for row in range(h):
    for col in range(w):
        r, g, b = rgb_im.getpixel((col, row))
        arrG.append(g)
        arrR.append(r)
        arrB.append(b)
        iter = iter + 1

        if iter >= chunk:
            # create a note here
            note = (median(arrR) % 21 + median(arrG) % 21 + median(arrB) % 21) + 36
            note = int(note)

            if note > 108:
                note = 108

            output_arr.append(note)

            # reset everything
            iter = 0
            arrB = []
            arrG = []
            arrR = []

BASE = {
    'C': 24,
    'D': 26,
    'E': 28,
    'F': 29,
    'G': 31,
    'A': 33,
    'B': 35
};

SCALES = {
    'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
    'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
    'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
}

KEYS = {}
for octave in range(-2, 8):
    for k in BASE:
        key = BASE[k] + (octave * 12)
        KEYS[str(k) + 'b' + str(octave)] = key - 1
        KEYS[str(k) + str(octave)] = key
        KEYS[str(k) + '#' + str(octave)] = key + 1

print('original:', output_arr)

corrected_output = list()

for i, val in enumerate(output_arr):
    for kv in KEYS:
        if val == KEYS[kv]:
            if '#' in kv:
                splitted = kv.split('#')

                if splitted[0] == 'G':
                    nextChord = 'A'
                    octave = str(int(splitted[1]) + 1)
                else:
                    nextChord = chr(ord(splitted[0]) + 1)
                    octave = splitted[1]

                corrected = ''.join([nextChord, octave])

                corrected_output.append(KEYS.get(corrected))
            elif 'b' in kv:
                splitted = kv.split('b')

                if splitted[0] == 'C':
                    nextChord = 'B'
                    octave = str(int(splitted[1]) - 1)
                else:
                    nextChord = chr(ord(splitted[0]) - 1)
                    octave = splitted[1]

                corrected = ''.join([nextChord, octave])

                corrected_output.append(KEYS.get(corrected))

            else:
                corrected_output.append(val)

            break

print('corrected:', corrected_output)

for note in corrected_output:
    output.addNote(track, channel, note, time, duration, volume)
    time += duration

with open("test.mid", "wb") as output_file:
    output.writeFile(output_file)
