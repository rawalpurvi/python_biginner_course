# This is the function in mymodule


'''
Add all numbers from argument
'''
def addition(*args):
    
    return sum((args))


'''
Subtract two numbers
'''
def subtraction(a,b):
    
    return (a-b)

'''
Multipy all numbers from argument
'''
def multiplication(*args):

    result = 1

    for i in args:
        result *= i
    return result


'''
Divide two numbers
'''
def division(a,b):

    return (a/b)


'''
Addition of Square numbers

'''
def add_square_number(*args):
    
    square_number = lambda a : a * a
    
    square_result = 0
    
    for i in map(square_number,args):
        
        square_result += i
       
    return square_result