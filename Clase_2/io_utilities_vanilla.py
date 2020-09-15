import numpy as np
import pandas as pd

# #Ejemplo de Clases en Python
# class Student():
#     def __init__(self, name, last_name, major):
#         self.name = name
#         self.last_name = last_name
#         self.major = major
#         self.grades = []
#     def add_grades(self, grade):
#         self.grades.append(grade)
#         print("A grade of {} was added to the student {} {}".format(grade, self.name, self.last_name))
#     def get_average(self):
#         return np.mean(self.grades)
#
# def check_student_class():
#     edo = Student("Edoardo", "Bucheli", "MCC")
#     print(edo.major)
#     edo.add_grades(95)
#     average = edo.get_average()
#     print("The average is {}".format(average))
#
#
# Evitar funciones globales
# if __name__ == '__main__':
#     check_student_class()

def main():
    filepath = './Data/iris.data'
    with open(filepath,'r') as fp:
        data = fp.read()

    data_lines = data.split('\n')

    # data_final = []
    # for line in data_lines:
    #     data_final.append(line.split(','))
    # Esto de arriba es igual a lo de abajito
    data_final = [f.split(',') for f in data_lines]



    print(data_final)

if __name__ == '__main__':
    main()
