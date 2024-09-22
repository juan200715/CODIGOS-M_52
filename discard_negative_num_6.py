#Elaborar un algoritmo que lea cuatro numeros ingresados por el usuario y los sume,
#descartando los negativos.

def value():
    sume = 0
    for i in range(4):
        num = float(input("Enter number: "))
        if num >= 0:
            sume += num
    return sume

result = value()
print(f"The sume of the numbers is {result}")




        















# def numbers(sume):
#     if sume <= 0:
#         print()

# sume = num_1 +num_2 + num_3 + num_4
# print(sume)

