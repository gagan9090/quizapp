class Find():
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print("find Area into axb",a*b)
        elif a!=None:
            print("find Area into axa",a*a)
        else:
            print("not find area")
a=Find()
a.find_area()
a.find_area(20,20)
a.find_area(30)


'''class A:
    def lock(self):
        print("lock A")
class B(A):
    def lock(self):
        super().lock()
        print("lock b")
c=B()
c.lock()'''

def sum(a,b):
    print(a+b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

def min(a,b):
    print(a-b)










