# This is a demo for Python class
#import convertor
from convertor import kg_to_lbs
from app import find_max
import ecommerce.shipping
# from ecommerce.shipping import cal_shipping

ecommerce.shipping.calc_shipping()

numbers = [1, 2, 3, 0]
print(find_max(numbers))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(1,2)
point1.x = 10
point1.y = 20
print(point1.x)
point1.move()
point1.draw()

point2 = Point(1,2)
print(point2.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')

person = Person("tian nan")
person.talk()


# demo for inheritance /  do not repeat yourself
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("cat being annoying")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.be_annoying()


#print(convertor.kg_to_lbs(1))
print(kg_to_lbs(0.45))