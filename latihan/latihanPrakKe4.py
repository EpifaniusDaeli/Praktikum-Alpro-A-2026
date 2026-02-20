#D. Tugas Praktikum – Sistem Registrasi Peserta Event
#class exception custom        
class NamaError(Exception):
    def __init__(self, nama):
        self.nama = nama
        super().__init__('\033[91m[ERROR]\033[0m Nama terlalu pendek minimal 3 karakter dan berupa huruf!')
                
class UmurError(Exception):
   def __init__(self, umur):
        self.umur = umur
        super().__init__('\033[91m[ERROR]\033[0m Umur tidak memenuhi syarat (17-60 tahun)')   
        
class EmailError(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__('\033[91m[ERROR]\033[0m Email tidak valid! Harus mengandung "@"')
                      
class NoHPError(Exception):
    def __init__(self, noHP):
        self.noHP = noHP
        super().__init__('\033[91m[ERROR]\033[0m No HP harus berupa angka dan antara 10-13 digit!')

           
#fungsi validasi
def validasi_nama(nama):
    if not nama.replace(" ", "").isalpha() or len(nama) < 3:
        raise NamaError(nama)
    return True
    

def validasi_umur(umur):
    if  umur < 17 or umur > 60:
        raise UmurError(umur)
    return True

def validasi_email(email):
    if "@" not in email:
        raise EmailError(email)
    return True
               
def validasi_noHP(noHP):
    if not noHP.isdigit() or len(noHP) < 10 or len(noHP) > 13:
        raise NoHPError(noHP)
    return True
   

    
              
#main program
while True:
    try:    
        print("\n=== Regristrasi Peserta Seminar ===")
        while True:
            try:
                nama = input("Masukkan nama: ")
                validasi_nama(nama)
                break
            except NamaError as e:
                print(e)
            

        while True:
            try:
                umur = int(input("Masukkan umur:"))
                validasi_umur(umur)
                break   
            except UmurError as e:
                print(e)
            except ValueError:
                print("\033[91m[ERROR]\033[0m Umur harus angka!")

        while True:
            try:
                email = input("Masukkan Email:")
                validasi_email(email)
                break
            except EmailError as e:
                print(e)
            
                
        while True:
            try:
                noHP = input("Masukkan No HP:")
                validasi_noHP(noHP)
                break
            except NoHPError as e:
                print(e)
                
    finally:
     print("Proses input selesai.")
    break

#tampilkan data peserta
print("\n=== Data Peserta ===")
print("Nama:", nama)
print("Umur:", umur)        
print("Email:", email)
print("No HP:", noHP)

  
            

        
    
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
    



            