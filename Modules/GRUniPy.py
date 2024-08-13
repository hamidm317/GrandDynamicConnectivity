import numpy as np
from scipy import signal

from Utils import Constants
from Utils import SpectralDeco as SD

def PowerPhaseExt(x: np.ndarray):

    x_a = signal.hilbert(x, axis = -1)

    return np.abs(x_a), np.angle(x_a)

def FrequencyBandExt(Data: np.ndarray, Band = 'All'): # add kwargs and method

    assert Data.ndim < 4 and Data.ndim > 0, "The data must have a time dim at least and 3 dimensions (Trial, Channel, Time) at most"
    assert type(Band) == str or type(Band) == list, "Insert true Band name"

    if type(Band) == str:

        if Band == 'All':

            Band = [Band_i for Band_i in Constants.SpectralConstants.BandsBounds.keys()][:-1]

        else:

            Band = [Band]

    Band_Data = []

    for Band_i in Band:

        assert Band_i in Constants.SpectralConstants.BandsBounds.keys(), "Band Name is Not Available!"

        output = SD.WavletSpectralDecomposer(Data, Band = Band_i)

        Band_Data.append(np.mean(output[0], axis = -2))

    return Band_Data