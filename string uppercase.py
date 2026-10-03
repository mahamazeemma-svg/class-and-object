class IOstring:
    def __init__(self):
        self.str1=""

    def get_string(self):
        self.str1=(input("enter a string"))

    def print_string(self):
        print("string is",self.str1.upper())

str = IOstring()
str.get_string()
str.print_string()