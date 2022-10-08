# instance method access the instance variable of the  class


#  classmethod need cls as parameter  while static method don't need


# Accessor == getter and Mutator == setter  method
# static method  <= wh
class exp :
    dat=45
    def __init__(self):
        self._data=5

    @staticmethod
    def display(m,k):           # static  method don't  have self argument or cls
        print('static')

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,a):
        self._data=a

exp.display()



# for passing  members  between classes  we  can use STATIC METHODS


