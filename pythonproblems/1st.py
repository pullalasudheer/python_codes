'''class grandparent():
    def displaygp(self):
        print("I am sudheer")
class parent(grandparent):
    def displayp(self):
        print("I am child")
class child(parent):
    def displayc(self):
        print("I a child")
c = child()
c.displayc()
c.displayp()
c.displaygp()
'''
'''
lass display():
    def __init__(self,a,b):
        self.__a=a
        self._b=b
class child(display):
    def output(self):
        print(self._b)
c1 = child(2,10)
c1.output()
'''
''''
class parent():
    def __init__(self,a,b):
        self.__a=a
        self._b=b
class sudheer(parent):
    def teju(self):
        print(self._b)
v1=sudheer(2,10)
v1.teju()
'''
'''def student(a,b):
    print(a+b)
v=student(2,5)
v=student("p","w")
v=student(["student","harish"],["teju","harsha"])
'''

class shape:
    def parameter(self):
        pass
class square(shape):
    def __init__(self,sides):
        self.sides=sides
    def parameter(self):
        return self.sides * 4
class2=square(4)
print(class2.parameter())