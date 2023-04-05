class MyCustomeError(TypeError):
    def __init__(self, message,code):
        super().__init__(f"Error code {code} : {message}")
        self.code=code

    


class Student:
    def __init__(self,name) :
        self.name=name
    def setName(self,name):
        if(any(char.isdigit() for char in name)):
            raise ValueError("invalid value")
        else:
            self.name=name

student1=Student("ahmed")

try:
    student1.setName("a7med")
except ValueError:
    print("value error")

else:
    print("no errors")
finally:
    print("done")
#raise MyCustomeError("Authorization Error",400)
