class Student:

    school= "KV"

    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return ((self.m1+self.m2+self.m3)/3)

###object method
#  #Accessor methods - Don' t change value , used only for fetch
    def get_m1(self):
        return self.m1

##Mutator Methods - change values
    def  st_m1(self,value):
        self.m1=value
###object method

###class method

    @classmethod
    def getschool(cls):
     return cls.school

##Static method

    @staticmethod
    def info():
       print ("This is Student class.. in abc module")

s1=Student(34,45,23)
s2=Student(34,54,73)

print (s1.avg())
print (s2.avg())
print (Student.getschool())
Student.info()
