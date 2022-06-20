'''
作业要求：
编写一个Python包，包里提供若干函数，再写一个py文件，通过读取文本文件中指定的函数名，能够调用该包中的函数。
'''
import string
import MyFuncs.Funcs as funcs

def readFunctionsName(path:str):
    with open(path, "r") as f:
        Funcs = f.read()
    return Funcs.split()

funcNames = readFunctionsName("Funclist.txt")

for funcName in funcNames:
    eval("funcs."+funcName)()