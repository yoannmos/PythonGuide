from scipy.signal import butter, lfilter, freqz


def butter_lowpass_filter(Serie, cutoff, fs):
    order = 6     # Filter order
    # fs = Freq sample rate, [Hz]
    # cutoff = Cutoff frequency  [Hz]
    
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    Serie = lfilter(b, a, Serie)
    return Serie
