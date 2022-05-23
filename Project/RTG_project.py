import random

nama = [
    "Izzan",
    "Mirza",
    "Erwin",
    "Najwa",
    "Kanaya"
    ]

tim = int(input("Jumlah Kelompok: "))
member = len(nama)//tim
lebih = len(nama) % tim

keluar = []

def tampilkanNama():
    nomor = random.randrange(len(nama))
    if len(keluar) == 0:
        print("\t\t", nama[nomor])
        keluar.append(nomor)
    else:
        for i in range(len(keluar)):
            if nomor == keluar[i]:
                cek = False
                break
            else:
                cek = True
        
        if cek:
            print("\t\t", nama[nomor])
            keluar.append(nomor)
        else:
            tampilkanNama()
        

for i in range(tim): #menampilkan kelompok
    print("Kelompok", i+1)
    if i < lebih:
        for j in range(member+1): #menampilkan nama
            tampilkanNama()
    else:
        for j in range(member): #menampilkan nama
            tampilkanNama()