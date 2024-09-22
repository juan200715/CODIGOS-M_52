# Elaborar un algoritmo que solicite un numero de dia de entre 1 y 7; e imprima el dia de la
#semana correspondiente.
def day_week():
    number = int(input("Number: "))
    week = {1: "Monday",2: "Tuesday", 
            3: "Wednesday", 4: "Thursday",
              5: "Friday", 6: "Saturday",
                7: "Sunday"}
    if 1 <= number <= 7:
        print(f"The day of the week is {week[number]}")
    else:
        print("Unable number")

if __name__ == "__main__":
    day_week()