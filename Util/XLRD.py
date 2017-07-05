import xlrd
import numpy

def Getcontent(slef,path,sheet=0):
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet]
    return table



