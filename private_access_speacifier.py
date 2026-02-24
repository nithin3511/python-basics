class Myclass:
    __a=10
    def __init__(self,p):
        self.__p=p

    def meth(self):
        print(self.__p)
        print(self.__a)

m1=Myclass(90)
m1.meth()