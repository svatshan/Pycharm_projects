class Student:

    def __init__(self,m1,m2):

        self.m1=m1
        self.m2=m2

##Method overriding - Setting the paramters as none
    def sum(self,a=None,b=None,c=None):

        s= 0
        if a!=None and b!=None and c!=None:
            s=a+b+c+s1.m2
        elif a!=None and b!=None:
            s = a+b+s1.m1
        else:
            s=a

        return s

s1=Student(35,45)
print(s1.sum(9))
