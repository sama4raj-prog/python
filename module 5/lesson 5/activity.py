from abc import ABC, abstractmethod

#abstract class
class Absclass(ABC):

    def print(self,x):
        print("Passed value is: ",x)

    @abstractmethod
    def task(self):
        print("We are inside an abstract method.")


class test_class(Absclass):
    def task(self):
        print("We are inside the test class.")

ob = test_class()
ob.task()
ob.print(100)