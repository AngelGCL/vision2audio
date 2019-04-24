from wavebender import *

def violin(amplitude=0.1):
    # simulates a violin playing G.
    # return (damped_wave(400.0, amplitude=0.76*amplitude, length=44100 * 5),
    #         damped_wave(800.0, amplitude=0.44*amplitude, length=44100 * 5),
    #         damped_wave(1200.0, amplitude=0.32*amplitude, length=44100 * 5),
    #         damped_wave(3400.0, amplitude=0.16*amplitude, length=44100 * 5),
    #         damped_wave(600.0, amplitude=1.0*amplitude, length=44100 * 5),
    #         damped_wave(1000.0, amplitude=0.44*amplitude, length=44100 * 5),
    #         damped_wave(1600.0, amplitude=0.32*amplitude, length=44100 * 5))

    return (damped_wave(391.995, amplitude=0.76 * amplitude, length=44100 * 5),
            damped_wave(783.991, amplitude=0.44 * amplitude, length=44100 * 5),
            damped_wave(1567.982, amplitude=0.32 * amplitude, length=44100 * 5),
            damped_wave(18.354, amplitude=0.16 * amplitude, length=44100 * 5),
            damped_wave(20.601, amplitude=1.0 * amplitude, length=44100 * 5),
            damped_wave(21.827, amplitude=0.44 * amplitude, length=44100 * 5),
            damped_wave(24.499, amplitude=0.32 * amplitude, length=44100 * 5),)

channels = (violin(),)
samples = compute_samples(channels, 44100 * 60 * 1)
write_wavefile('test1.wav', samples, 44100 * 60 * 1, nchannels=1)