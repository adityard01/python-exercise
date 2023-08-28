import random

pilihan = ['batu','gunting','kertas']

#cetak skor tiap ronde
def cetak_skor(skor_user, skor_komputer):
    print(f"Anda : {skor_user} vs {skor_komputer} Komputer\n")

jumlah_ronde = int(input("Masukkan Jumlah Ronde : "))

skor_user=skor_komputer=0

for _ in range(jumlah_ronde):
    pilihan_user = input("Masukkan pilihan anda : ").lower()

    #kalo inputnya salah, munculin error, terus minta input ulang
    while pilihan_user not in pilihan:
        print("Input yang bener dong! Pilih batu, gunting, atau kertas")
        pilihan_user = input("Masukkan pilihan anda : ").lower()

    pilihan_komputer = random.choice(pilihan)

    print(f"Anda pilih : {pilihan_user}, Komputer pilih : {pilihan_komputer}")

    if (pilihan_komputer==pilihan_user):
        print("Seri")
    elif (pilihan_user=='batu' and pilihan_komputer=='gunting') or (pilihan_user=='gunting' and pilihan_komputer=='kertas') or (pilihan_user=='kertas' and pilihan_komputer=='batu'):
        print("Anda Menang")
        skor_user += 1
    else :
        print("Anda Kalah")
        skor_komputer += 1

    cetak_skor(skor_user,skor_komputer)

print("Skor Akhir :")
print(f"Anda : {skor_user} vs {skor_komputer} Komputer")