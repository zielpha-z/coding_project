#Date (24/1/26)
import random, math, sys, time
tebak = 0
angka = 50
angka2 = 50
jawabh = "SALAH" 
jawab = ""
memo = 50
percobaan = 0
jawab1 = ""
jawab2 = ""
jawab3 = ""


def loading(teks="Loading", pengulangan=int(random.randint(1, 3)), delay1=0.2, delay2=0.2):
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


kalimat("Haloo...") 
kalimat("Selamat datang di projek tes ku yang ke-2")
kalimat("Di projek ini aku akan menebak pikiranmu")
kalimat("Jadi, aku mau kamu memilih angka acak dari 1-100")
kalimat("Kalau kamu sudah menentukannya-")
kalimat("Aku sarakan untuk menulisnya disuatu tmepat agar tidak lupa")
kalimat("Lalu, aku akan memberimu pertanyaan dan tebakkan")
kalimat("Pertanyaanya berupa, apakah angka kamu lebih besar atau lebih kecil?")
kalimat("Kalau angkanya lebih besar, jawab 'besar'-")
kalimat("dan kalau angkanya lebih kecil, jawab 'kecil'")
kalimat("Untuk tebakkan, kamu bisa jawab 'benar' atau 'salah'")
kalimat("Kamu harus menjawabnya dengan jujur")
kalimat("Kalau kamu jujur, aku akan bisa menebanyak hanya dalam 7 kali percobaan")


while True:
    kalimat("Apakah kamu siap?", 1)
    print("1). Ya \n2). Tidak")
    jawab1 = input("Jawab: ")
    loading("Loading")
    if jawab1.isalpha():
        jawab1 = jawab1.upper()
        if jawab1 == "YA":
            kalimat("Oke... Ayo kita mulai sekarang!")
            break
        elif jawab1 == "TIDAK":
            kalimat("Tidak papa kok kalau kamu belum siap")
            kalimat("Tekan saja tombol run lagi, kapanpun kamu siap")
            kalimat("Sampai jumpa lagi...")
            loading()
            sys.exit()
        else:
            print("Tolong masukkan jawaban yang sesuai!")
            kalimat("Ulangi...", 1)
    elif jawab1.isdigit():
        print("Tolong hanya masukkan jawaban berupa huruf!")
        kalimat("Ulangi...", 1)
    else:
        print("Tolong masukkan jawaban yang valid dong!")
        kalimat("Ulangi...", 1)


kalimat("Sebelum masuk ke permainannya, aku mau kamu pilih mode")
while True:
    kalimat("Apakah kamu mau ada kesempatan ku untuk menebak dan bertanya?", 1)
    print("1). Ya\n2). Tidak")
    jawab2 = input("Jawab: ")
    loading()
    if jawab2.isalpha():
        jawab2 = jawab2.upper()
        if jawab2 == "YA":
            kalimat("Oke... Ayo kita mulai sekarang!")
            break
        elif jawab2 == "TIDAK":
            kalimat("Tidak papa kok kalau kamu belum siap")
            kalimat("Tekan saja tombol run lagi, kapanpun kamu siap")
            sys.exit()
        else:
            print("Tolong masukkan jawaban yang sesuai!")
            kalimat("Ulangi...", 1)
    elif jawab2.isdigit():
        print("Tolong hanya masukkan jawaban berupa huruf!")
        kalimat("Ulangi...", 1)
    else:
        print("Tolong masukkan jawaban yang valid dong!")
        kalimat("Ulangi...", 1)


