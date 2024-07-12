


""
"""
    4. class with custom constructor 
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





if __name__ == "__main__":
    p = Two("sekhar",56)
    p.voteEligibility()
