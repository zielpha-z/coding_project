# Dtae (18/1/26)

import winsound
import math
import time
import sys

def memuat(teks="Loading", pengulangan=2, delay1=0.2, delay2=0.2):
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
    sys.stdout.write("\r" + " " * (len(teks) + 1))
    sys.stdout.flush()
    sys.stdout.write("\r")


def loading(teks="Loading", durasi=5):
    for _ in range(durasi):
        for titik in ["", ".", "..", "..."]:
            sys.stdout.write(f"\r{teks}{titik} ")
            sys.stdout.flush()
            time.sleep(0.5)

    sys.stdout.write(f"\r{teks}  \r")  



def loadingg(teks="Loading", durasi=5):
    for i in range(durasi):
        for titik in ["   ", ".  ", ".. ", "..."]:
            sys.stdout.write(f"\r{teks}{titik}")
            sys.stdout.flush()
            time.sleep(0.5)
        for titik2 in [".. ", ".  ", "   "]:
            sys.stdout.write(f"\r{teks}{titik2}")
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write(f"\r{teks}  \r")  




def loadinggg(teks="Loading", durasi=5):
    for _ in range(durasi):
        for titik in ["", ".", "..", "..."]:
            sys.stdout.write(f"\r{teks}{titik}")
            sys.stdout.flush()
            time.sleep(0.5)
        for titik2 in ["", ".", "..", "..."]:
            sys.stdout.write(f"\r{teks}{titik2}")
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write(f"\r{teks}  \r")  


def spin():
    spinner = ['|', '/', '-', '\\']
    for i in range(50):
        sys.stdout.write('\r' + spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.2)

def wavi(teks):

    wave = ['  ▂ ▃ ▅ ▇ █ ▇ ▅ ▃ ▂  ', '▂ ▃ ▅ ▇ █ ▇ █ ▇ ▅ ▃ ▂', '▃ ▅ ▇ █ ▇ ▅ ▇ █ ▇ ▅ ▃', '▅ ▇ █ ▇ ▅ ▃ ▅ ▇ █ ▇ ▅', "▇ █ ▇ ▅ ▃ ▂ ▃ ▅ ▇ █ ▇", "█ ▇ ▅ ▃ ▂   ▂ ▃ ▅ ▇ █", "▇ █ ▇ ▅ ▃ ▂ ▃ ▅ ▇ █ ▇", '▅ ▇ █ ▇ ▅ ▃ ▅ ▇ █ ▇ ▅', '▃ ▅ ▇ █ ▇ ▅ ▇ █ ▇ ▅ ▃', '▂ ▃ ▅ ▇ █ ▇ █ ▇ ▅ ▃ ▂' ]
    for i in range(100):
        sys.stdout.write('\r' + teks + wave[i % len(wave)])
        sys.stdout.flush()
        time.sleep(0.1)

memuat("Haiii")