from PIL import Image
from midiutil import MIDIFile

music_color_scale = {
    'A': (0, 255, 255),
    'B': (255, 0, 0),
    'C': (0, 0, 255),
    'D': (0, 255, 0),
    'E': (127, 0, 255),
    'F': (255, 128, 0),
    'G': (255, 0, 255),
    'SPACE': (128, 128, 128)
}

note_midi_conversion = {
    (0, 255, 255): 57,
    (255, 0, 0): 59,
    (0, 0, 255): 48,
    (0, 255, 0): 50,
    (127, 0, 255): 52,
    (255, 128, 0): 53,
    (255, 0, 255): 55,
    'SPACE': -1
}

note_duration_conversion = {
    (0, 255, 255): [57, 1/2],
    (255, 0, 0): [59, 1/2],
    (0, 0, 255): [48, 1/2],
    (0, 255, 0): [50, 1/2],
    (127, 0, 255): [52, 1/2],
    (255, 128, 0): [53, 1/2],
    (255, 0, 255): [55, 1/2],
    (0, 204, 204): [57, 1/4],
    (204, 0, 0): [59, 1/4],
    (0, 0, 204): [48, 1/4],
    (0, 204, 0): [50, 1/4],
    (102, 0, 204): [52, 1/4],
    (204, 102, 0): [53, 1/4],
    (204, 0, 204): [55, 1/4],
    (0, 153, 153): [57, 1/8],
    (153, 0, 0): [59, 1/8],
    (0, 0, 153): [48, 1/8],
    (0, 153, 0): [50, 1/8],
    (76, 0, 153): [52, 1/8],
    (153, 76, 0): [53, 1/8],
    (153, 0, 153): [55, 1/8],
    (0, 102, 102): [57, 1/16],
    (102, 0, 0): [59, 1/16],
    (0, 0, 102): [48, 1/16],
    (0, 102, 0): [50, 1/16],
    (51, 0, 102): [52, 1/16],
    (102, 51, 0): [53, 1/16],
    (102, 0, 102): [55, 1/16],

    (172, 172, 172): [-1, 1/8],
    'SPACE': -1
}


m = Image.open("eb.png")
rgb_im = m.convert('RGB')

w, h = m.size
print(w)
print(h)

result = list()


track = 0  # Track (default 0)
channel = 0  # Channel (default 0)
time = 0  # In beats
tempo = 90  # In BPM
volume = 100

output = MIDIFile(1)
output.addTempo(track, time, tempo)

for row in range(h):
    for col in range(w):
        r, g, b = rgb_im.getpixel((col, row))
        print('[%i,%i]:' % (row, col), (r, g, b))

        note, duration = note_duration_conversion.get((r, g, b), [0, 0])

        if note != -1:
            print(note, ':', duration)
            output.addNote(track, channel, note, time, duration+(1/4), volume)

        time += duration+(1/4)

with open("newTest5.mid", "wb") as output_file:
    output.writeFile(output_file)
