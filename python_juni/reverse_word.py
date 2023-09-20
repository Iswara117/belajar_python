def reverse_word(s):
    
    new_list = s.split()
    reverse_list = []
    str1 = " "

    # print(len(new_list[0]))
    for i in range(len(new_list)):
        print(i)
        if(len(new_list[i]) > 0):
            reverse_list.append(new_list[i][::-1])

    


    return  (str1.join(reverse_list))

    















reverse_word("This is an example!")