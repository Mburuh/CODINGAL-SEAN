class student:
    grade=11
    name="Sean"
    year='1st year'
    def Introduction(self):
        print('Hello y name is')
    def Details(self):
            print('My name is ',self.name)
            print('I am in grade',self.grade)
    def Additional(self):
        print('I am in',self.year)      
ob=student()
ob.Introduction()
ob.Details()
ob.Additional()            