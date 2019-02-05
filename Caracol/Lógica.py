Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as np

def txtToArray(txt):
    if isinstance(txt, str):
        return txtToArray(txt.split("\n"))
    if isinstance(txt, list):
        if len(txt) > 1:
            return [list(map(int, txt[0].split(" ")))] + txtToArray(txt[1:])
        else:
            return [list(map(int, txt[0].split(" ")))]

def imprimirCar(m, x, y):
    if len(m)==1:
        return [m[x][y]]
    if x==0 and y<(len(m[x])-1):
        return [m[x][y]] + imprimirCar(m, x, y + 1)
    if y==(len(m[x])-1) and x<(len(m)-1):
        return [m[x][y]] + imprimirCar(m, x + 1, y)
    if x==(len(m)-1) and y>0:
        return [m[x][y]] + imprimirCar(m, x, y - 1)
    if y==0 and x>0:
        if x-1>0:
            return [m[x][y]] + imprimirCar(m, x - 1, y)
        else:
            return [m[x][y]] + imprimirCar((np.array(m))[1:-1,1:-1], x - 1, y)
    return []
