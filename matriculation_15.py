#La Universidad tiene dos (2) modalidades de matricula financiera: Completa e Incompleta.
#La matricula completa es aquella con numero de creditos entre 10 y 18, ambos inclusive, y
#tiene un valor fijo de $3.446.000. La matricula incompleta es aquella con numero de
#creditos entre 1 y 9, ambos inclusive, y se cobra segun el numero de creditos tomados,
#donde cada credito tiene un valor fijo de $275.000. Elaborar un algoritmo que permita
#calcular cuanto debe cancelar un estudiante por concepto de matricula.

def matricule(credits):
    if credits < 1 or credits > 18:
        return "Not allowed value, must be in between 1 and 18"
    if 10 <= credits <= 18:
        cost = 3446000
    else:
        cost = credits * 275000
    return f"You must pay {cost} $" 

if __name__ == "__main__":
    c = int(input("Please, enter your credits: "))
    print(matricule(c))






