# streaming the file

# picking and unpickling



import pickle

class Student:

    def __init__(self):
        self.name="dharmesh"
        self.age=22

    def disp(self):
        print(f'name {self.name} , age {self.age}')

# wb for write in binary
with open('student_object.bat','wb')  as sb:
    st=Student()
    
    # using pickle

    pickle.dump(st,sb)

    print('pickling done')

# rb for read in binary
with open('student_object.bat','rb')  as sb:
    #loading  binary file
    obj=pickle.load(sb)

    obj.disp()
    
    

    




