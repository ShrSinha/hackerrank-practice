"""Transpose row to column.

Inputs:
    Space separated row of integers, with each row on a new line.

"""
# Time Complexity: O(nm)
import sys
matrix = []
while True:
    try:
        matrix.append( list( map(int,input().strip().split()) ) )
    except EOFError:          
        break

print(list((zip(*matrix))))