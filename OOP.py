

class animal():
    def __init__(self, name):
        self.name = name

    def showName(self):
        print('\n i m ' + self.name)


class Cat(animal):
    def __init__(self):
        super().__init__(self.name)
        self.height = "50"
        self.age = '0'

    def showName(self):
        print('\n I m cat ' + self.name)
        print(' Age ' + str(self.age), end='')
        print(' height ' + str(self.height), end = '\n')



class Mouse(animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height


    def showName(self):
        super().showName()
        print('\n age ' + str(self.age))
        print(' height ' + str(self.height))


    def move(self):
        print('Mouse moving .... ')




if __name__ == '__main__':

    tom = Cat(name='Tom', age=20, height='11')
    tom.showName()

    giv = animal(name='giv')
    giv.showName()

    jerry = Mouse('jerry', 3, 5)
    jerry.showName()