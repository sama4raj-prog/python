class Employee:

    #Constructor:
    def __init__(self):
        print("Employee created")

    #Destructor:
    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making an object")
    obj = Employee()
    return obj

obj = create_obj()
