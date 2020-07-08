class A :

    def feature1(self):
        print("Feature1 is working in class A")

    def feature2(self):
        print("Feature2 is working in class A")

class D:

    def feature6(self):
        print("Feature6 is working in class D")

    def feature7(self):
        print("Feature7 is working in class D")


###Single level Inheritance
class B(A):

    def feature3(self):
        print ("Single level Inheritance")
        print("Feature3 is working in class B")

    def feature4(self):
        print ("Single level Inheritance")
        print("Feature4 is working in class B")

###ulti Level inheritance
class C(B):

    def feature5(self):
        print ("Multi level Inheritance")
        print("Feature5 is working in class C")


####Multiple Inheritance
class E(A,D):

    def feature8(self):
        print ("Multiple Inheritance")
        print("Feature8 is working in class E")

e1=E()

print ("class E")
e1.feature8()
e1.feature7()
e1.feature1()
e1.feature2()
e1.feature6()


print ("class A")
a1=A()
a1.feature1()
a1.feature2()

print ("class B")
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

print ("Class C")
c1=C()
c1.feature5()
c1.feature1()
c1.feature3()