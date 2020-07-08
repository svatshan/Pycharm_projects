class A:

    def show(self):
        print ("in A show")

class B(A):
##Method overriding - overriding the parent class same function
    def show(self):
        print("in B show")

a1=B()
a1.show()