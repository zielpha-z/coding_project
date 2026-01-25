
# Date (02/01/2026)
# Membuat permainan tebak tebakan angka tapi yang jawab kita

import random
angka = random.randint(1,100)
percobaan = 0
jawab = 0
komplen = ""
kesalahan = 0

print("Haloo, selamat datang di game tebak angka...")
print("Aku akan memilih 1 angka acak dari 1 - 100")
print("Apakah kamu bisa menebaknya?")
print("Sebelum itu kamu mau berapa kesempatan untuk menebaknya?")


while True:
    kesempatan = input("Jawab: ")
    kesempatanh = kesempatan.isdigit()
    if kesempatanh:
        kesempatan = int(kesempatan)
        if  kesempatan >= 1 and  kesempatan <= 100:
            break
        else:
            print("Tolong masukkan jawaban yang valid dan sesuai")
            print("Kamu mau berapa kesempatan untuk menebak? ")
    else:
        print("Tolong hanya masukkan jawaban berupa angka!")
        print("Kamu mau berapa kesempatan untuk menebak? ")

kesempatan2 = kesempatan

print("Oke, ayo mulai")
print("Pertama, tebak 1 angka dari 1 - 100 untuk memulai")
print("Aku akan memberitahumu apakah angka itu lebih besar atau lebih kecil")
print("Kamu bisa menjadikan itu untuk memberimu petunjuk untuk menebak dengan benar!")
print("Jadi, ayo, apa angka pertamamu?")

while True:
    jawab = input("Jawab ")
    jawabh1 = jawab.isdigit()
    if jawabh1:
        jawab = int(jawab)
        if jawab == angka:
            percobaan += 1
            print("Wihh... Selamat kamu benar!")
            print("Kamu sangat hoki sekali bisa menebaknya dengan sekali coba")
            print(f"Jawabannya adalah {angka}")
            print(f"Kamu menebaknya dengan {percobaan} kali percobaan dari {kesempatan2} kesempatan")
            akurasi = (1 - kesalahan / kesempatan2) * 100
            round(akurasi, 2) 
            print(f"Dengan akurasi jawabanmu sebesar {akurasi}%")
        elif jawab >=  1 and jawab <= 100:
            if angka > jawab:
                komplen = "Angkanya lebih besar dari itu..."
            elif angka < jawab:
                komplen = "Angkanya lebih kecil dari itu..."
            kesalahan += 1
            kesempatan -= 1
            percobaan += 1
            break
        else:
            print("Jawaban tidak bolwh dibawah 1 dan diatas 100, coba ulangi lagi")
            komplen = ""
        
    else:
         print("Jawaban harus angka murni, coba ulangi lagi")
         komplen = ""


while True:
    if jawab == angka:
        print("Selamat... Kamu benar!")
        print(f"Jawabannya adalah {angka}")
        print(f"Kamu menebaknya dengan {percobaan} kali percobaan dari {kesempatan2} kesempatan")
        akurasi = (1 - kesalahan / kesempatan2) * 100
        akurasi = round(akurasi, 2)  
        print(f"Dengan akurasi jawabanmu sebesarr {akurasi}%")
        break
    else:
        if kesempatan > 0:
            while True:
                print(f"Jawabanmu salah! {komplen}")
                print(f"Ayo, coba lagi. Kamu masih punya {kesempatan} kesempatan!")
                jawab = input("Jawab: ")
                jawabh2 = jawab.isdigit()
                if jawabh2:
                    jawab = int(jawab)
                    if jawab >=  1 and jawab <= 100:
                        if angka > jawab:
                            komplen = "Angkanya lebih besar dari itu..."
                        else:
                            komplen = "Angkanya lebih kecil dari itu..."
                        kesalahan += 1
                        percobaan += 1
                        kesempatan -= 1
                        break
                    else:
                        print("Jawaban tidak boleh dibawah 1 dan diatas 100, coba ulangi lagi")
                        komplen = ""
                else:
                    print("Jawabannya harus angka murni, coba ulangi lagi!")
                    komplen = ""
        else:
            print(f"Maaf, kamu gagal menebaknya dengan {kesempatan2} kesempatan")
            print(f"Sebenarnya, angka yang ku pilih adakah {angka}")
            print("Tapi, kerja bagus! Kamu sudah berusaha dengan baik...")
            break


