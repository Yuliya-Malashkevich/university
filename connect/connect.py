import pymysql
from pymysql.cursors import DictCursor


class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='user',
            password='3261028',
            database='university',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self, login, password, name, surname, course):
        sql = "INSERT INTO users (login, password, status) VALUES (%s, %s, %s)"
        temp = [login, password, 'student']
        self.cursors.execute(sql, temp)
        self.connection.commit()
        sql = "INSERT INTO student (id, name_surname, course, physics, informatics, mathematics, average_rating, login)" \
              "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"
        temp = ['NULL', name + ' ' + surname, course, 0, 0, 0, 0, login]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def getUsers(self):
        sql = "SELECT * FROM users"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def getUser(self, login, password):
        sql = f"SELECT * FROM users WHERE login = '{login}' and password = '{password}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def getUser1(self, login):
        sql = f"SELECT * FROM users WHERE login ='%s'"
        temp = [login]
        self.cursors.exacute(sql, temp)
        data = self.cursors.fetchall()
        return data

    def getStatus(self, login):
        sql = f"SELECT status FROM users WHERE login = '{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def getStudent(self, login):
        sql = f"SELECT physics, informatics, mathematics FROM student WHERE login = '{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def getStudentInfo(self, login):
        sql = f"SELECT name_surname, course, physics, informatics, mathematics FROM student WHERE login = '{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def average_rating(self, login):
        sql = f"SELECT mathematics, physics, informatics FROM student WHERE login = '{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def get_course(self, name_surname):
        sql = f"SELECT course FROM student WHERE name_surname='{name_surname}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def change_course(self, name_surname, course):
        sql = f"UPDATE student SET course = %s WHERE name_surname = '{name_surname}'"
        temp = ['NULL', 0, course, 0, 0, 0, 0, 0]
        self.cursors.execute(sql, temp)
        self.connection.commit()


    def change_score(self, name_surname, mathematics, physics, informatics): # редактирлвать!!!!!!!!!!!!
        sql = f"UPDATE student SET mathematics = %s, physics = %s, informatics = %s WHERE name_surname = '{name_surname}'"
        temp = ['NULL', 0, 0, mathematics, physics, informatics, 0, 0]
        self.cursors.execute(sql, temp)
        self.connection.commit()

    def student_information(self, name_surname):
        sql = f"SELECT course, physics, informatics, mathematics, average_rating FROM student WHERE name_surname = '{name_surname}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]