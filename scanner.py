from table.transitions import transitions_table
from table.key import key_converter
from table.tokens import tokens_table

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

string_table = []
number_table = []

output = []

terminal_states = [13,25,26,27,28,29,30,31,32,33,34,35,36]
states_checked = [14,15,16,17,18,19,20,21,22,23,24]

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
    if len(string_table) != 0:
        str1 = ""
        for e in string_table:
            str1 += e 
    if type == "ID": 
        del string_table[:]
        value = tokens["ID"]
        output.append(value)
    elif type == "KW":
        value = tokens[str1]
        output.append(value)
        del string_table[:]
    else:
        value = tokens[token]
        output.append(value)

if __name__ == "__main__":
    open_file = "tests/test1.txt"
    with open(open_file, 'r', encoding='utf-8') as file:
        state = 1
        while True:
            # get char to read
            char = file.read(1).lower()
            if not char: 
                print('Reached end of file')
                break
                    
            # check if the char to be defined is letter, digit, delim, sp sym or rare
            transition = get_value(char) 
            # convert the char to int to be able to use the key from the transitions table
            get_int = key_converter(transition)
            # get the new state given the transition
            new_state = transition_states[state][get_int] 
            state = int(new_state)
            print("S: ",state)
            # delim_tokens 
            if state == 1:
                pass
            # read all the chars from the string 
            if state == 9:
                string_table.append(char)
            elif state == 10:
                integer_table.append(char) 
            elif state == 34 or state == 35:
                str1 = ""
                for e in string_table:
                    str1 += e 
                if str1 in keywords:
                    add_to_output(str1, "KW")
                else: 
                    add_to_output(str1, "ID")
                    token_ids_table.append(str1)
                state = 1
                print("VALUE")
                print(char)
                if char not in delim_tokens:
                    add_to_output(char, "")
                continue
            elif state in terminal_states:
                if state == 30:
                    print("VALUE")
                    print(char)
                    print(char[-1])
                if char not in delim_tokens:
                    add_to_output(char, "")
                # str1 = ""
                # for e in string_table:
                #     str1 += e 
                # if str1 in keywords:
                #     # keywords_table.append(str1)
                #     add_to_output(str1, "KW")
                # else: 
                #     add_to_output(str1, "ID")
                #     token_ids_table.append(str1)
                state = 1
                continue
            elif state in states_checked:
                if char not in delim_tokens:
                    add_to_output(char, "")
                # print("HERE!!!!")
                state = 1
                continue

            # elif state == 37:
            #     print("ERROR")

        for e in token_ids_table:
            print("TOEKENS: ")
            print(e)    
        for i in output:
            "OUTPUT: "
            print(i)