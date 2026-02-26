class student:
  
  institute_name='pyspiders'
  institute_loc='btm'
  room_num=302
  class_timing='12pm-2pm'

  def __init__(self,name,age,gender,yop,degree,place,phno):
    self.name=name
    self.age=age
    self.gender=gender
    self.yop=yop
    self.degree=degree
    self.place=place
    self.phno=phno

  def details_student(self):
    print(f"name: {self.name}") 
    print(f"age: {self.age}")
    print(f"gender{self.gender}") 
    print(f"YOP:{self.yop}")
    print(f"degree:{self.degree}")
    print(f"place: {self.place}")
    print(f"phno:{self.phno}")
    print(f"institute_name:{student.institute_name}")
    print(f"institute_loc:{student.institute_loc}")
    print(f"room_num :{student.room_num}")
    print(f"class_timing:{student.class_timing}")


s1=student("nithin",21,'M','2026','cse','hyd','765980xxxx')
s1.details_student()