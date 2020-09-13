


class paint():
    def __init__(self, x = 0 , y = 0 ):
        self.x = x
        self.y = y

    def checkValue(x):
        if isinstance(x, int):
            return True
        return False

    def setCords(self, x, y):
        if paint.checkValue(x) and paint.checkValue(y):
            self.x = x
            self.y = y

    def __getattribute__(self, item):
        if item == "paint__x":
            return self.x


pt = paint(1, 2)
pt.setCords(2, 3)
print(pt.__dict__)