


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

