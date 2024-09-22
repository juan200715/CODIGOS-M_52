#Elaborar un algoritmo que lea un numero de tres (3) cifras e indique si el digito que
#representa las centenas es par.
def descomposition_letters():
    number = int(input("Enter number: ")) 
    if 100 <= number <= 999:
        centene = (number) // 100
        if centene % 2 == 0:
            print(f"The digit {centene} in the centenes is even")
        else:
            print(f"The digit {centene} in the centenes is odd")
    else:
        print("The number doesn't has three values. Please try again")

if __name__ == "__main__":
    descomposition_letters()
