def solution(s):
    string = ''
    st = ''
    
    for i in s:
        if st + i in 'abcdefghijklmnopqrstuvwxyz':
            st += i
        else:
            string += st[::-1]
            st = i
            
    return string + st[::-1]