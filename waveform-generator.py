import numpy as np
import matplotlib.pyplot as plt

# generate trombone-like sound given base formant frequency
base_frequency = 150  # Hz
sound_length = 0.5    # seconds
ramp_time = 0.05      # seconds (ramp 50 ms)
new_fs = 44.1e3       # sampling rate in Hz
formant_amplitude = np.array([
    0.00338228234061383,
    0.00226922129759024,
    0.00871263427834780,
    0.00793701307097099,
    0.00884670768767992,
    0.0141776629957550,
    0.0130699547346117,
    0.00532919247754215,
    0.00281525320614360,
    0.00275592890049937,
    0.00259025915149248,
    0.00195870812579687,
    0.00108603438964854,
    0.00109042043074750,
    0.00112494823472505
])

n_formants = len(formant_amplitude)
formant_frequency = base_frequency * np.arange(1, n_formants + 1)

# generate sin wave of sound_length seconds at base frequency
timepoints = np.arange(1/new_fs, sound_length + 1/new_fs, 1/new_fs)
all_freq = formant_amplitude[:, np.newaxis] * np.sin(formant_frequency[:, np.newaxis] * timepoints * 2 * np.pi)

stimulus = np.sum(all_freq, axis=0)
ramp = np.ones(len(stimulus))
ramp[:int(ramp_time * new_fs)] = np.linspace(0, 1, int(ramp_time * new_fs))
ramp[-int(ramp_time * new_fs):] = np.linspace(1, 0, int(ramp_time * new_fs))
stimulus *= ramp

plt.plot(timepoints, stimulus)
plt.show()

