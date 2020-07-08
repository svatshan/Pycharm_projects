##Polymorphism
#used in  Loose Coupling , Dependency Injection , Interfaces

### Polymorphism

#Duck Typing , Operator overloading , Method overloading , Method overriding

#1.Duck Typing - Object of any class and having same method

class Pycharm:

    def execute(self):
        print ("compiling and Running")

class Myeditor:

    def execute(self):
        print ("spell check")
        print ("COnventional check")
        print ("Compiling and running")

class Laptop:

    def code(self,ide):
        ide.execute()

#ide= Pycharm()
ide= Myeditor()
lap1=Laptop()
lap1.code(ide)

