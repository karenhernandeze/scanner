from table.transitions import transitions_table
from table.key import key_converter
from table.tokens import tokens_table
import os.path

# White spaces = blanks, newlines, and tabs
delim_tokens = [" ", "\n", "\t", ""]
keywords= ["int", "float", "if", "else", "read", "write", "string", "for", "while", "return", "void"]
special_symbols = ["+", "-", "*", ";", ",", "(", ")", 
                   "[", "]", "{", "}", "<", ">", "=", "!", "/", ".", '"', ]

transition_states = transitions_table()
tokens = tokens_table()
integer_table = []
float_table = []
token_ids_table = []
strings_output_table = []

string_table = []
number_table = []

output = []

error_states = [38,39,40,41]
symbols_states = [26,27,28,29,30,31,32]

def get_value(char: str) -> str:
    if char.isdigit():
        return "digit"
    elif char.isalpha():
        return "letter"
    elif char in special_symbols:
        return char 
    elif char in delim_tokens: 
        return "delim" 
    else:
        return "rare_char"

def add_to_output(token: str, type: str):
    if type == "ID": 
        del string_table[:]
        value = tokens["ID"]
        index = token_ids_table.index(token)
        output.append((value, index+1))
    elif type == "KW":
        value = tokens[str1]
        output.append(value)
        del string_table[:]
    elif type == "string":
        value = tokens["strings"]
        index = strings_output_table.index(token)
        output.append((value, index+1))
        del string_table[:]
    elif type == "num1":
        value = tokens["integer_cons"]
        index = integer_table.index(token)
        output.append((value, index+1))
        del number_table[:]
    elif type == "num2":
        value = tokens["integer_float"]
        index = float_table.index(token)
        output.append((value, index+1))
        del number_table[:]
    else:
        value = tokens[token]
        output.append(value)

