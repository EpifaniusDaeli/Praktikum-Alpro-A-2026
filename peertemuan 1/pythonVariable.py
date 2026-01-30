#casting
x = str(3)    # x jadi  '3'
y = int(3)    # y jadi  3
z = float(3)  # z jadi 3.0

#case sensitive
a= 3 
A= 6 #A TIDAK SAMA DENGAN a!!

#nama variabel
myvar = "Epi"
my_var = "Epi"
_my_var = "Epi"
myVar = "Epi"
MYVAR = "Epi"
myvar2 = "EPI" #semua yang ini boleh 

'''ini yang nggak boleh
2myvar = "Epi"
my-var = "Epi"
my var = "Epi" 
karena tak boleh angka di awal dan 
tak boleh pakai -
juga tak boleh pakai spasi'''

#ini adalah cara assignment nilai di pyhton untuk banyak varabel dan nilai
x, y, z = "pir", "melon", "anggur"
print(x)
print(y)
print(z)

#ini cara untuk satu nilai untuk banyak variabel
x = y = z = "guava"
print(x)
print(y)
print(z)

#ini cara cetak di python
x = "gua"
y = "ya"
z = "handsome"
print(x, y, z)#ini untuk cetak banyak variabel sekaligus

#global variabel
x = "manis"

def myfunc():
  print("anggur itu ada yang " + x)

myfunc()




