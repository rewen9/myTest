class English:
    def greet(self):
        print("Hello")


class French:
    def greet(self):
        print("Bonjur")


def intro(language):
    language.greet()

eng = English()
fr = French()

intro(eng)
intro(fr)