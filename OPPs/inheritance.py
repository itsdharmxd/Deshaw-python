# python suppports multiple inheritance


class parent:
    def __init__(self):
        self.name='parent'

    def display1(self):
        print(self.name)

class  child(parent):
    def __init__(self):               # constructor overiding
        super().__init__()           # invoking the  parent  class
        self.sname='upadhyay'

    def display(self):
        super().display1()
        print(self.sname)


son=child()

son.display()