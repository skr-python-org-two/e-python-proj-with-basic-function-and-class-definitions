

""
"""
    3. class with instance variables and methods
"""
class One:
    def __init__(self,a:str , b:int):
        self.name = a  # instance variable
        self.age = b

    def voteEligibility(self): # instance method
        if self.age > 18 :
            print("eligible for vote")
        else:
            print(f"{self.name} not eligible for vote")


if __name__ == "__main__":
    m = One("Sekhar" , 25)
    n = One("Jagadeesh" , 17)

    print(m.__dict__)
    m.voteEligibility()

    print(n.__dict__)
    n.voteEligibility()




