#!/usr/bin/python3

# open a microphone in pyAudio and listen for taps
import time
import glob,os
import pyaudio
import struct
import math
import random
from datetime import datetime as dt
print("Hello")
a=list()
f=open("example.txt","a+")
for file in glob.glob("*.mp3"):
    a.append(file)
INITIAL_TAP_THRESHOLD = 0.150
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 1
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
di=2

def get_rms( block ):

    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768. 
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        
    def stop(self):
        self.stream.close()

#    def find_input_device(self):
#        device_index = 2            
#        return device_index

    def open_mic_stream( self ):
        device_index = di

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def tapDetected(self):
        print("Dog Bark Detected!")
        d=random.randint(0,len(a))
        f.write(dt.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"+"\n"))
        b='mpg321 '+ "'" + a[d] +"'"
        os.system(b)
	

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError as e:
            # dammit. 
            print( " Error recording" )
            return

        amplitude = get_rms( block )
        if amplitude > self.tap_threshold:
         self.tapDetected()


if __name__ == "__main__":
    tt = TapTester()

    while true:
        tt.listen()
f.close()	
