def generate_hashtag(s):
    if(len(s) == 0):
        return False
    new_list = s.split()
    result = ''
    for i in range(len(new_list)):
        result += new_list[i].capitalize()


    # result = ''
    return False if len(result) >= 140 else "#{}".format("".join(result))
    # capital








print(generate_hashtag('Mau Kamu'))