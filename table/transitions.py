# import csv

# def transitions_table():
#     transition_table = []

#     # open file
#     with open('table/transitions_table.csv', encoding='utf-8-sig') as csvfile:
#         # transitions = csv.reader(csvfile, delimiter=',')

#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             transition_table.append(row)

#         # convert states to integers
#         for sub in transition_table:
#             for key in sub:
#                 sub[key] = int(sub[key])

#         # print to use in scanner.py
#         for d in transition_table:
#             print(f"{d},")

#     return transition_table

import csv

def transitions_table():
    # transition_table = []

    # open file
    with open('table/f.csv', encoding='utf-8-sig') as csvfile:
        # transitions = csv.reader(csvfile, delimiter=',')
        
        reader = csv.reader(csvfile)
        lst = list(reader)

        # for d in lst:
        #     print(f"{d},")
        return lst
# transitions_table()
