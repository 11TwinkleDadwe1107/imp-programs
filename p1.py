#1. define a class student with following specifications, private member of class student,admission number of type integer, surname of type character, 
#subject english, maths, science of type float, total marks of type float, total pf type float, c total a function to calculate english, maths,
# science with float return type.
#2. public member function of class student take data a function to accept values for admission number, surname, English, science, maths and
#  envoke C total function to calculate total.
#3. show data to display all the data member on the screen

class student:
    def __init__(self, admission_number, surname, english, maths, science):
        self.__admission_number = admission_number
        self.__surname = surname
        self.__english = english
        self.__maths = maths
        self.__science = science
        self.__total_marks = 0.0

    def calculate_total(self):
        self.__total_marks = self.__english + self.__maths + self.__science
        return self.__total_marks

    def take_data(self, admission_number, surname, english, maths, science):
        self.__admission_number = admission_number
        self.__surname = surname
        self.__english = english
        self.__maths = maths
        self.__science = science
        self.calculate_total()

    def show_data(self):
        print("Admission Number:", self.__admission_number)
        print("Surname:", self.__surname)
        print("English:", self.__english)
        print("Maths:", self.__maths)
        print("Science:", self.__science)
        print("Total:", self.__total_marks)


s = student(0, " ", 0, 0, 0)
s.take_data(101, "roy", 89, 99, 75)
s.show_data()