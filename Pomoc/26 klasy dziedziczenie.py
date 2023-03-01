class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print('How How')

class Wolf(Dog):
    def getVoice(self):
        print('Jestem wilkiem')
        super().voice()

dog = Dog('Max', 10)
print(dog.name)
print(dog.age)
dog.voice()

class Cat(Animal):
    def getVoice(self):
        print('Miau miau')

cat = Cat('Diament', 12)
print(cat.name)
cat.getVoice()

wolf = Wolf('Geralt', 55)
wolf.getVoice()
print(wolf.name)