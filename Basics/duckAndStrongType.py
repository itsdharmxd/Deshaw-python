

class  dog:
    def walk():
        print('dog is walking')
class  cat:
    def walk():
        print('cat is walking')

class  fish:
    def swim():
        print('fish is swimming')


def move(obj):
    obj.walk()

# duck typeing (passing any object)
move(cat)
move(dog)
# move(fish)     here we  cannot pass  fish


# stromg typeing
def move2(obj):
    if(hasattr(obj,'walk')):
        obj.walk()


move2(cat)
move2(dog)
move2(fish)    # here we can pass  fish


