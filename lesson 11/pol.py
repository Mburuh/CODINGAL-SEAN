class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'I am a cat.My name is {self.name} I am {self.age} years old')
    def make_sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print(f'I am a dog.My name is {self.name} I am {self.age} years old')
    def make_sound(self):
        print("bark, gugu") 
cat1=cat('Tom',3)
dog1=dog('Jerry',2)
for animal in (cat1,dog1):  
    animal.make_sound()
    animal.intro()
