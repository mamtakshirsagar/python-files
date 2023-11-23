import sys
def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1-num2)
def mul(num1,num2):
    print(num1*num2)
def div(num1,num2):
    print(num1/num2)

num1= int(sys.argv[1])
num2=int(sys.argv[2])
add(num1,num2)
sub(num1,num2)
mul(num1,num2)
div(num1,num2)