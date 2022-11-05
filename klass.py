import datetime
import random
class Klass:
    name= ''
    time=random.randint(2008, 2010)
    clas = 'б'
    mark = ''
    def __init__(self, name='', time= datetime.date.today().year, clas = 'б', mark = '' ):
        self.name = name
        self.time = time
        self.clas = clas
        self.mark = mark

    def __str__(self):
        return f' == {self.name} ==\n' \
               f' time = {self.time}\n' \
               f' clas = {self.clas}\n' \
               f' mark = {self.mark}\n'
    def get_age(self):
        return datetime.date.today().year - self.time




