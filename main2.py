from directory1.test1 import test1
from directory2.test2 import test2
import DateTime.DateTime as dt
import sys

def main_func(username = None, level = None):
    print("Inside Component 2... Date & Time : "+str(dt()))
    if username is not None and level is not None:
        print("Uername = ", username)
        print("Level = ",level)
    else:
        print("User Details are not provided")

if __name__ == '__main__':
    arg_list = sys.argv
    print(arg_list)
    if len(arg_list) == 3:
        username = arg_list[1]
        level = arg_list[2]
        main_func(username, level)
    else:
        main_func()
