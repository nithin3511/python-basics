from multipleInheritance import p1
from multipleInheritance import p2
from multipleInheritance import p3


class child(p1,p2,p3):
  d=40

  def __init__(self, p,q,r,s):
    self.s=s
    p1.__init__(self,p)
    p2.__init__(self,q)
    p3.__init__(self,r)

  def meth_c(self):
    self.meth_p()
    self.meth_q()
    self.meth_r()
    print('i am chid')
    print(f"s:{self.s}")

obj_c=child(100,200,300,400)
obj_c.meth_c()

