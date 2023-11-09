
commands = {1: 'add book', 2: 'add phone', 3: 'edit phone', 4:'add handler', 5:'greeting handler',
            6: 'search handler', 7: 'add birthday'}

var_input = 'dd pho'

if var_input in commands.values():
    print (var_input)
else:
    list_commands = []   
    for i in commands.values():
        dict_commands = {}
        for char in i:       
            if char not in dict_commands:
                dict_commands.update({char : 1})
            else:
                dict_commands[char] += 1
        list_commands.append({i:dict_commands})


    my_dict = {}
    for i in var_input:
        if i not in my_dict:
            my_dict.update({i : 1})
        else:
            my_dict[i] += 1

print(list_commands)
print(my_dict, '\n')

final = {}

for i_command in list_commands:
    result = 0
    #print (i_command)
    for i_dict in my_dict:
        for k, v in i_command.items():
            if i_dict in v:
                #print (i_command, i_dict, v, my_dict[i_dict]/v[i_dict])
                result += v[i_dict]/my_dict[i_dict]
                #print (k, i_dict, result)
                final.update({k:result})

print (max(final, key=final.get))

