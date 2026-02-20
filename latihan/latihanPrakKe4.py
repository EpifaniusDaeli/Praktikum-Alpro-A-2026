#D. Tugas Praktikum – Sistem Registrasi Peserta Event
print("\n=== Registrasi Peserta Seminar ===")
while True:
    try:
        nama = input("Masukkan nama peserta: ")
        if len(nama) < 3:
            print("Nama harus lebih dari 3 karakter!")
            continue
        break
    except ValueError:
            raise ValueError("Nama harus lebih dari 3 karakter!")
umur = input("Masukkan umur peserta: ")
email = input("Masukkan email peserta: ")
#latihan bagian C di materi praktikum
#1    
angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')
    
#2
while True:
    try:
        a1 = int(input("Masukkan angka Pertama:"))
        break
    except ValueError:
        print("Input harus angka!")
while True:
    try:
        a2 = int(input("Masukkan angka kedua:"))
        break
    except ValueError:
        print("Input harus angka!")
try:
    hasil = a1 / a2
    print("Hasil pembagian: ", hasil)
except ZeroDivisionError:
    print("Tidak bisa bagi pakai nol!")
    

#D. Tugas Praktikum – Sistem Registrasi Peserta Event

            