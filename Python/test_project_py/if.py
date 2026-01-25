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

kesempatan = 7
kesempatanabs = 7
while kesempatan >= 1:
    while jawabh == "SALAH":
        if kesempatan > 1:
            percobaan += 1 
            selisih = abs(angka2 - angka)  
            angka3 = math.ceil(50 * pow(0.5, percobaan))
            if jawab == "LEBIH BESAR":
                angka2 =  angka2 + angka3
            elif jawab == "LEBIH KECIL":
                angka2 = angka2 - angka3
            print(f"apakah angka kamu adalah {angka}")
            jawabh = input("Masukkan: ")
            print(f"Apakah angka kamu lebih besar atau lebih kecil dari {angka} ")
            jawab = input("Masukkan: ")
            angka3 = math.ceil(50 * pow(0.5, percobaan))
            if jawab == "LEBIH BESAR":
                angka =  angka + angka3
            elif jawab == "LEBIH KECIL":
                angka = angka - angka3
            selisih2 = angka2 - angka
            kesempatan -= 1
        elif kesempatan == 1 and percobaan <7:
            angka = random.randint(angka2, angka + 1)
            print(f"{angka}b")
            break
    break

