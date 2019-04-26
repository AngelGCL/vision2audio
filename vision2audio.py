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

m = Image.open("abcdefga.png")
rgb_im = m.convert('RGB')

w, h = m.size
print(w)
print(h)

result = list()


track = 0  # Track (default 0)
channel = 0  # Channel (default 0)
time = 0  # In beats
# duration = h  # In beats
tempo = 110  # In BPM
volume = 100

output = MIDIFile(1)
output.addTempo(track, time, tempo)

for col in range(w):
    for row in range(h):
        r, g, b = rgb_im.getpixel((col, row))
        print('[%i,%i]:' % (row, col), (r, g, b))

        repeatCount = 0
        # check if next pixel is repeated
        midi = note_midi_conversion[(r, g, b)]
        duration = 1/2

        output.addNote(track, channel, midi, time, duration, volume)

        time += duration
        print(time)

        print(midi)

with open("newTest.mid", "wb") as output_file:
    output.writeFile(output_file)



#
# degrees = suparr  # MIDI note number
# track = 0  # Track (default 0)
# channel = 0  # Channel (default 0)
# time = 0  # In beats
# duration = 1  # In beats
# tempo = 120  # In BPM
# volume = 100  # 0-127, as per the MIDI standard
#
# output = MIDIFile(1)
# output.addTempo(track, time, tempo)
#
# for e in degrees:
#     output.addNote(track, channel, e[0], time, e[1], volume)
#     print('added note:', e[0])
#     time += e[1]
#
# with open("test.mid", "wb") as output_file:
#     output.writeFile(output_file)
