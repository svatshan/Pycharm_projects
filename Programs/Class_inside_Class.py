class Student:

    def __init__(self,name,rollno):

        self.name=name
        self.rollno=rollno
        self.lap1=self.Laptop()

    def  show(self):
        print (self.name , self.rollno)
         self.lap1.show()

    class Laptop:

        def __init__(self):
            self.brand = 'Dell'
            self.cpu = 'i7'
            self.ram= 8

        def show (self):
            print (self.brand,self.cpu,self.ram)

        def update(self):
            self.cpu='i5'

s1=Student('AJ',102115)
s2=Student('SRI',102116)

s1.show()
s2.lap1.update()
s2.show()