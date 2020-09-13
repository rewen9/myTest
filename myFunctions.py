
import os
import colorama
from json import *



def writeDicInFile(dic, pathToFile):
    with open(pathToFile, 'w') as out:
        for key, val in dic.items():
            out.write('{}:{}\n'.format(key,val))
    return out

def writeFromFileInDic(dic, filetoPath):
    d2 = {}
    with open(filetoPath) as inp:
        for i in inp.readlines():
            key, val = i.strip().split(':')
            d2[key] = val
    print(d2)
    return d2

def writeListWithDicInFile(dic, pathToFile):
    with open(pathToFile, 'w') as out:
        for key, val in dic.items():
            out.write('{}:{}\n'.format(key,val))
    return out