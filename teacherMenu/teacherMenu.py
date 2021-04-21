from connect.connect import DataBase
import pymysql
from pymysql.cursors import DictCursor


class TeacherMenu(DataBase):
    def __init__(self, name_surname):
        DataBase.__init__(self)
        # self.login = login
        self.name_surname = name_surname
        # self.course = course
        # self.mathematics = mathematics
        # self.physics = physics
        # self.informatics = informatics


    def changing_course(self):
        data = self.change_course(self.name_surname)
        print(data)
        # for i in data:
        #     print(i)
        # name_surname = input("Введите surname end name студента: ")
        # get_course = self.get_course()
        # print(get_course)
        # course = input("Измените курс: ")
        # self.add_course(course, name_surname)
        # print(1)

    def changing_score(self):
        data = self.change_score(self.name_surname)
        print(data)

        # data = DataBase().change_score()
        # for i in data:
        #     print(i)
        # name_surname = input("Введите имя и фамилию студента: ")
        # score = DataBase().change_score(name_surname)
        # print(f"mathematics: {score['mathematics']} \n physics: {score['physics']} "
        #       f"\n informatics: {score['informatics']} ")
        #
        # mathematics = input("mathematics: ")
        # physics = input("physics: ")
        # informatics = input("informatics ")
        #
        # DataBase().change_score(name_surname, mathematics, physics, informatics)

    def all_information(self):
        data = self.student_information(self.name_surname)
        print(data)

    def menu(self):
        while True:
            print('МЕНЮ ВЫБОРА: ' '\n' '1.Changing course' '\n' '2.Changing score' '\n' '3.Student information' '\n' '0.Exit')
            type = int(input("Выберите пункт: "))
            if type == 1:
                self.changing_course()
            elif type == 2:
                self.changing_score()
            elif type == 3:
                self.all_information()
            elif type == 0:
                break

