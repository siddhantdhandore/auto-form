with open ('test123.txt','r') as f:
    empty_dict={}
    string=f.readlines()
    for i in string:
        if i != '\n':
            empty_dict[i.split(':')[0].strip()]=(i.split(':')[-1])[:-1].strip()
    print(empty_dict)
print(empty_dict['username'])
