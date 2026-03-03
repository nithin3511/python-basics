class A:
  a=10
  def __init__(self,p):
    self.p=p

  def meth_a(self):
    print(f"p:{self.p}")

class B(A):
  b=10
  def __init__(self, p,q):
    self.q=q
    super().__init__(p)

  def meth_b(self):
    self.meth_a
    print(f"q:{self.q}")

class C(B):
  c=30
  def __init__(self, p,q,r):
    self.r=r
    super().__init__(p,q)

  def meth_c(self):
    self.meth_b
    print(f"r:{self.r}")
    
class E:
  E=40

  def __init__(self,t):
    self.t=t

  def meth_e(self):
    print(f"t:{self.t}") 

class D(C,E):
   d=50

   def __init__(self, p, q, r,t,s):
     super().__init__(p, q, r)
     E.__init__(self,t)
     self.s=s

   def meth_d(self):
     self.meth_c()
     self.meth_e()


class E()   