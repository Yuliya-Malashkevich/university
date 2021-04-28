from connect.connect import DataBase
from studentMenu.studentMenu import StudentMenu
import pymysql
from pymysql.cursors import DictCursor


class TeacherMenu(DataBase):
    def __init__(self, login):
        DataBase.__init__(self)
        self.login = login
    #     # self.name_surname = name_surname
    #     # self.course = course
    #     # self.mathematics = mathematics
    #     # self.physics = physics
    #     # self.informatics = informatics


    def changing_course(self):
        data = self.change_course() #self.name_surname, 4
        # print(data)
        for i in data:
            print(i)
        id = input("Введите id студента: ")
        get_id = self.get_id(id)
        print(get_id)
        course = input("Измените курс: ")
        self.add_course(id, course)

    def changing_marks(self):
        data = self.change_course()
        # print(data)
        for i in data:
            print(i)
        id = input("Введите id студента: ")
        marks = self.select_marks(id)
        print(f"mathematics: {marks['mathematics']} \n physics: {marks['physics']} "
              f"\n informatics: {marks['informatics']} ")
        mathematics = input("mathematics: ")
        physics = input("physics: ")
        informatics = input("informatics ")
        self.change_marks(id, mathematics, physics, informatics)

    def all_information(self):
        name_surname = input("Введите фамилию и имя студента: ")
        data = self.student_information(name_surname)
        print(data)
        data = self.average_rating(name_surname)
        summ = 0
        counter = 0
        for key in data:
            if data[key] != 'NULL':
                summ += int(data[key])
                counter += 1
        print(summ / counter)



    def menu(self):
        while True:
            print('МЕНЮ ВЫБОРА: ' '\n' '1.Changing course' '\n' '2.Changing score' '\n' '3.Student information' '\n' '0.Exit')
            type = int(input("Выберите пункт: "))
            if type == 1:
                self.changing_course()
            elif type == 2:
                self.changing_marks()
            elif type == 3:
                self.all_information()
            elif type == 0:
                break

