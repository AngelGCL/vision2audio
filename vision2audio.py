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
chunk = h*w*0.10
chunk_arr = []
iter = 0
for row in range(h):
    for col in range(w):
        r, g, b = rgb_im.getpixel((col, row))
        chunk_arr.append([r, g, b])
        iter+=1

        if iter == chunk:
        #create a note here
            mediana= median(chunk_arr)
            chunk_arr = []
            note = (mediana[0]%21 + mediana[1]%21 + mediana[3]%21) + 70
            if note > 108:
                note = 108
            duration = 1/4
            output.addNote(track, channel, note, time, duration+(1/4), volume)
            time += duration + (1 / 4)

with open("badbunny.mid", "wb") as output_file:
    output.writeFile(output_file)
