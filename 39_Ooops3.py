class Employ:
    no_of_leavs = 8
    # def__init__(self,name , salary ,role ):
    #     self.name =name
    #     self.salary = salary
    #     sels.role = role 


    def printdetails(self):
        return f"Name is{self.name}.Salary is{self.salary}"
harry = Employ()
rohan=Employ()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructer"

rohan.name = "Rohan"
rohan.salary = 450
rohan.role = "Student"
print(rohan.printdetails())
