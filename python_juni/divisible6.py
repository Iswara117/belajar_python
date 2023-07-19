def is_divisible_by_6(s):
    
    list = []
    for x in range(10):
               if(s.find('*') == -1):
                    return list
               else:
                    num = s.replace('*',str(int(x)))
                    if (int(num) % 6 == 0):
                        if(len(str(num)) > 1):
                            list.append(num.lstrip("0"))
                        else:
                            list.append(num) 
    
    
    return list

    # for z in range(len(list)):
    #         if(list[z] % 6 != 0):
    #                list.pop(z)
    


    # li = string_New.split(" ")
    # print(li)s

is_divisible_by_6("*")