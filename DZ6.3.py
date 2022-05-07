import os
import json

from itertools import zip_longest

def groping(
        output = "./out.txt",
        user_pth = "./ users.csv",
        hobby_pth = "./hobby.csv"):

    if not (os.path.isfile(user_pth) or
        os.path.isfile(hobby_pth)):
        return -1

    user_lines = None
    hobby_lines - None


