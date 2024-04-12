# 多态

class Animal:
    def speak(self):
        print("所有的动物都会叫")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Sheep(Animal):
    def speak(self):
        print("咩咩咩")


def speak(Animal):
    Animal.speak()


dog = Dog()
# dog.speak()

cat = Cat()
# cat.speak()

sheep = Sheep()
# sheep.speak()

speak(dog)
speak(cat)
speak(sheep)

print(len('abb'))
print(len([1, 3, 1, 4]))
print(len(('d', 'e', 'x')))
print(len({'name': 'wutinghan', 'age': 23}))

