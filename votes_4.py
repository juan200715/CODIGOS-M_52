# Se cuenta con los votos obtenidos por Juan, Pedro y Maria en una eleccion democratica a
#la presidencia de un club. Para ganar la eleccion se debe obtener como minimo el 50% del
#total de votos mas 1. En caso que no haya un ganador, se repite la eleccion en una segunda
#vuelta, yendo a esta los dos candidatos que obtengan la mas alta votacion. Se anula la
#eleccion en caso de producirse un empate doble por el segundo lugar o un empate triple.
#Disene un algoritmo que determine el resultado de la eleccion

def results(vjuan, vpedro, vmaria):
    total = vjuan + vpedro + vmaria
    min_votes = total / 2 + 1
    if vjuan >= min_votes:
        result = "Juan wins the election" 
    elif vpedro >= min_votes:
        result = "Pedro wins the election" 
    elif vmaria >= min_votes:
        result = "Maria wins the election"
    else:
        if vpedro > vjuan and vmaria > vjuan:
            result = "Pedro and Maria go into second round!"
        elif vpedro > vmaria and vjuan > vmaria:
            result = "Pedro and Juan go into second round!"
        elif vmaria > vpedro and vjuan > vpedro:
            result= "Maria and Juan go into second round!"
        else:
            result = "Election has been anulated"
    return result

if __name__ == "__main__":
    vj = int(input("Enter amount of votes from Juan: "))
    vp = int(input("Enter amount of votes from Pedro: "))
    vm = int(input("Enter amount of votes from Maria: "))
    print(results(vj,vp,vm))