from connect.connect import DataBase
from teacherMenu.teacherMenu import TeacherMenu
from studentMenu.studentMenu import StudentMenu

import pymysql
from pymysql.cursors import DictCursor

class Start(DataBase):
    def registration(self):
        login = input('Enter login: ')
        password = input('Enter password: ')
        password = password.replace("4", "a")
        name = input('Enter your name: ')
        surname = input('Enter your surname: ')
        course = input('Enter your course: ')
        self.addUser(login, password, name, surname, course)
        StudentMenu(login).menu()

    def chek_login(self, login):
        # db = DataBase()
        data = self.getUser1(login)
        if data == ():
            return True
        else:
            return False


    def input_data(self):
        login = input('Enter login: ')
        password = input('Enter password: ')
        return login, password
        # if self.chek_login() is False:
        #     self.input_data()
        # else:
        #     db= DataBase()
        #     db.addUser(self,login,password)

    def chek_data(self, login, password):
        data = self.getUser(login, password)
        if data != ():
            return data
        else:
            return False

    def authorization(self):
        while True:
            login, password = self.input_data()
            data = self.chek_data(login, password)
            if data is not False:
                if data['status'] == 'student':
                    StudentMenu(data['login']).menu()
                if data['status'] == 'teacher':
                    TeacherMenu(data['login']).menu()

Start()