class parent:
  def __init__(self,p):
    self.p=p

  def meth_a(self):
    print(f"p:{self.p}")

class child(parent):
  def __init__(self, p,q):
     super().__init__(p) #super() is used to call methods (especially the constructor) of the parent class from the child class
     self.q=q

  def meth_b(self):
    self.meth_a()
    print(f"q:{self.q}")

obj_c=child(100,200)
obj_c.meth_b()