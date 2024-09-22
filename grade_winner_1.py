#Elaborar un algoritmo que permita determinar cual es el ganador de la beca de entre
# cuatro estudiantes. El algoritmo deberahallar la nota definitiva de cada uno de ellos (4
#materias) Si es mayor que 4.5 el alumno podraaspirar a la beca, de lo contrario no.

def calculate_final_note(notes):
    return sum(notes) / len(notes)

def determine_winner(students):
    limit = 4.5
    winner = None
    maximum_note = 0
    for student, notes in students.items():
        definitive_note = calculate_final_note(notes)
        if definitive_note > limit and definitive_note > maximum_note:
            winner = student
            maximum_note = definitive_note
        return winner
    
students = {}
num_students = int(input("Enter the number of the students: "))


for i in range(num_students):
    name = input(f"Enter student's name {i+1}: ")
    notes = []
    for j in range(4):
        note = float(input(f"Enter notes {j+1} of the student {name}: "))
        notes.append(note)
    students[name] = notes

winner = determine_winner(students)
print(f"The winner is: {winner}")
