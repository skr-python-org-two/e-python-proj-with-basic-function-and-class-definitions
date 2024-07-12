


""
"""
    6. class with class-variables,class-methods and instance-variables,instance-methods 
"""
class Three:
    var_a = "your name"
    var_b = "your age"

    def __init__(self,a:str , b:int):
        self.name = a  # instance variable
        self.age = b

    def voteEligibility(self): # instance method
        if self.age > 18 :
            print("eligible for vote")
        else:
            print(f"{self.name} not eligible for vote")


    """
        Class methods without-arguments (description) and with-arguments (wishIndividual)
    """


    @classmethod
    def description(cls):
        print(" Gives information abut vote eligibility")


    @classmethod
    def wishIndividual(cls , name: str , message: str ):
        print(f"Hi {name} . {message} . May i know your {cls.var_a} {cls.var_b}")



if __name__ == "__main__":

    Three.description() # accessing class method using ClassName
    Three.wishIndividual("dummy" , "how are you") # accessing class method using ClassName
    print("value of var_a is ::: ",Three.var_a) # accessing class variables using class name
    print("value of var_b is ::: ",Three.var_b) # accessing class variables using class name
    p = Three("sekhar",56)
    p.voteEligibility()
    p.description() # accessing class method using object
    p.wishIndividual("dummy" , "how are you") # accessing class method using object
    print("value of var_a is ::: ",p.var_a) # accessing class variables using object
    print("value of var_b is ::: ",p.var_b) # accessing class variables using object

    print("######################################################################################")
    Three.var_a = "MY NAME"
    Three.var_b = "MY AGE"
    p = Three("sekhar", 56)
    p.voteEligibility()
    p.wishIndividual("tommy","how are you")
    print("value of var_a is ::: ",Three.var_a) # accessing class variables using object
    print("value of var_b is ::: ",Three.var_b) # accessing class variables using object
    print("value of var_a is ::: ",p.var_a) # accessing class variables using object
    print("value of var_b is ::: ",p.var_b) # accessing class variables using object

