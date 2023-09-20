def xo(s):
    
    xNumber = 0
    oNumber = 0

    for i in s:
        if(i.lower() == 'x' ):
            xNumber += 1
        elif(i.lower() == 'o'):
            oNumber += 1
    
    return xNumber == oNumber








print(xo('xooxx'))