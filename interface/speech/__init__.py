#!/Users/evamy/bot/bin/python
# ################################################################################################
# 
#         @author: Antriksh Agarwal
# 
# ################################################################################################

import speech_recognition as sr
import pyaudio
import wave
import sys


# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
# Sample rate is how often values are recorded
sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()
# print(mic_list)
# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.

