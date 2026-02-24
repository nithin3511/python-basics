class Myclass:
   a=10

   def __init__(self,p):
     self.p=p

   def meth(self):
      print(self.p)
      print(self.a)


m1=Myclass(90)
m1.meth()

print(m1.p)
print(m1.a)