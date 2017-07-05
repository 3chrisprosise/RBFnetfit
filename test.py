from Util import XLRD
import numpy

table = XLRD.GetContent('data.xlsx')

print(XLRD.GetColValue(table, 1))
print XLRD.GetColNumber(table)
print XLRD.GetRowNumber(table)

data 