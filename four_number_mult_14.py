#Elaborar un algoritmo que determine si un numero (positivo de 4 cifras) dado es multiplo
# de 3, multiplo de 6 omultiplo de ambos.
def number(value):
    if value % 6 == 0:
        print(f"The number {value} is multiple of 3 and 6 ")
    elif value % 3 == 0:
        print(f"The number {value} is multiple of 3 ")
    else:
        print("This number is not  multiple of 3 and 6")

if __name__ == "__main__":
    v = int(input("Enter number: "))

    if 1000 <= v <= 9999:
        number(v)
    else:
        print("Enter a number of four digits, more arent allowed")
