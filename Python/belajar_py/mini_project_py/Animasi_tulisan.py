
import math
import time
import sys

def tensess(text, time_delay=0.1, tenses_pause=1.8):
    alpha = len(text)
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay)
    time.sleep(tenses_pause)
    sys.stdout.write(f"\r" + " " * alpha)
    sys.stdout.write("\r")




def tenses(text, baris, time_delay=0.1, tenses_pause=2):
    alpha = len(text)
    spasi = " " * alpha
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay)
    time.sleep(tenses_pause)

    sys.stdout.write("\r")
    for worddd in spasi[:alpha]:
        sys.stdout.write(f"{worddd}")
        sys.stdout.flush()
        time.sleep(time_delay)
    if baris == 0:
        sys.stdout.write("\r")
    elif baris == 1:
        print()
    else: 
        pass

def tensees(text, baris=0, time_delay1=0.1, time_delay2=0.15, tenses_pause1=2, tense_pause2=2):
    alpha = len(text)
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay1)
    time.sleep(tenses_pause1)
    sys.stdout.write("\r")
    for worddd in text:
        text2 = text[:alpha - 1]
        sys.stdout.write(f"{text2:<30}")
        sys.stdout.flush()
        time.sleep(time_delay2)
        sys.stdout.write("\r")
        sys.stdout.flush()
        alpha = alpha - 1
    time.sleep(tense_pause2)
    if baris == 0:
        sys.stdout.write("\r")
    elif baris == 1:
        print()
    else: 
        pass
    
def tensees2(text, baris=0, time_delay1=0.1, time_delay2=0.15, tenses_pause1=2, tense_pause2=2):
    alpha = len(text)
    alpha1 = len(text)
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay1)
    time.sleep(tenses_pause1)
    for worddd in text:
        text2 = text[:alpha1 - 1]
        sys.stdout.write("\r" + f"{text2:<{alpha}}")
        sys.stdout.flush()
        time.sleep(time_delay1)
        alpha1 = alpha1 - 1
    time.sleep(tense_pause2)
    if baris == 0:
        sys.stdout.write("\r")
    elif baris == 1:
        print()
    else: 
        pass

import sys, time

def type_and_delete(text, delay=0.1):
    # Ketik huruf satu per satu
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

    time.sleep(1)  # jeda sebelum hapus

    # Hapus huruf satu per satu
    for i in range(len(text)):
        sys.stdout.write('\r' + text[:len(text)-i-1] + ' ' * (i+1))
        sys.stdout.flush()
        time.sleep(delay)

# Coba animasi
type_and_delete("jakjasajkajjaakjssjkjk")


# Coba animasi
tensees2("Belvaaaaa Kmauuuuuu Bikin aku melelehhh")



#tensess("Haiiii epaaaa") 
#tenses("Aku kangen kita mabar kayak dulu bellll", 0)

