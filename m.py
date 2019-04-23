import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('man.wav')
print(data.shape)
plt.plot(data);
plt.show()
wav.write('high_voice.wav',0.5*fs,data)


