# Date (18/1/26)

import winsound

import math
import time
import sys

width = 0
height = 0
length = 0
time_delay = 0.1

# Function For Loading

def memuat(teks="Loading", pengulangan=5, delay1=0.2, delay2=0.2):
    for a in teks:
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(delay1)
    for b in range(pengulangan):
        for load1 in ["      ", " .    ",  " . .  ", " . . ."]:
            sys.stdout.write(f"\r{teks}{load1}")
            sys.stdout.flush()
            time.sleep(delay2)
        sys.stdout.write(f"\r{teks} . . .")  
        for load2 in [" . .  ", " .    ", "      "]:
            sys.stdout.write(f"\r{teks}{load2}")
            sys.stdout.flush()
            time.sleep(delay2)
        for load3 in ["      ", " =    ",  " = =  ", " = = ="]:
            sys.stdout.write(f"\r{teks}{load3}")
            sys.stdout.flush()
            time.sleep(delay2)
        
        for load4 in [" = =  ", " =    ", "      "]:
            sys.stdout.write(f"\r{teks}{load4}")
            sys.stdout.flush()
            time.sleep(delay2)
    sys.stdout.write(f"\r{teks}\r")
    sys.stdout.write("\r") 

# Function For Writing animation
def tensess(text, time_delay=0.1, tenses_pause=1.8):
    alpha = len(text)
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay)
    time.sleep(tenses_pause)
    sys.stdout.write(f"\r" + " " * alpha)
    sys.stdout.write("\r")


tensess("temanku semua pada jahat tante", 0.1)
tensess("Alvin bau")

sys.exit()













