class Computer:

   def __init__(self):
       self.name="AJ"
       self.age=27

   def update(self):
       self.age=30

   def compare(self,other):
       if self.age==other.age:
           return True
       else:
           return False

c1=Computer()
c1.update()
c2=Computer()

if c1.compare(c2):
    print ("They are same")
else:
    print("They are different")

#c1.name="Sre"
#c1.age=28

#c1.update()

print(c1.name,c1.age)
print(c2.name,c2.age)