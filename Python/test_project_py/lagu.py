import sys
import time

def kalimat(text, baris=0, time_delay1=0.055, time_delay2=0.018, tenses_pause1=1.5, tense_pause2=1.5):
    alpha1 = len(text)
    for wordd in text:
        sys.stdout.write(f"{wordd}")
        sys.stdout.flush()
        time.sleep(time_delay1)  
    sys.stdout.write("\r" + text + " ")
    sys.stdout.flush()
    time.sleep(tenses_pause1)
    if baris == 0:
        for worddd in text:
            text2 = text[:alpha1 - 1]
            sys.stdout.write("\r" + f"{text2:<{alpha1}}")
            sys.stdout.flush()
            time.sleep(time_delay2)
            alpha1 = alpha1 - 1
        sys.stdout.write("\r")
        time.sleep(tense_pause2)
    elif baris == 1:
        sys.stdout.write("\n")
    elif baris == 3: 
        text2 = text[:alpha1 - 1]
        sys.stdout.write("\r" + " " * alpha1)
        sys.stdout.flush()
        sys.stdout.write("\r")
        time.sleep(time_delay2)

kalimat("Sudah terbiasa terjadi tante")
