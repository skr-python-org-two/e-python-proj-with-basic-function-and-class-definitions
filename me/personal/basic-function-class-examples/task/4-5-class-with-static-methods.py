


""
"""
    4. class with static methods (with args and without args) , static variables donot exist 
"""
class Two:

    def __init__(self,a:str , b:int):
        self.name = a  # instance variable
        self.age = b

    def voteEligibility(self): # instance method
        if self.age > 18 :
            print("eligible for vote")
        else:
            print(f"{self.name} not eligible for vote")


    """
        Static methods without-arguments (description) and with-arguments (wishIndividual)
    """


    @staticmethod
    def description():
        print(" Gives information abut vote eligibility")


    @staticmethod
    def wishIndividual(name: str , message: str ):
        print(f"Hi {name} . {message}")



if __name__ == "__main__":
    p = Two("sekhar",56)
    Two.description() # accessing static method using ClassName
    p.voteEligibility()
    p.description() # accessing static method using object

    Two.wishIndividual("sekhar" , "how are you")
    p.wishIndividual("jagadeesh" , "Iam fine")