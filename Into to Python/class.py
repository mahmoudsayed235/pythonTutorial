class Student:
    def __init__(self,name,grades) :
        self.name=name
        self.grades=grades
    def calculateAverage(self):
        return sum(self.grades)/len(self.grades)
    



student1=Student("Madah", [20,30,40,50,60])
print(student1.calculateAverage())
print(Student.calculateAverage(student1))

print(student1.__class__)

class Garage:
    def __init__(self):
        self.cars=[]
    def __len__(self):
        return len(self.cars)
    def __getitem__(self,i):
        return self.cars[i]
    def __repr__(self):
        return f"this Garage contains {len(self.cars)} cars"
    
    def __str__(self):
        return f"Garage with {len(self.cars)} cars"
    

garage=Garage()
garage.cars.append("car1")
garage.cars.append("car2")
print(len(garage))
print(garage[0])
print(garage)