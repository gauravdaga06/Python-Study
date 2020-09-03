#Module 5 functions in python
def check(a,b):
    if(a>b):
        print('a is greeater than b')
    elif(a<b):
        print('a is less than b')
    else:
        print('a and b are equal')

a=input(print('Enter the value of a'))
b=input(print('Enter the value of b'))
check(a,b)
