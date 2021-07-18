from directory1.test1 import test1
from directory2.test2 import test2

def main_func():
    print("Inside test")
    op = test1()
    op = test2()

if __name__ == '__main__':
   main_func()

#C:\Users\ketan\D\Projects\Python_Workspace\Test_kubeflow_python