class parent:
   a=10
   def meth_a(self):
      print("i am parent class method")

class child(parent):
   b=20
   def meth_b(self):
      print("i am child class method")

#print(dir(parent)) #It returns a list of all attributes and methods of an object.
#print(dir(child)) #It returns a list of all attributes and methods of an object.

obj_p=parent()
obj_p.meth_a()
#obj_p.meth_b()  #attribute error

obj_c=child()
obj_c.meth_a() 
obj_c.meth_b()

# a child can access all properties of parent excppt private members