if jawab2 == "YA":
    kalimat("Kamu memilih mode kesempatan")
    kalimat("Pilihlah berapapun kesempatan yang kamu mau")
    kalimat("Minimal 4 kesempatan dan maksimal 20")
    kalimat("Meskipun begitu-")
    kalimat("Aku pede sih kalau akau bisa menebaknya dalam 7 kesempatan")
   
    while True:
        kalimat("Masukkan kesempatan yang kamu mau", 1)
        print("Pilih dari 4-20")
        kesempatan = input("Jawab: ")
        loading()
        if kesempatan.isalpha():
            print("Tolong hanya masukkan jawawan berupa angka!")
            kalimat("Ulangi...", 1)
        elif kesempatan.isdigit():
            kesempatan = int(kesempatan)
            if 3 < kesempatan <= 20:
                kesempatanabs = kesempatan
                if kesempatan < 7:
                    kalimat(f"Oke, aku menerima hanya dengan {kesempatan}")
                    kalimat("Meskipun kesempatan dibawah 7, tapi aku yakin aku bisa")
                    kalimat("Ayo mulai!", 1)
                    break
                elif kesempatan == 7:
                    kalimat("Pas banget nih 7 kesempatan")
                    kalimat("Sesuai dengan kemampuan ku!")
                    kalimat("Ayo kita mulai!", 1)
                    break
                elif kesempatan > 7:
                    kalimat("Wah, sepertiya kesempatannya sedikit kebanyakan")
                    kalimat("Makin mudah inimah bagiku untuk menebaknya")
                    kalimat("Ayo kita mulai sekarang!", 1)
                    break
            else:
                print("Hanya 4-20 kesempatan aja woi!")
                print("Nggak lebih nggak kurang")
                kalimat("Ulangi...", 1)
        else:
            print("Tolong masukkan jawaban yang valid dong!")
            kalimat("Ulangi...", 1)


    while kesempatan >= 1:
        while jawabh == "SALAH":
            if kesempatan > 1:
                percobaan +=1 
                selisih = abs(angka2 - angka)  
                angka3 = math.ceil(50 * pow(0.5, percobaan))
                
                if jawab == "BESAR":
                    angka2 =  angka2 + angka3
                elif jawab == "KECIL":
                    angka2 = angka2 - angka3

                print(f"Tebakan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka mu adalah {angka}", 1)
                    print("1). Benar\n2). Salah")
                    jawabh = input("Jawab: ")
                    if jawabh.isalpha():
                        jawabh = jawabh.upper()
                        if jawabh == "SALAH":
                            kalimat("HmmHhmM, Salah ya? Oke")
                            break
                        elif jawabh == "BENAR":
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawabh.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)
                if jawabh == "SALAH":
                    pass
                elif jawabh == "BENAR":
                    break

                print(f"Pertanyaan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka kamu lebih besar atau lebih kecil?", 1)
                    print("1). Besar\n2). Kecil")
                    jawab = input("Jawab: ")
                    if jawab.isalpha():
                        jawab = jawab.upper()
                        if jawab == "BESAR":
                            kalimat("Ohhhh, lebih besar ya?")
                            break
                        elif jawab == "KECIL":
                            kalimat("Ohhhh, lebih kecil ya?")
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawab.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)


                angka3 = math.ceil(50 * pow(0.5, percobaan))
                if jawab == "BESAR":
                    angka =  angka + angka3
                elif jawab == "KECIL":
                    angka = angka - angka3
                selisih2 = angka2 - angka
                kesempatan -= 1


            elif kesempatan == 1 and kesempatanabs < 7:
                kalimat("Aduh, Kesempatan ku tinggal 1")
                kalimat("Kalau begitu aku akan menebak")
                angka = random.randint(angka2, angka + 1)
                print(f"Tebakan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka mu adalah {angka}", 1)
                    print("1). Benar\n2). Salah")
                    jawabh = input("Jawab: ")
                    loading()
                    if jawabh.isalpha(): 
                        jawabh = jawabh.upper()
                        if jawabh == "SALAH":
                            kalimat("Hah, Salahkah?")
                            kalimat("Baiklah kalau begitu, kamu menang")
                            kalimat("Tchihh, selamat ya.")
                            kalimat("Aku kalah gara gara kamu memberiku kesempatan dibawah 7 btw")
                            kalimat("Ayo kita bermain lagi nanti!")
                            sys.exit()
                        elif jawabh == "BENAR":
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawabh.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)
            elif kesempatan == 1 and kesempatanabs > 7:
                kalimat("Aduh, Kesempatan ku tinggal 1")
                kalimat("Kalau begitu aku akan menebak")
                angka = random.randint(angka2, angka + 1)
                print(f"Tebakan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka mu adalah {angka}", 1)
                    print("1). Benar\n2). Salah")
                    jawabh = input("Jawab: ")
                    loading()
                    if jawabh.isalpha(): 
                        jawabh = jawabh.upper()
                        if jawabh == "SALAH":
                            kalimat("Hah, Apa? Salah???")
                            kalimat("Nggak mungkin, kamu pasti berbohong!")
                            for q in range(15):
                                kalimat("BERBOHONG BERBOHONG BERBOHONG", 3, 2,)
                            for w in range(10):
                                print()
                            time.sleep(5)
                            kalimat("Kamu yakin udah jujur?")
                            kalimat("Baiklah")
                            kalimat("Tchihh, selamat ya.")
                            kalimat("Aku kalah gara gara proyek ini masih banyak bug btw")
                            kalimat("Atau kamu yang tidak mau mengakui kalau kamu bohong")
                            kalimat("Ya sudahlah...")
                            kalimat("Ayo kita bermain lagi nanti!", 1)
                            sys.exit()
                        elif jawabh == "BENAR":
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawabh.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)

        break

    
