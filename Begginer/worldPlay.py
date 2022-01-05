import re

def a(lista):
    filterLista = [ s for s in lista if re.search("^[a-z]+ime$", s) ]
    print(filterLista)
    
def b(lista): 
    filterLista = [s for s in lista if re.search("r|s|t|l|n|e",s)]
    print( len(filterLista) )
    
def c(lista): 
    filterLista = [s for s in lista if re.search("r|s|t|l|n|e",s)]
    total = len(filterLista)
    percent = (total / len(lista)) * 100
    print( f' {percent} % ' )
    
def d(lista): 
    filterLista = [ s for s in lista if not re.search("[aeiou]",s) ]
    print( filterLista )
    
def e(lista): 
    filterLista = [ s for s in lista if re.search('^(?=\w*?a)(?=\w*?e)(?=\w*?i)(?=\w*?o)(?=\w*?u)[a-zA-Z]+$',s )  ]
    print( filterLista )
    
def efe(lista): 
    filterTen = [ s for s in lista if len(s) == 10  ]
    filterSeven = [ s for s in lista if len(s) == 7  ]
    result =  "there is more with"

    if len(filterTen) > len(filterSeven):
        result += " 10 letters"
    else:
        result += " 7 letters"

    print( f" Words with 10: { len(filterTen) } - words with 7: { len(filterSeven) } " )
    print(f"Therefore {result} ")

def g(lista):
    long_word = max(lista, key=len)
    print(long_word)
    
def h(lista):
    filterLista = []
    for i in lista:
        rever = i[::-1]
        if i == rever:
            filterLista.append(i) 
    print(filterLista)  
    
def i(lista):
    listReverse = []
    for i in lista:
        reversa = i[::-1] 
        listReverse.append(reversa)    
    print( set(lista) & set(listReverse) )
    
def j(lista):
    filterLista = [ s for s in lista if re.search("^\w*q(?!u)\w*$", s) ]
    print(filterLista)
    
def k(lista):
    filterLista = [ s for s in lista if re.search("zu", s) ]
    print(filterLista)
    
def l(lista):
    filterLista = [ s for s in lista if re.search("(?=.*z)(?=.*w)", s) ]
    print(filterLista)
    
def m(lista):
    filterLista = [ s for s in lista if re.search("^a[a-z]{2}e[a-z]{10}i$", s) ]
    print(filterLista)
    
def n(lista):
    filterLista = [ s for s in lista if re.search("^[a-z]{2}$", s) ]
    print(filterLista)
    
def o(lista):
    filterLista = []
    for i in lista:
        if( len(i) == 4 and (i[0] == i[3]) ):
            filterLista.append(i)
            
    print(filterLista)
    
def p(lista):
    filterLista = []
    for i in lista: 
        count = len([j for j in i if j in 'aeiou'])
        if( count > 8 ):
            filterLista.append(i)
            
    print(filterLista)
    
def q(lista): 
    filterLista = [ s for s in lista if re.search('^(?=\w*?a)(?=\w*?b)(?=\w*?c)(?=\w*?d)(?=\w*?e)(?=\w*?f)[a-zA-Z]+$',s )  ]
    print( filterLista )
    
def r(lista):
    filterLista = [ s for s in lista if s[0:4] == s[ len(s)-4::] and len(s) > 3 ]
    print(filterLista)
    
def s(lista):
    filterLista = {}
    for i in lista: 
        count = len([j for j in i if j in 'i'])
        if( count != 0 ): 
            filterLista[i] = count 
    print( max(filterLista, key=filterLista.get) )     

def t(lista):
    filterList = []
    for pal in lista:
        for i in range( len(pal) -1 ):
            if pal[i] == pal[i+1] and pal[i] != "l" and pal[i+1] != "l":
                filterList.append( pal )
    print(filterList)
    
def u(lista):
    filterLista = [ s for s in lista if re.search("ab", s) ]
    print(filterLista)

