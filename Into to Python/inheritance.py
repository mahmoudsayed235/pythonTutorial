class Student:
    def __init__(self,name,school) :
        self.name=name
        self.school=school
        self.marks=[]
    def calculateAverage(self):
        return sum(self.marks)/len(self.marks)
   
class WorkingStudent(Student):
    def __init__(self, name, school,salary):
        super().__init__(name, school)
        self.salary=salary
    @property
    def weeklySalary(self):
        return self.salary/4

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

class Bar:
    @staticmethod
    def hi():
        print("hello there!")


class FixedFloat:
    def __init__(self,amount) :
        self.amount=amount
    def __repr__(self):
        return f"<fixedFloat {self.amount:.2f}"
    @staticmethod
    def fromSum(value1,value2):
        return FixedFloat(value1+value2)
    @classmethod
    def fromSum(cls,value1,value2):
        return cls(value1+value2)


class Dollar(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol="$"

    def __repr__(self):
        return f"<Dollar {self.amount:.2f} {self.symbol}"
   
        





print(Dollar.fromSum(1.2,2.3))


student1=WorkingStudent("Mahmoud","Imbaba",1600)
student1.marks.append(20)
student1.marks.append(40)
print(student1.calculateAverage())
print(student1.weeklySalary)

foo=Foo()
foo.hi()
Bar.hi()





