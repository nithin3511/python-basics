class grandparent:
  a=10
  
  def __init__(self,p):
    self.p=p

  def meth_a(self):
    print("i am grand parent")
    print(f"p:{self.p}")


class parent(grandparent):
  b=20
  
  def __init__(self,p,q):
    self.q=q
    super().__init__(p)

  def meth_b(self):
    print("i am  parent")
    print(f"q:{self.q} \n p:{self.p}")


class child(parent):
    c=20
  
    def __init__(self,p,q,r):
     super().__init__(p,q)
     self.r=r
     

    def meth_c(self):
     print("i am  child")
     print(f"r:{self.r} \n q:{self.q} \n p:{self.p}")


obj_c=child(100,200,300)
obj_c.meth_a()
obj_c.meth_b()
obj_c.meth_c()