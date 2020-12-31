import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
import numpy as np
import pyrec
def captrue(filepath, seconds=5): 
    pyrec.rec(filepath)
    wav2pcm(filepath)


def playback(filepath):
    data, fs = sf.read(filepath, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()

def wav2pcm(wavfile, data_type=np.int16):
    pcmfile = "%s.pcm" %(wavfile.split(".")[0])
    f = open(wavfile, 'rb')
    f.seek(0)
    f.read(44)
    data = np.fromfile(f, dtype= data_type)
    data.tofile(pcmfile)

if __name__ == '__main__':
	captrue()


