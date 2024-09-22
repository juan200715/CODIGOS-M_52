# Elaborar un algoritmo que teniendo el tipo de empleado y su sueldo, calcule el incremento
# salarial y el valor del nuevo sueldo; si se conoce que a los empleados tipo 1 y 2, se les
# aumenta un 5%; y a los tipo 3 y 4 el 12%. El algoritmo debe imprimir el sueldo mas
# aumento

def salary(employee_type, money):
    if employee_type == "1" or employee_type == "2":
        increasement = money * 0.05
        total = money + increasement
        print("The total salary is", total, "$")
    elif employee_type == "3" or employee_type == "4":
        increasement = money * 0.12
        total = money + increasement
        print("The total salary is", total, "$")
    else:
        print("Unclear value, please type again")
    return total

if __name__ == "__main__":
    emp = input("Type of employee. Choose: 1, 2, 3, 4: ")
    m = float(input("Enter your salary: "))
    print(salary(emp, m))
