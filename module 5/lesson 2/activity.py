class IOString():
    #contructer
    def __init__(self):
        self.str1 = ""

        #method to get input from user
    def get_string(self):
        self.str1 = input("Enter a word: ")

        #method to print the string in upper case
    def print_string(self):
        print("Result: ", self.str1.upper())

ob = IOString()
ob.get_string()
ob.print_string()