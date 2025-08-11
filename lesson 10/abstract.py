from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print('I can walk and run')
class Snake(Animal):
    def move(self):
        print('I can slither')
class dog(Animal):
    def move(self):
        print('I can walk and run')
class lion(Animal):
    def move(self):
        print('I can walk and run')
R=Human()
R.move()
k=Snake()
k.move()
s=dog()
s.move() 
l=lion()
l.move()                                  