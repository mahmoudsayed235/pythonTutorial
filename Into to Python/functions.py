def greeting(name):
   print(f"welcome {name}")

def getName():
   
    return input("enter your name : ")
   
greeting(getName())


defaultY=3
#the function will take the first value of defaultY
def add(x,y=defaultY):
    return x+y
print(add(3))

defaultY=4
print(add(3))

lambda x,y:x*y
#lambda calling
mult=lambda x,y:x*y
print(mult(3,3))
#or
print((lambda x,y:x*y)(3,4))