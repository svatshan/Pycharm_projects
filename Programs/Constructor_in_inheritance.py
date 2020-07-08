class A:

    def __init__(self):
        print ("in A init")

    def feature1(self):
        print("Feature1 is working in class A")

    def feature2(self):
        print("Feature2 is working in class A")

class D:

    def __init__(self):
        print ("in D init")

    def feature1(self):
        print("Feature1 is working in class D")


    def feature6(self):
        print("Feature6 is working in class D")

    def feature7(self):
        print("Feature7 is working in class D")


###MRO -Method Resolution Order
class E(A,D):

    def __init__(self):
        super().__init__()
        print ("in E init")

    def feature8(self):
        print ("Multiple Inheritance")
        print("Feature8 is working in class E")

    def feat(self):
        super().feature2()


class B(A):

    def __init__(self):
        super().__init__()
        print ("in init B")

    def feature3(self):
        print ("Single level Inheritance")
        print("Feature3 is working in class B")

    def feature4(self):
        print ("Single level Inheritance")
        print("Feature4 is working in class B")


a1=E()

## Super Class
a1.feature1()
a1.feat()