elif jawab2 == "TIDAK":
    kalimat("Oke kalau begitu, kamu memilih modetanpa kesempatan!")
    kalimat("Aku akan menebak pikiranmu hanya dengan 7 kali kesempatan saja")
    kesempatan = 7
    kesempatanabs = 7
    while kesempatan >= 1: 
        while jawabh == "SALAH":
            if kesempatan > 1:
                percobaan +=1 
                selisih = abs(angka2 - angka)  
                angka3 = math.ceil(50 * pow(0.5, percobaan))
                if jawab == "BESAR":
                    angka2 =  angka2 + angka3
                elif jawab == "KECIL":
                    angka2 = angka2 - angka3


                print(f"Tebakan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka mu adalah {angka}", 1)
                    print("1). Benar\n2). Salah")
                    jawabh = input("Jawab: ")
                    if jawabh.isalpha:
                        jawabh = jawabh.upper()
                        if jawabh == "SALAH":
                            kalimat("HmmHhmM, Salah ya? Oke")
                            break
                        elif jawabh == "BENAR":
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawabh.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)
                if jawabh == "SALAH":
                    pass
                elif jawabh == "BENAR":
                    break
                
                print(f"Pertanyaan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka kamu lebih besar atau lebih kecil?", 1)
                    print("1). Besar\n2). Kecil")
                    jawab = input("Jawab: ")
                    if jawab.isalpha:
                        jawab = jawab.upper()
                        if jawab == "BESAR":
                            kalimat("Hhhmmm... Lebih besar ya...")
                            break
                        elif jawab == "KECIL":
                            kalimat("Hhhmmm... Lebih kecil ya...")
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawab.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)


                angka3 = math.ceil(50 * pow(0.5, percobaan))
                if jawab == "BESAR":
                    angka =  angka + angka3
                elif jawab == "KECIL":
                    angka = angka - angka3
                selisih2 = angka2 - angka
                kesempatan -= 1
            elif kesempatan == 1 and kesempatanabs == 7:
                kalimat("Aduh, Kesempatan ku tinggal 1")
                kalimat("Sudah banyak aku salah menebak")
                kalimat("Aha, sekarang, aku tahu!")
                angka = random.randint(angka2, angka + 1)
                print(f"Tebakan ke-{percobaan}")
                while True:
                    kalimat(f"Apakah angka yang kamu pikirkan adalah adalah {angka}", 1)
                    print("1). Benar\n2). Salah")
                    jawabh = input("Jawab: ")
                    loading()
                    if jawabh.isalpha():
                        jawabh = jawabh.upper()
                        if jawabh == "SALAH":
                            kalimat("Hah, Apa? Salah???")
                            kalimat("Nggak mungkin, kamu pasti berbohong!")
                            for q in range(25):
                                kalimat("BERBOHONG BERBOHONG BERBOHONG", 3, 2,)
                            for w in range(10):
                                print()
                            time.sleep(5)
                            kalimat("Kamu yakin udah jujur?")
                            kalimat("Baiklah")
                            kalimat("Tchihh, selamat ya.")
                            kalimat("Aku kalah gara gara proyek ini masih banyak bug btw")
                            kalimat("Atau kamu yang tidak mau mengakui kalau kamu bohong")
                            kalimat("Ya sudahlah...")
                            kalimat("Ayo kita bermain lagi nanti!", 1)
                            sys.exit()
                        elif jawabh == "BENAR":
                            break
                        else:
                            print("Tolong masukkan jawaban yang sesuai!")
                            kalimat("Ulangi...", 1)
                    elif jawabh.isdigit():
                        print("Tolong hanya masukkan jawaban berupa huruf!")
                        kalimat("Ulangi...", 1)
                    else:
                        print("Tolong masukkan jawaban yang valid dong!")
                        kalimat("Ulangi...", 1)
        break


kalimat("Wow...")
kalimat("Sepertinya aku benar")
kalimat("Tuh kan, apa kataku")
kalimat("Aku bisa membaca pikiranmu")
kalimat("Jangan marah... Ini cuma permainan kok, hehe")
kalimat("Terimakasih telah bermain dengan ku")
kalimat("Dan mencoba proyekku")
kalimat("Cobalah lagi kapanpun kamu mau")
kalimat("Terimakasih, sekali lagi")





