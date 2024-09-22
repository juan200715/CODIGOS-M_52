#Elaborar un algoritmo que lea el nombre, la edad, el sexo y el estado civil de cualquier
#persona e imprima el nombre de la persona; solo si, corresponde a un hombre casado,
# mayor de 40 anos o una mujer soltera menor de 50 anos, y un mensaje que asilo indique.


def state(name, age, gender, civil_status):
    if civil_status == "Married" and gender =="M" and age > 40:
        return name, f" is {civil_status}, it has {age} years and its male"
    elif civil_status == "Single" and gender == "F" and age < 50:
        return name, f" is {civil_status}, it has {age} years and its female"
    else:
        print("Data error, please write correct information.")

if __name__ == "__main__":
    n = input("Enter your name: ")
    a = int(input("Age: "))
    g = input("Enter your gender as M or F: ")
    cs = input("Civil status: ")
    print(state(n,a,g,cs))