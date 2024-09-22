### Elaborar un algoritmo que determine si un ano ingresado por teclado es o no bisiesto

year = int(input("Year: "))

if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0):
    print(str(year), "It's Bisiesto.")
else:
    print(str(year), "It's NOT Bisiesto.")