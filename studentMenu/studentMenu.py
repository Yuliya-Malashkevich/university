from connect.connect import DataBase


class StudentMenu(DataBase):
    def __init__(self, login):
        DataBase.__init__(self)
        self.login = login

    def viewing_progress(self):
        data = self.getStudentInfo(self.login)
        print(data)
        # print(1)

    def student_rating(self):
        data = self.average_rating(self.login)
        summ = 0
        counter = 0
        for key in data:
            if data[key] != 'NULL':
                summ += int(data[key])
                counter += 1
        print(summ/counter)

    def menu(self):
        while True:
            print('МЕНЮ ВЫБОРА: ' '\n' '1.Average rating' '\n' '2.Student information' '\n' '0.Exit')
            type = int(input("Выберите пункт: "))
            if type == 1:
                self.student_rating()
            elif type == 2:
                self.viewing_progress()
            elif type == 0:
                break