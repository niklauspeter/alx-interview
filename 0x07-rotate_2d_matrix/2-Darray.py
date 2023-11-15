#!/usr/bin/env python3
"""
function takes in 2-d array from user
and displays it
"""

def Darr(a, b):
    output = []
    for i in range(a):
        row = []
        
        for j in range(b):
            num = int(input(f"please insert number[{0}][{j}]"))
            row.append(num)
        output.append(row)
    return output

def arrSum(m, n):
    Sum = []
    for i in range(len(m)):
        row = []
        for j in range(len(m[0])):
            row.append(m[i][j] + n[i][j])
        Sum.append(row)
    return Sum

a = int(input("enter the number of rows"))
print(a)
b = int(input("enter the number of colums"))
print(b)

print("Enter the First matrix ")
m = Darr(a,b)
print("display the first (M) matrix")  
print(m)

print("Enter the second matrix ")
n = Darr(a, b)
print("display the Second (n) matrix")  
print(n)

S = arrSum(m, n)
print(S)

