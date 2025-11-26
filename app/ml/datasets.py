import numpy as np

def synthetic_waveform(length=256, amp=1.0):
    x = np.linspace(0, 2*np.pi, length)
    y = amp * np.sin(x)
    return x, y
