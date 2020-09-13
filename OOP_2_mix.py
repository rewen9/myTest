import os


class Animal():
    """Класс , простая модель собаки"""

    def __init__(self,
                 name,
                 age):
        self.name = name
        self.age = age
        self.width = 50
        print("Собака создана")


    def set_width(self, width):
        self.width = width


class skelet_animal():
    def __init__(self, width=0):
        self.width = width

    """parent method"""
    def set_width(self):
        self.width = self.width + 5
        return self.width


class Dog(Animal):
    """Класс , простая модель собаки"""
    def __init__(self, name, age):
        super().__init__(name, age)
        self.width = skelet_animal().set_width()
        self.sit = ""
        self.pushistost = "No"


    def sit_dog(self):
        self.sit = "dog sit"

    def no_sit(self):
        self.sit = "dog no sit"

    def set_pushistost(self):
        self.pushistost = "yes"



"""test"""
class annotation():
    def printing(self, *args, **kwargs):
        print(args, kwargs)




if __name__ == '__main__':
    dogFredo = Dog(name="fredo", age="12")
    dogFredo.sit_dog()

    print(dogFredo.sit, "ширина собаки ",  dogFredo.width)