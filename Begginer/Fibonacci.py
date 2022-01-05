def fibonacci(n):
    '''
    Return nth Fibonacci using a recursive function
    input: 
        n:int -> Number to calculate nth Fibonacci
    output: 
        The Fibonacci value in nth number
    >>> fibonaci(5)
    5
    '''
    if n < 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


def fibonacciUpTo(n):
    '''
    Return a list where elements Fibonacci will be lower than n
    input:
        n: int -> Limit number 
    output:
        list: -> List with integer numbers Fibonacci lower than n
    >>>fibonacciUpTo(6)
    [0, 1, 1, 2, 3, 5]
    '''
    sequence = [0, 1]

    for i in range(1, n+1):
        next = sequence[-1]+sequence[-2]
        if(next > n):
            return sequence
        else:
            sequence.append(next)


def invalid(n):
    '''
    function that throws an exception if you choose a non-existent option
    '''
    raise Exception("Operation not found")


def custom_switch(n, opt="0"):
    '''
    Choose an option without use "sentence if or switch"
    input:
        n:int -> Number to use in both Fibonacci options
        opt:str -> Option selected by default selects the first option.
    output:
        Result of the selected option
    >>>custom_switch(5,"1")
    Result of the selected option
    '''
    ops = {
        "1": fibonacci,
        "2": fibonacciUpTo
    }

    func_selected = ops.get(opt, invalid)
    return func_selected(n)

############################################

'''
    1) Digit the option to use
    2) Digit the number
'''

try:
    print('''Options:
            1) Calculate nth Fibonacci
            2) List Fibonacci terms lower than n
    ''')
    opt = input('Select option: ')
    n = int(input('Digit a number upper than 0: '))
    
    if( type(n) != int or n < 1 ):
        raise Exception("The number should be upper than 0")    
    
    print(f'Result for operation # {opt} with n = {n}')
    print('>>>',custom_switch(n, opt))
except Exception as e:
    print( str(e) )
