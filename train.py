import os
#import librosa
import ffmpy
import time
import subprocess
import numpy as np
import pandas as pd
import wave
import contextlib
#import pyaudio
import xlsxwriter
import math

from shutil import rmtree
from pytube import YouTube

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [20, 10]

pathSrc = 'src/'


def transformMpegToWav(filename):
    os.system(str('ffmpeg -i {}.mpeg {}.wav').format(filename, filename))


def segmentFile(samples, fileName):
    '''
    Funcion que segmenta los audios de acuerdo a la cantidad de frames y los
    guarda de acuerdo a la siguiente etiqueta:
    - ##_###_{segmento}.wav
    '''
    duration = 0
    #transformMpegToWav(pathSrc + fileName)
    origen = pathSrc + fileName + '.wav'

    with contextlib.closing(wave.open(origen, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
    for i in range(0, samples):
        destino = pathSrc + fileName + '/' + fileName + \
            '_' + '{0}'.format(str(i + 1).zfill(3))
        print(destino)
        str_inci = time.strftime(
            '%H:%M:%S', time.gmtime(int(i * (duration/samples))))
        str_duracion = time.strftime(
            '%H:%M:%S', time.gmtime(int(duration/samples)))

        os.system(str('ffmpeg -ss {} -t {} -i {} -acodec pcm_s16le -ar 44000 {}.wav').format(
            str_inci, str_duracion, origen, destino))


segmentFile(720, 'rpp_01')
