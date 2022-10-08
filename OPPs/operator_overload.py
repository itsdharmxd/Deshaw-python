class num:
    def __init__(self,val):
        self.val=val

    def __add__(self,other):
        self.val+=other.val

num1,num2 =num(5), num(4)

num1+num2

print(num1.val)