# def key_converter(value: str):
#     keys = {"letter": 1,
#             "digit": 2,
#             "+": 3,
#             "-": 4,
#             "*": 5,
#             ";": 6,
#             ",": 7,
#             "(": 8,
#             ")": 9,
#             "[": 10,
#             "]": 11,
#             "{": 12,
#             "}": 13,
#             "<": 14,
#             ">": 15,
#             "=": 16,
#             "!": 17,
#             "/": 18,
#             ".": 19,
#             '"': 20,
#             "delim": 21,
#             "rare_char": 22,
#             "comments": 23
#             }
#     return keys[value]


def key_converter(value: str):
    keys = {"letter": 0,
            "digit": 1,
            "+": 2,
            "-": 3,
            "*": 4,
            ";": 5,
            ",": 6,
            "(": 7,
            ")": 8,
            "[": 9,
            "]": 10,
            "{": 11,
            "}": 12,
            "<": 13,
            ">": 14,
            "=": 15,
            "!": 16,
            "/": 17,
            ".": 18,
            '"': 19,
            "delim": 20,
            "rare_char": 21,
            "comments": 22
            }
    return keys[value]