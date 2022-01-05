import re

def calculate_new_char(char, offset, limit, flag):
    '''
    Calculate de new ASCII value from char
    input:
        char:int -> char value in ASCII
        offset:int -> shift positions
        limit:int -> base if char is upper(65) or lower(97)
        flag:boolean -> true = Decode false = encode
    output:
        int -> new ASCII value
    >>>calculate_new_char(72,4,65,false) #encode char = H with offset = 4
    L
    '''
    offset = 26 - offset if flag else offset
    return (char - limit + offset) % 26 + limit


def caesar_Cipher(text, offset, flag=False):
    '''
    Encode or decode a string using only this set[A-Z] and [a-z] and ignore spaces to encode or decode
    input:
        text:str -> string to encode or decode
        offset:int -> shift positions
        flag:boolean -> true = Decode false = encode
    '''
    newText = ""
    
    regRex = re.compile('^([A-Z]|[a-z]|\s)+$')
    if( regRex.match(text) == None ):
        raise Exception("String only should be to contain [A-Z][a-z] or whitespaces")    
    
    for i in range(len(text)):
        char = text[i]

        # ignore spaces
        if(ord(char) == 32):
            newText += char
        # if char is upper or lower
        elif(char.isupper()):
            newText += chr(calculate_new_char(ord(char), offset, 65, flag))
        else:
            newText += chr(calculate_new_char(ord(char), offset, 97, flag))

    return newText

#############


def encode(states):
    '''
    Function to ask the text to encode
    input:
        states:dic -> dic to control some parameters as save encode text, offset for this text and
                        flag for sentence while    
    '''
    text = input('Insert your text to encode: ')
    offset = int(input('Digit your offset: '))
    encodeText = caesar_Cipher(text, offset)

    states['encodeText'] = encodeText
    states['offset'] = offset

    print("\n*************\n")
    print(f' Text: {text} ')
    print(f' Encode text: {encodeText} with offset {offset} ')


def decode(states):
    '''
    Function to ask what do you want to decode?
    input:
        states:dic -> dic to control some parameters as save encode text, offset for this text and
                        flag for sentence while    
    '''
    text = states['encodeText']
    offset = states['offset']

    print(f'''What do you want to decode?
        1) Decode previous text \"{text}\"
        2) Decode another text
        ''')
    opt = int(input('Choose an option: '))
    if opt == 1:
        
        if( len(text) == 0 ):
            raise Exception("There is not a previous encode text")
        
        
        textDecode = caesar_Cipher(text, offset, True)
        print("\n*************\n")
        print(f'Encode text {text} with offset {offset} ')
        print(f'Decode text: {textDecode} ')

    elif opt == 2:
        textCustom = input('Insert your text to decode: ')
        offsetCustom = int(input('Digit your offset for this text: '))
        textDecode = caesar_Cipher(textCustom, offsetCustom, True)
        print("\n*************\n")
        print(f'Encode text {textCustom} with offset {offsetCustom} ')
        print(f'Decode text: {textDecode} ')
        
    else:
        invalid(states);
        
def exit(states):
    '''
    This function change the flag in dic for to exit from while sentence
    '''
    states['flag'] = True


def invalid(states):
    print("invalida")
    return


def custom_switch(states, opt="0"):
    '''
    Choose an option without use "sentence if or switch"
    input:
        states:dic ->  states:dic -> dic to control some parameters as save encode text, offset for this text and
                        flag for sentence while    
        opt:str -> Option selected by default selects the first option.
    output:
        Result of the selected option
    >>>custom_switch(dic,"1")
    Result of the selected option
    '''
    ops = {
        "1": encode,
        "2": decode,
        "3": exit
    }

    func_selected = ops.get(opt, invalid)
    return func_selected(states)

##################


'''
    1) Choose option to encode or decode
    2) If you want encode you will insert your text to decode and shift
    3) If you want encode you will choose if you want to decode a previous encode text or
        a custom text where you know the offset
'''

states = {
    "encodeText": "",
    "offset": "",
    "flag": False
}

while not states['flag']:

    try:
        print('''What do you want to do?
                1) Encode a text
                2) Decode text
                3) Exit
                ''')

        opt = input('Choose an option: ')
        custom_switch(states, opt)

    except Exception as e:
        print(e)
        
    finally:
        print()
        
