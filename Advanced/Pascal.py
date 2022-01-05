def PascalTriangle(n):
    '''
        fuction that calculates pascal using indexes that pount
        input: 
            n -> number of rows
        output:
            triangle        
    '''
    res = [[1]]
    for line in range(2, n+2):
        newline = [1]
        
        #we go through the previous row to add
        for i in range(1, line-1):
            newline.append(res[-1][i-1] + res[-1][i])
        newline.append(1)
        res.append(newline)
    return res

#############################

try:    
    
    n = 0
    n = int(input('Enter the rows to calculate: '))

    if( n <= 0 or type(n) != int ):
        raise Exception("Invalid value")
        

    list1 = PascalTriangle(n)
    for i in range(len(list1)):
        x = str( list1[i] ).center(n*n, " ")
        print(  x )      
    
except Exception as e:
    print(e)
    