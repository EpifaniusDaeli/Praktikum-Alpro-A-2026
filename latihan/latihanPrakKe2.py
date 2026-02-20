#latihan 1
def fizzbuzz_plus(n):
  if n % 3 | 5 == 0: 
    print(fizzbuzz_plus(n))
  elif n % 3 == 0:
    print ("Fizz")
  elif n % 5 == 0:
    print ("Buzz")
  elif n % 7 == 0:
    print("Seven")
  else:
    print(n)

#latihan 2
def is_password_valid(password):
  if len(password) < 8:
    return False
  if not any(c.isupper() for c in password):
    return False
  if not any(c.islower() for c in password):
    return False
  if not any(c.isdigit() for c in password):
    return False
  return True


#latihan 3
def is_password_valid(password):
  
  nilai=tugas*0.3% + uts*0.3% + uas*0.4

  if nilai >= 85:
    grade = "A"
  elif nilai >= 70:
    grade = "B"
  elif nilai >= 55:
    grade = "C"
  elif nilai >= 40:
    grade = "D"
  elif nilai < 40:
    grade = "E"

print(nilai)
print(grade)