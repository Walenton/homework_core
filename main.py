import re


commands = [{i : re.sub('\W|\d', '', i)}  for i in 
            ['help', 'hello', 'address', 'add', 'change', 'phone', 'search', 'birthday', 'email', 
             'show all', 'show birthdays', 'delete', 'good bye', 'close', 'exit', 'stop']]


user_input = 'dalit'


def shrink_input(user_input):
    pure_input = re.sub('[^a-zA-Z]', '', user_input)
    return pure_input


def match(pure_input):
    list_of_possible_commands = []
    var_input = shrink_input(pure_input)
    for command in commands:
        for k, v in command.items():
            if var_input in v:
                list_of_possible_commands.append(k)
    #print (f'first match: {list_of_possible_commands}')                
    return list_of_possible_commands
    #return 'no match in commands'


def regexed_input_one_d(pure_input, ind):
    a = list(pure_input)
    a[ind]='.?'
    return ''.join(a)


def one_dimensional(pure_input):
    list_of_possible_commands = []
    for command in commands:
        for k_command, v_command in command.items():
            for ind, _ in enumerate(pure_input):
                re_symbol = regexed_input_one_d(pure_input, ind)
                result = re.findall(re_symbol, v_command)
                if result and k_command not in list_of_possible_commands:
                    list_of_possible_commands.append(k_command)
    return list_of_possible_commands
                    # print (k_command, re_symbol, result, pure_input)


def regexed_input_two_d(pure_input, fixed_ind, ind):
    a = list(pure_input)
    a[fixed_ind] = '.?'
    a[ind]='.*'
    return ''.join(a)


def two_dimensional(pure_input, len_of_input):
    list_of_possible_commands = []     
    counter = 0
    while counter<len_of_input:   
        for command in commands:
            for k_command, v_command in command.items():
                for ind, _ in enumerate(pure_input):
                    re_symbol = regexed_input_two_d(pure_input, counter, ind)
                    #print(re_symbol)
                    result = re.findall(re_symbol, v_command)
                    if result and k_command not in list_of_possible_commands:
                        list_of_possible_commands.append(k_command)
                        #print (k_command, re_symbol, result, pure_input)                  
        counter+=1
    return list_of_possible_commands


def main():
    pure_input = shrink_input(user_input)
    result = match(pure_input)
    if not result:
        result = one_dimensional(pure_input)
    if not result:
        len_of_input = len(pure_input)
        if len_of_input>=5:
            result = two_dimensional(pure_input, len_of_input)  
    return result if result else 'Command not found. Try again.'


if __name__ == '__main__':
    print(main())