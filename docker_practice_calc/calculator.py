class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a+self.b

    def subtract(self):
        return self.a-self.b

    def division(self):
        return self.a/self.b

    def multiply (self):
        return self.a*self.b
    
    def sqrt (self):
        return self.a**0.5
    
if __name__ == "__main__":
    myCalc = Calculator(a=435,b=2)
    print(myCalc.sqrt())
    