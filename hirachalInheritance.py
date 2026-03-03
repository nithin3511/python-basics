class parent:
  def __init__(self,p):
    self.p=p

  def meth_p(self):
    print("i am parent")


class c1(parent):

  def __init__(self, p,a):
    super().__init__(p)
    self.a=a

  def meth_a(self):
    print("i am child 1")

class c2(parent):
  
  def __init__(self, p,b):
    super().__init__(p)
    self.b=b

  def meth_b(self):
    print("i am child 2")

class c3(parent):
  def __init__(self, p,c):
    super().__init__(p)
    self.c=c

  def meth_c(self):
    print("i am child 3")

obj_c1=c1(100,200)
obj_c1.meth_a()
obj_c2=c2(101,300)
obj_c2.meth_b()
obj_c3=c3(103,400)
obj_c3.meth_c()