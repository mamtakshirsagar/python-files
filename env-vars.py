import sys
import os
def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    s = num1-num2
    return s
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)

num1= int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])

print(operation)

if operation == "add":
    add(num1,num2)
if operation == "sub":
    result = sub(num1,num2)
    print(result)
if operation == "mul":
    mul(num1,num2)
if operation == "div":
    div(num1,num2) 
print(os.getenv("password"))