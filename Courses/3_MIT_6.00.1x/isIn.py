def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return char == aStr[round(len(aStr)//2)]
    elif char < aStr[round(len(aStr)//2)]:
        aStr = aStr[0:round(len(aStr)//2)]
        return isIn(char, aStr)
    else:
        aStr = aStr[round(len(aStr))//2:len(aStr)]
        return isIn(char, aStr)