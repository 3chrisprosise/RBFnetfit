import xlrd

def GetContent(path,sheet=0):
    data = xlrd.open_workbook(path)
    table = data.sheets()[sheet]
    return table

def GetRowNumber(table):
    return table.nrows

def GetColNumber(table):
    return table.ncols

def GetRowValue(table,row):
    return table.row_values(row)

def GetColValue(table,col):
    return table.col_values(col)






