
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")

class Dog(Animal):
    def __init__(self, name, hususiyat):
        super().__init__(name)
        self.hususiyat = hususiyat


    def speak(self):
        super().speak()
        print("vov vov ....")

d = Dog("bobik", "4 ayaqi boo")
d.speak()

w = Wallet(50)
res = w.pay(100)
print(res.ok, res.message)


class Persoh:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

p = Persoh("sara", 20)
print((p.age))
print(p.name)

class person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

p = person("sara", 20)
print(p.age)

