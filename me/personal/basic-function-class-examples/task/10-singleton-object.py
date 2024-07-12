

""""""

"""
    SingletonClass with no args
"""
class Singleton:
    # Created a private variable
    __ins = None

    # Defined the __new__ method
    def __new__(cls):
        if cls.__ins is None:
            print("Instance creating...")
            cls.__ins = super().__new__(cls)
        return cls.__ins


    def __init__(self):
        pass

    def getvals(self):
        print(f"details are {obj1} , {obj2} , {obj3}")


# Creating object
obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton()
print(obj1)
print(obj2)
print(obj3)



"""
    SingletonClass with  args
"""
class SingletonTwo:
    # Created a private variable
    __ins = None

    # Defined the __new__ method
    def __new__(cls,arg_a:int ,arg_b:str , arg_c:str):
        if cls.__ins is None:
            print("Instance creating...")
            cls.__ins = super(SingletonTwo,cls).__new__(cls)
        return cls.__ins

    def __init__(self,arg_a:int ,arg_b:str , arg_c:str):
        self.sno =arg_a
        self.firstname = arg_b
        self.lastname = arg_c

    def printDetails(self):
        print(f"My name is {self.firstname} {self.lastname}")


# Creating object
obj1 = SingletonTwo(1,"sekhar","talupula")
print(obj1.printDetails())