def v(lista):
    filterLista = [ s for s in lista if re.search("[a|e|i|o|u]{4}", s) ]
    print(filterLista)
    
def w(lista):
    filterLista = [ s for s in lista if re.search("abcd[a-z]+dcba", s) ]
    print(filterLista)
    
def ex(lista):
    filterLista = [ s for s in lista if re.search("^[a-z][a|e|i|o|u|][a-z]$", s) ]
    filSubLists = []
    
    while len( filterLista ) != 0:
                                
        pal = filterLista.pop(0)
        cI = pal[0]
        cE = pal[ len(pal) - 1 ]
        temporalArray = [pal]    
        
        for palCompare in filterLista:  
            flag = re.search(f"^{cI}[a|e|i|o|u|]{cE}$", palCompare) 
            
            if  flag != None:
                temporalArray.append( palCompare )
                
            if( len(temporalArray) == 5 ):
                break;                
            
        if( len(temporalArray) == 5 ):
            #print( temporalArray ) 
            filSubLists.append( temporalArray )
            
    print( filSubLists )
    

def invalid(lista):
    ''' 
    function that throws an exception if you choose a non-existent option
    '''
    raise Exception("Operation not found")


def custom_switch(lista, opt="0"):
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
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "f": efe,  #with f throws r :s
        "g": g,
        "h": h,
        "i": i,
        "j": j,
        "k": k,
        "l": l,
        "m": m,
        "n": n,
        "o": o,
        "p": p,
        "q": q,
        "r": r,
        "s": s,
        "t": t,
        "u": u,
        "v": v,
        "w": w,
        "x": ex
    }

    func_selected = ops.get(opt, invalid) 
    return func_selected(lista)

try:
    file = "../wordsInEnglish.txt"
    f = open(file, "r")
    lista = []

    for x in f: 
        lista.append(x[0 : len(x)-1 ])
        
        
    print('''
      
      - (a) All words ending in \"ime\".
    - (b) How many words contain at least one of the letters \"r, s, t, l, n, e\".
    - (c) The percentage of words that contain at least one of the letters \"r, s, t, l, n, e\".
    - (d) All words with no vowels.
    - (e) All words that contain every vowel.
    - (f) Whether there are more \"ten-letter\" words or \"seven-letter\" words.
    - (g) The longest word in the list.
    - (h) All palindromes.
    - (i) All words that are words in reverse, like \"rat\" and \"tar\".
    - (j) All words that contain a \"q\" that isn’t followed by a \"u\".
    - (k) All words that contain \"zu\" anywhere in the word.
    - (l) All words that contain both a \"z\" and a \"w\".
    - (m) All words whose first letter is \"a\", third letter is \"e\" and fifth letter is \"i\".
    - (n) All two-letter words.
    - (o) All four-letter words that start and end with the same letter.
    - (p) All words that contain at least nine vowels.
    - (q) All words that contain each of the letters \"a, b, c, d, e,\" and \"f\" in any order. There may be other letters in the word. Two examples are backfield and feedback.
    - (r) All words whose first four and last four letters are the same.
    - (s) The word that has the most \"i’s\".
    - (t) All words that contain double letters next to each other like \"aardvark\" or \"book\", excluding words that end in \"lly\".
    - (u) All words that contain \"ab\" in multiple places, like \"habitable\".
    - (v) All words with four or more vowels in a row.
    - (w) All words of the form \"abcd*dcba\", where \"*\" is arbitrarily long sequence of letters.
    - (x) All groups of 5 words, like \"pat pet pit pot put\", where each word is 3 letters, all words share the same first and last letters, and the middle letter runs through all 5 vowels.
      
      ''')
        
        
    findBy = input('Enter the option to filter: ')     
    custom_switch(lista,findBy)    
    
except Exception as e:
    print(e) 
finally:
    f.close();
 
    
    
