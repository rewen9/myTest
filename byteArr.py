

# вывести результат функции
def wrapPrint(func):
    def val_print(*args):
        return_val = func(*args)
        print(return_val)
        return return_val
    return val_print


@wrapPrint
def testList(s='shrubbery'):
    list_s = list(s)
    list_s[1] = 'w'
    testLtoStr = ''.join(list_s)
    testLtoStr2 = bytearray(b'spam')
    testLtoStr2.extend(b'eggs')
    testLtoStr2 = testLtoStr2.decode()


    sv = testLtoStr2
    print(sv)
    sv = sv.find('g')

    return sv


if __name__ == '__main__':
    strWord = 'strawberry'
    testList(strWord)