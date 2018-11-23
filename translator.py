def translate(word):
    return word

def multiply_s(word):
    """
    s is s if the first letter of a word, ss if in the middle of a word, sss if the final letter of a word [i.e.: susurrus becomes 'swsswrwsss']

    """
    word = word[0] + word[1:-1].replace('s', 'ss') + word[-1]
    word = word[0] + word[1:-1] + word[-1].replace('s', 'sss')
    return word

def replace_letters(word):
    """
    c, g, and ph become k, j, and f respectively
    x and z become yks and ss respectively 
    vowels become y, except u which becomes w invariable

    """
    word = word.replace('c', 'ph')
    word = word.replace('g', 'j')
    word = word.replace('ph', 'f')
    word = word.replace('x', 'yks')
    word = word.replace('z', 'ss')
    word = word.replace('i', 'y')
    word = word.replace('o', 'y')
    word = word.replace('e', 'y')
    word = word.replace('a', 'y')
    return word

def replace_u(word):
    word = word.replace('u', 'w')
    return word


def remove_duplicates(word):
    """ 
    duplicate letters are removed, except for w and s
    
    """
    output = word[0]
    for letter in word[1:]:
        if letter in {'w', 's'} or (letter != output[-1]):
            output += letter
    return output

def spread_w(word):
    """
    when w appears beside a vowel, it spreads to adjacent vowels

    """
    if word[0] == 'w':
        if word[1] in {'a', 'e', 'i', 'o'}:
            word = word[0] + 'w' + word[2:]
    if word[-1] == 'w':
        if word[-2] in {'a', 'e', 'i', 'o'}:
            word = word[:-2] + 'w' + word[-1]
    change_happened = True
    while(change_happened):
        change_happened = False
        for i in range(1, len(word) - 1):
            if word[i] == 'w':
                if word[i - 1] in {'a', 'e', 'i', 'o'}:
                    word = word[:i - 1] + 'w' + word[i:]
                    change_happened = True
                if word[i + 1] in {'a', 'e', 'i', 'o'}:
                    word = word[:i + 1] + 'w' + word[i + 2:]
                    change_happened = True
    return word
