class Myclass:
   _a=10
   def __init__(self,p):
      self._p=p

   def meth(self):
      print(self._p)
      print(self._a)
      
m1=Myclass(90)
m1.meth()

print(m1._p)
print(Myclass._a)