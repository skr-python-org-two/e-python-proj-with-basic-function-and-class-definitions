


class Six:
    def __init__(self,a:int,b:str):
        self.sno = a
        self.name = b


    def __call__(self,b):
        print(f"from call {b}")


    def printdetails(self):
        print(f" values are {self.sno} {self.name}")



p = Six(1,"sekhar")
p.printdetails()
p(25)
p(36)


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

    def getvalue(self):
        print(f"values are ::: {self.factor}")


double = Multiplier(2)
result = double(10)  # Calls __call__ with 10
print(result)  # Output: 20