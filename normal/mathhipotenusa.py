#catetos e hipotenusa
import math

cat1 = float(input("Cateto 1: "))
cat2 = float(input("Cateto 2: "))
hipotenusa = math.sqrt((cat1**2 + cat2**2))

print("A sua hipotenusa é:",round(hipotenusa,2))
