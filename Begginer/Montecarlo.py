import random
 
def calculate(n):
    '''
    Calculates the PI estimation using Monte Carlo
    input:
        n:int -> Shooting points in the zone
    output:
        Pi estimacion: float
    >>>calculate(3)
    3.333 - Probabilistic result
    '''
    count = 0
    for i in range(n):
        
        #throws a point using x^2 + y^2
        x = random.random()        
        y = random.random()    
        throw_point = pow(x,2) + pow(y,2)
        
        #if point fell into circle increase we success cases
        if throw_point < 1:
            count += 1
    #using count/n = pi / 4 will be get an estimation
    return [4*(count/n),count]

############################################

'''
    1) Digit the number of shoots to use
'''
 
try:
    n = int( input('Digit the number of shooting upper than 2: ') ) 
    if type(n) != int or n < 2:
        raise Exception('Invalid value')
    
    result = calculate(n) 
    print( f'The PI estimation for {n} shoots is: {result[0]} with {result[1]} success cases ')
    
except Exception as e:
    print( str(e) )

 
