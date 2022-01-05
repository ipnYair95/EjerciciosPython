
import random 
import unicodedata
import re


def transformPal(pal):
    '''
    Normalizes the string without special characters and transform to uppercase
    input: 
        pal:str -> text to normalize
    output:
        str -> normalized text
    >>> transformPal("Hello?? World_)
    Hello World
    '''
    
    try:
        pal = unicode(pal, 'utf-8')
    except NameError:  
        pass

    #here transform to utf-8 for accents as Öü
    pal = unicodedata.normalize('NFD', pal)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")
    #replaces special characters with regex with ''
    pal = re.sub('\...|\©|\.|\,|\;|\:|\-|\_|\?|\¿|\!|\¡|\{|\}|\(|\)|\$|\%|\&|\#|\"|\\|\'|\´|\<|\>|\*|\[|\]|\@','',pal)

    return pal.upper();
 

def game(itemSelected):
    '''
    Creates hangman game
        input: 
            int -> itemSelected for game
        output:
            steps in the game
    '''
    
    letters = ''    
    attempts = 5    
     
    while attempts > 0:
     
        # counter for know how many char missing
        chars_to_find = 0
        
        #show the status of the board
        for char in itemSelected:            
          
            if char in letters:                
                print(char, end =" ")
                
            else:
                print("_", end = " ")   
                #for each letter missing we increase counter
                chars_to_find += 1
                
    
        # if there are no letters missing
        if chars_to_find == 0:
            print(f'\n Winner - your word was: {itemSelected} ')
            break
        
        
        letter_user = input("\n\n Enter a letter in UPPER - you can use space char if you think it is necessary :")
        print()
        
        # we store letter in our list from inputs
        letters += letter_user
        
        # if letter is not into itemSelected we subtract one try
        if letter_user not in itemSelected:
            
            attempts -= 1           
            print("Fail")           
            # and shows remaining attempts 
            print(f'Attempts left -> {attempts}' )                       
            
            if attempts == 0:
                print(f'You loose your word was: {itemSelected} ')
    
#######

obj = {
    1 : "contries.txt",
    2 : "emotions.txt",
    3 : "fruits.txt"
}

 
try:
    lista = []
    
    print('''
          Topics....
            1) Countries
            2) Emotions
            3) Fruits
          ''')
    topic = int(input('Select your topic: '))
    print(topic)
    if( topic < 1 or topic > 3  ):
        raise Exception("Topic not found")
     
    topicText = obj.get( topic )
    #print(topicText)
    file = f'../{topicText}'
    
    f = open(file, "r")

    for x in f: 
        pal = x[0 : len(x)-1 ]
        pal = transformPal(str(pal))   
        lista.append(pal)
    
    #print(lista)
    itemSelected = random.choice(lista)
    #print(itemSelected)
    print("Game start...")
    game(itemSelected)
    
except Exception as e:
    print(e)
except FileExistsError as e:
    print("File not found")
 
 
