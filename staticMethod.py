class Date():
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year


    def display(self):
        return f"{self.month}-{self.day}-{self.year}"


    @classmethod
    def mil_c(cls, month, day):
        return cls(month, day, 2000)


    @staticmethod
    def mil_x(month, day):
        return Date(month, day, 2000)



class DateTime(Date):
    def display(self):
        return f"{self.month}-{self.day}-{self.year} - 00:00:00"


d1 = Date.mil_c(9 , 6)
d2 = Date.mil_x(9 , 6)

dt1 = DateTime(10,10,1990)
dt2 = DateTime.mil_c(10,10)

print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))

print(dt1.display())
print(dt2.display())