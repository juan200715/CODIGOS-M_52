#Elabore un algoritmo que descomponga un numero entero de tres cifras en sus digitos y
#luego imprima cada uno de ellos en letras

digits = {0: "cero", 1: "one", 2: "two", 3: "three", 4: "four",
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

def descomposition_letters(number):
    if 100 <= number <= 999:
        c,d,u = number // 100, (number % 100) // 10, number % 10
        print(f"First: {digits[c]}, Second: {digits[d]}, Third: {digits[u]}")
    else:
        print("Enter three digits")


number = int(input("Enter number: ")) 
descomposition_letters(number)