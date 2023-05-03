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

# terminal_states = [13,25,26,27,28,29,30,31,32,33,34,35,36]
# terminal_states = [13,14,15,16,17,18,19,20,21,22,23,24,25,
#                    26,27,28,29,30,31,32,33,34,35,36]
# states_checked = [4, 14,15,16,17,18,19,20,21,22,23,24]
error_states = [38,39,40,41]

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
    elif type == "num1":
        value = tokens["integer_cons"]
        output.append(value)
        del number_table[:]
    elif type == "num2":
        value = tokens["integer_float"]
        output.append(value)
        del number_table[:]
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

            # delim_tokens 
            if state == 1:
                pass
            # read all the chars from the string 
            # is letter
            if state == 9:
                string_table.append(char)
            # integers or floats, save to table 
            elif state == 10 or state == 11 or state == 13:
                number_table.append(char) 
            elif state <= 15 or state >= 25:
                if char not in delim_tokens:
                    add_to_output(char, "")
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
                    # if it is an id append it to the ids table 
                    add_to_output(str1, "ID")
                    token_ids_table.append(str1)
                # if the string table is empty it means a special symbols has come up after an id 
                if not string_table:
                    if char not in delim_tokens:
                        add_to_output(char, "")
                state = 1
                continue
            # integers
            elif state == 35:
                str1 = ""
                for e in number_table:
                    str1 += e 
                add_to_output(str1, "num1")
                integer_table.append(str1)
                state = 1
                # too add delimeters that are next to a num e.g. 4>5
                if char not in delim_tokens:
                    add_to_output(char, "")
                continue
            # floats
            elif state == 36:
                str1 = ""
                for e in number_table:
                    str1 += e 
                add_to_output(str1, "num2")
                float_table.append(str1)
                state = 1
                # too add delimeters that are next to a num e.g. 4.5>5
                if char not in delim_tokens:
                    add_to_output(char, "")
                continue
            # elif state in terminal_states:
            #     if char not in delim_tokens:
            #         add_to_output(char, "")
            #     state = 1
            #     continue
            elif state in error_states:
                print("ERROR")
            else:
                if char not in delim_tokens:
                    add_to_output(char, "")
                state = 1
                continue
            # elif state in states_checked:
            #     if char not in delim_tokens:
            #         add_to_output(char, "")
            #     state = 1
            #     continue

        for e in token_ids_table:
            print("TOEKENS: ")
            print(e)    
        for i in output:
            "OUTPUT: "
            print(i)