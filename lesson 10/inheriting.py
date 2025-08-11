class buyer(object):
    def __init__(self,name,age,Idnumber,height):     
     self.idnumber=Idnumber
     self.age=age
     self.height=height
     self.name=name 
    def display(self):
       print('Name:',self.name)
       print('Age:',self.age)
       print('Idnumber:',self.idnumber)
       print('Height:',self.height)

class seller(buyer):
   def __init__(self,idnumber,height,name,age):
      super().__init__(age,idnumber,height,name)
q=seller(20,'12345',5.6,'John Doe')
q.display()
      
            
    