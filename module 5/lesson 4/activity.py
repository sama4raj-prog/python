class myclass:

    #private variable
    __privateVar = 27

    #private method
    def __privateMethod(self):
        print("I'm inside the myclass.")

    #Public method
    def hello(self):
        print(myclass.__privateVar)


ob = myclass()
ob.hello()
ob.__privateMethod() 