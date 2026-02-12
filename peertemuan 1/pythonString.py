#ini adalah contoh stringnya
"ikan suka plankton"
'ikan suka plankton'
#1 dan 2 sama karena "" dan '' itu setara

#ini contoh cara kasih tanda kutip di kata
print('dosen pa saya adalah "pak irsan"')

#ini cara assignment nilai string
a = "hidup joko.."
print(a)

#ini cara assignment jika nilainya banyak
a="""saya adalah mahasiswa
unri angkatan 2025
di fakultas teknik
jurusan teknik elektro prodi TI"""#bisa juga pakai kutip satu '''
print(a)

#ini cara kayak motong gitu katanya
b = "kulia, mandiri!"
print(b[2:5])#nanti bakal dicetak 
#ibarat motong gitu tapi berdasarkan nilai 
b = "kuliah, mandiri!"
print(b[:5])#ini motong awal

b = "kuliah, mandiri!"
print(b[2:])#ini motonng akhir

b = "kuliah, mandiri!"
print(b[-5:-2])#ini kebalikannya karena pakai negative index

#modify string
a= "kuliah"
print(a.upper())
#dia bakal ubah semua nilai stringnya jadi huruf kapital
#sebaliknya
a= "kerja"
print(a.lower())

#ini untuk misahin nilainya
a = "kuliah, mandiri!"
print(a.split(",")) # bakal jadi ['kuliah', ' mandiri!']

#ini cara python cetak kata
a = "kuliah"
b = "mandiri"
c = a + b
print(c) #dia bakal jadi "kuliah mandi"

#ini cara kalau mau ada spasi
a = "kuliah"
b = "mandiri"
c = a + " " + b
print(c)

#ini contoh format string
age = 19
txt = f"Namaku Epi aku umur {age}"
print(txt)


price= 1.000
txt = f"harganya {price} rupiah"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)#bisa juga nyisipkan operasi aritmatika

txt = "suara \"horeg\" dari jatim." #ini untuk escape kalimatnya

#ini adalah contoh metode string
#1. 
txt = "hai, selamat datang kawan."

x = txt.capitalize()

print (x)

#2.
txt = "hai, selamat datang kawan!"

x = txt.casefold()

print(x)

#3.
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)




