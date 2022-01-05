def list_of_lists(list, n):
    '''
    Function that slices the list in sublist using n as limit
    input:
        list: list -> list for divide
        n:int -> limit of elements in each sublist
    output:
        list -> list of list
    >>>list_of_list(list,4)
    [[1, 2, 3, 4], [4, 5, 7, 8], [9]]
    '''
    newList = []
    for i in range(0, len(list), n):
        newList.append(list[i:(i+n)])

    return newList

################

'''
    1) Digit the number of elements for the sublists
'''

n = 0
lista = [1, 2, 3, 4, 4, 5, 7, 8, 9]

try:
    n = int( input('Digit the number of elements for the sublist: ') )
    if( type(n) != int  ):
        raise Exception('Invalid value')
    elif n >= len(lista) or n < 2:
        raise Exception('n should be lower than length of list and greather than 1')
    else:
        print( list_of_lists(lista,n) )
except Exception as e:
    print(e)
