import datetime

class Person:
    def __init__(self, name): # name : STRING
        self.name = name
        try:
            # str1.rindex(str2, startindex, endindex)
            # returns the index of last str2 in str1
            # returns ERROR for notfound
            LastBlank = name.rindex(' ') # find index of the last blank
            self.lastname = name[LastBlank + 1 : ]
        except: # if ERROR, then...
            self.lastname = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastname

    def setBirthday(self, birthday):
        self.birthday = birthday

    def getAge(self):
        if self.birthday == None:
            # raise : Gives out the ERROR
            raise ValueError
        else:
            return (datetime.date.today() - self.birthday).days // 365
    def __lt__(self, other):
        if self.lastname == other.lastname
            return self.name < other.name
        return self.lastname < other.lastname
    def __str__(self):
        return self.name

Yonezu = Person('Kenshi Yonezu')
Amiyon = Person('Aimyon')

Yonezu.setBirthday(datetime.date(1991, 3, 10))
Amiyon.setBirthday(datetime.date(1995, 3, 5))

print(Yonezu.getName() + ' is ' + str(Yonezu.getAge()) + ' years old')
print(Amiyon.getName() + ' is ' + str(Amiyon.getAge()) + ' years old')
