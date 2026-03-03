class p1:
  a=10
  
  def __init__(self,p):
    self.p=p

  def meth_p(self):
    print("i am parent")
    print(f"p:{self.p}")

class p2:
  def __init__(self,q):
    self.q=q

  def meth_q(self):
    print("i am parent 2")
    print(f"q:{self.q}")

class p3:
  def __init__(self,r):
    self.r=r

  def meth_r(self):
    print("i am parent 3")
    print(f"r:{self.r}")