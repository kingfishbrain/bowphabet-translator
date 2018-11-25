import string
import itertools

def translate_sentence(sentence):
    word = ''
    output = ''
    for letter in sentence:
        if letter in string.ascii_letters + "'":
            word += letter
        else:
            output += translate(word) + letter
            word = ''
    output += translate(word)
    return(output)

def translate(word):
    if word == '':
        return ''
    word = replace_u(word)
    word = spread_w(word)
    word = replace_letters(word)
    word = multiply_s(word)
    word = remove_duplicates(word)
    word = swap_y_w(word)
    return word

def multiply_s(word):
    """
    s is s if the first letter of a word, ss if in the middle of a word, sss if the final letter of a word [i.e.: susurrus becomes 'swsswrwsss']

    """
    if len(word) < 2:
        return word
    word = word[0] + word[1:-1].replace('s', 'ss') + word[-1]
    word = word[0] + word[1:-1] + word[-1].replace('s', 'sss')
    return word

def replace_letters(word):
    """
    c, g, and ph become k, j, and f respectively
    x and z become yks and ss respectively 
    vowels become y

    """
    word = word.replace('c', 'k')
    word = word.replace('C', 'K')
    word = word.replace('g', 'j')
    word = word.replace('G', 'J')    
    word = word.replace('ph', 'f')
    word = word.replace('PH', 'F')    
    word = word.replace('x', 'yks')
    word = word.replace('X', 'YKS')   
    word = word.replace('z', 'ss')    
    word = word.replace('Z', 'SS')
    word = word.replace('i', 'y')
    word = word.replace('I', 'Y')    
    word = word.replace('o', 'y')
    word = word.replace('O', 'Y')
    word = word.replace('e', 'y')
    word = word.replace('E', 'Y')    
    word = word.replace('a', 'y')
    word = word.replace('A', 'Y')
    return word

def replace_u(word):
    """
    , except u which becomes w invariable

    """
    word = word.replace('u', 'w')
    word = word.replace('U', 'W')
    return word


def remove_duplicates(word):
    """ 
    duplicate letters are removed, except for w and s
    
    """
    output = word[0]
    for letter in word[1:]:
        if letter in 'wWsS' or (letter != output[-1]):
            output += letter
    return output

def spread_w(word):
    """
    when w appears beside a vowel, it spreads to adjacent vowels

    """
    if(len(word) < 2):
        return word
    if word[0] in 'wW':
        if word[1] in "aeio":
            word = word[0] + 'w' + word[2:]
        elif word[1] in "AEIO":
            word = word[0] + 'W' + word[2:]
    if word[-1] in 'wW':
        if word[-2] in 'aeio':
            word = word[:-2] + 'w' + word[-1]
        elif word[-2] in 'AEIO':
            word = word[:-2] + 'W' + word[-1]
    change_happened = True
    while(change_happened):
        change_happened = False
        for i in range(1, len(word) - 1):
            if word[i] in 'wW':
                if word[i - 1] in 'aeio':
                    word = word[:i - 1] + 'w' + word[i:]
                    change_happened = True
                elif word[i - 1] in 'AEIO':
                    word = word[:i - 1] + 'W' + word[i:]
                    change_happened = True
                if word[i + 1] in 'aeio':
                    word = word[:i + 1] + 'w' + word[i + 2:]
                    change_happened = True
                elif word[i + 1] in 'AEIO':
                    word = word[:i + 1] + 'W' + word[i + 2:]
                    change_happened = True
    return word

def swap_y_w(word):
    """
    y before w, except after w

    """
    word = word.replace('wy', 'yw')
    word = word.replace('Wy', 'Yw')
    word = word.replace('wY', 'yW')
    word = word.replace('YW', 'YW')
    word = word.replace('wyw', 'wwy')
    word = word.replace('Wyw', 'Wwy')
    word = word.replace('wYw', 'wWy')
    word = word.replace('WYw', 'WWy')
    word = word.replace('wyW', 'wwY')
    word = word.replace('WyW', 'WwY')
    word = word.replace('wYW', 'wWY')
    word = word.replace('WYW', 'WWY')
    return word
