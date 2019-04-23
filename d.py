import numpy as np
from matplotlib import pyplot as plt
F1=np.asarray(input("enter msg frequency for signal1 from 10 to 300"),'float32')
F2=np.asarray(input("enter carrier frequency for signal2 from 10 to 300"),'float32')
Fs=np.asarray(700,'float32')
n=np.asarray(range(0,500),'float32')
m1=3*np.sin(2*np.pi*(F1/Fs)*n)
c1=np.sin(2*np.pi*(F2/Fs)*n)
plt.subplot(311)
plt.plot(m1)
plt.subplot(312)	
plt.plot(c1)
plt.subplot(311)#'''to plot original signal'''#
plt.plot(m1)
plt.show()


