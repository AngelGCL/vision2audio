from PIL import Image
from midiutil import MIDIFile
from statistics import median


m = Image.open("./scaler/logo.png")
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

            print('the note is %i' % note)

            if note > 108:
                note = 108

            duration = 1

            output.addNote(track, channel, note, time, duration, volume)
            time += duration

            # reset everything
            iter=0
            arrB = []
            arrG = []
            arrR = []

with open("test.mid", "wb") as output_file:
    output.writeFile(output_file)