if __name__ == "__main__":
    test_num = 11
    open_file = f"tests/test{test_num}.txt"
    with open(open_file, 'r', encoding='utf-8') as file:
        state = 1
        flag = 0
        i = 1
        while True:
            # print the ouput also in the next .txt file to assert true or false the tests 
            if os.path.exists(f"tests/output_results/results{test_num}.txt"):
                os.remove(f"tests/output_results/results{test_num}.txt")
            f = open(f"tests/output_results/results{test_num}.txt", "a")

            # get char to read
            char = file.read(1).lower()
            if not char: 
                if state == 7 or state == 8:
                    f.write(f"Comments not Closed. \nError in line: {i}")
                    raise Exception(f"Comments not Closed. \nError in line: {i}")
                elif state == 12:
                    f.write(f"String not Closed. \nError in line: {i}")
                    raise Exception(f"String not Closed. \nError in line: {i}")
                print('Reached end of file')
                break
                    
            # check if the char to be defined is letter, digit, delim, sp sym or rare
            transition = get_value(char) 
            # convert the char to int to be able to use the key from the transitions table
            get_int = key_converter(transition)
            # get the new state given the transition
            if state > 13:
                f.write(f"Invalid Character. \nError in line: {i}")
                raise Exception(f"Invalid Character. \nError in line: {i}")
            else:
                new_state = transition_states[state][get_int] 
                state = int(new_state)

                # delim_tokens 
                if state == 1:
                    if char == '\n':
                        i += 1
                    pass
                # read all the chars from the string 
                # if it is letter
                elif state == 9:
                    string_table.append(char)
                # integers or floats, save to table 
                elif state == 10 or state == 11 or state == 13:
                    number_table.append(char) 
                # if a string is beginning
                elif state == 12: 
                    # add all incoming strings to array, no matter if it is repetitive 
                    string_table.append(char)
                    # flag used to check if the string is closed  
                    flag = 1
                # means a string came up and has been closed 
                elif state == 14:
                    flag = 0
                    str1 = ""
                    for e in string_table:
                        str1 += e 
                    str1 = str1 + '"'
                    strings_output_table.append(str1)
                    add_to_output(str1, "string")
                    # once reached a termimal state, set state to 1 
                    state = 1
                    continue
                # if char is a special symbol 
                elif state >= 15 and state <= 25:
                    add_to_output(char, "")
                    state = 1
                    continue
                # a comment was opened and now closed, too. set flag to 0 
                elif state == 34:
                    flag = 0
                    state = 1
                    continue
                # ids or keywords 
                elif state == 35:
                    # it reached the final state of an id, check if it is keyword or ids
                    str1 = ""
                    for e in string_table:
                        str1 += e 
                    if str1 in keywords:
                        add_to_output(str1, "KW")
                    else: 
                        if str1 in token_ids_table:
                            pass 
                        else:
                            token_ids_table.append(str1)
                        # if it is an id append it to the ids table 
                        add_to_output(str1, "ID")
                    # if the string table is empty it means a special symbols has come up after inmeditaly after an id 
                    if not string_table:
                        # if something came up inmediatly after but it was a delimiter, do not add 
                        if char not in delim_tokens:
                            add_to_output(char, "")
                    state = 1
                    continue
                # integers
                elif state == 36:
                    str1 = ""
                    for e in number_table:
                        str1 += e 
                    if str1 in integer_table:
                        pass 
                    else:
                        integer_table.append(str1)
                    add_to_output(str1, "num1")
                    state = 1
                    # to add delimeters that are next to a num e.g. 4>5
                    if char not in delim_tokens:
                        add_to_output(char, "")
                    continue
                # floats
                elif state == 37:
                    str1 = ""
                    for e in number_table:
                        str1 += e 
                    if str1 in float_table:
                        pass 
                    else:
                        float_table.append(str1)
                    add_to_output(str1, "num2")
                    state = 1
                    # too add delimeters that are next to a num e.g. 4.5>5
                    if char not in delim_tokens:
                        add_to_output(char, "")
                    continue
                # case for special symbols '<' '>' '!' '='
                elif state in symbols_states:
                    if state == 26:
                        add_to_output('<=', "")
                    elif state == 27:
                        add_to_output('<', "")
                    elif state == 28:
                        add_to_output('>=', "")
                    elif state == 29:
                        add_to_output('>', "")
                    elif state == 30:
                        add_to_output('==', "")
                    elif state == 31:
                        add_to_output('=', "")
                    elif state == 32:
                        add_to_output('!=', "")
                    state = 1
                # case for the comments, check they are correctly closed flag = 1
                elif state == 7 or state == 8:
                    flag = 1
                # if something went to an error state 
                elif state in error_states:
                    if state == 38:
                        f.write(f"Invalid Character. \nError in line: {i}")
                        raise Exception(f"Invalid Character. \nError in line: {i}")
                    elif state == 39:
                        f.write(f"Invalid ID. \nError in line: {i}")
                        raise Exception(f"Invalid ID. \nError in line: {i}")
                    elif state == 40: 
                        f.write(f"Invalid Number. \nError in line: {i}")
                        raise Exception(f"Invalid Number. \nError in line: {i}")
                    elif state == 41:
                        f.write(f"Invalid String. \nError in line: {i}")
                        raise Exception(f"Invalid String. \nError in line: {i}")
                    raise Exception(f"Error in line {i}")        

        print("Scanner Output: ")
        for i in output:
            f.write(str(i)+'\n')
            print((i))
        
        j = 1
        print(f"Integer Constants Table:")
        if not integer_table:
            print("Table Empty.")
        for i in integer_table:
            f.write(f"Entry {j}: "+ str(i)+'\n')
            print(f"Entry {j}: ", i)
            j += 1

        k = 1
        print(f"Floats Constants Table:")
        if not float_table:
            print("Table Empty.")
        for fn in float_table:
            f.write(f"Entry {k}: "+ str(fn)+'\n')
            print(f"Entry {k}: ", fn)
            k += 1

        l = 1
        print(f"Token IDs Table:")
        if not token_ids_table:
            print("Table Empty.")
        for t in token_ids_table:
            f.write(f"Entry {l}: "+ t+'\n')
            print(f"Entry {l}: ", t)
            l += 1
        
        m = 1
        print("Strings Table:")
        if not strings_output_table:
            print("Table Empty.")
        for s in strings_output_table:
            f.write(f"Entry {m}: "+ s+'\n')
            print(f"Entry {m}: ", s)
            m += 1

    f.close()