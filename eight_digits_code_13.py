#En una Universidad, los estudiantes tienen asignado un codigo de 8 cifras, en el que los 4
# primeros digitos indican el ano de matricula, y el que le sigue, el semestre del ano (primero
#o segundo); si se conoce el codigo de un estudiante, elabore un algoritmo que determine
# en que ano y en que semestre, ingreso a la Universidad.

def code(year, semester):
    year_str = str(year)
    semester_str = str(semester)

    if len(year_str) != 4:
        print("The year most have 4 digits")
        return None
    if semester not in [1, 2]:
        print ("Semester most be 1 or 2")

    semester_str = '0' + semester_str 
    student_code = year_str + semester_str + '00'
    return(student_code)

    
if __name__ == "__main__":
    y = int(input("Enter year: "))
    s = int(input("Enter semester 1 for First or 2 for second: "))
    back = code(y, s)
    print("The student's code is", back)
