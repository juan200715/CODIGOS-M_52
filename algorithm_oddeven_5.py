#Elaborar un algoritmo que lea dos numeros ingresados por el usuario, si la suma de los dos
#numeros es negativa, mostrar su promedio , de lo contrario mostrar si el resultado es par o
#impar.

num_1 = int(input("Enter num 1: "))
num_2 = int(input("Enter num 2: "))

sume = num_1 + num_2

if sume <= 0:
    print(sume)
else:
    if sume % 2 == 0:
        print(sume ,"Is Even")
    else:
        print(sume ,"Is Odd")