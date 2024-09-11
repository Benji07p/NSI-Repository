def multiplication(a,b):
    r = 0
    if a > 0 and b > 0 :
        for loop in range(b):
            r = r + a
    elif a < 0 and b < 0:
        a = -a
        b = -b
        for loop in range(b):
            r = r + a
    elif a < 0 :
        a = -a
        for loop in range(b):
            r = r + a
        r = -r
    elif b < 0 :
        b = -b
        for loop in range(a):
            r = r + b
        r = -r
    return r

def mot_possible(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for val in range(len(mot)):
        if mot_a_trous[val] != "*" and mot_a_trous[val] != mot[val]:
            return False
    return True

def inverse_chaine(mot):
    invert = ""
    for val in range(len(mot)-1, -1,  -1):
        invert = invert + mot[val]
    return invert

def est_palindrome_v1(mot):
    invert = ""
    for val in range(len(mot)-1, -1,  -1):
        invert = invert + mot[val]
    return invert == mot

def est_palindrome_v2(mot):
    return inverse_chaine(mot) == mot

def est_nbre_palindrome(num):
    num = str(num)
    return inverse_chaine(num) == num

def est_parfait(mot):
    CORRESPONDANCE = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    num = 0
    numstr = ""
    for lettre in mot:
        num = num + CORRESPONDANCE[lettre]
        numstr = numstr + str(CORRESPONDANCE[lettre])
    boolean = int(numstr)/num
    return (num, int(numstr), int(boolean)==boolean)