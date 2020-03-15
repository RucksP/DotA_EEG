# Rohan Patel
# EEG_to_DotA.py
# This file will take EEG recordings from a Mindwave Mobile EEG
# and parse them to send inputs to the video game DotA 2
# This implementation will activate show indicators button
# in DotA 2

import time
import pylsl
import sys
import keyboard

print('beginning readings')

#GLOBAL_VARS
stop_key = 'j' #press j to kill the code
attention_threshold = 65
attention_confirm_threshold = 3  #tried 3,4,5... 3 is the best because too hard to turn on
#attentions = [] this is there to debug when the attention values are low

attention_confirmation = 0
# read the neurosky recordings via python through OpenVibe EEG Software
streams = pylsl.resolve_stream('type','signal')


# continuously read from the EEG
while True:
    
    # this snippet gets the readings from the neurosky at the
    # current time
    inlet = pylsl.stream_inlet(streams[0])
    sample, timestamp = inlet.pull_sample()
    attention = sample[1]
    #print(attention)
    #attentions.append(attention)
    
    # high attention values lead to 
    if(attention > attention_threshold):
        attention_confirmation += 1
    else:
        attention_confirmation = 0
        keyboard.release('u')
    
    # if the arrention has been high for long enough, then press the button
    if(attention_confirmation >= attention_confirm_threshold):
        #print('pressed')
        keyboard.press('u')
        time.sleep(1)
        
    if(keyboard.is_pressed(stop_key)):
        print("ending process")
        sys.exit()
        break