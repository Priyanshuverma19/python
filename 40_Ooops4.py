class Employ:
    no_of_leavs = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary =  asalary
        self.role = arole 


    def printdetails(self):
        return f"Name is{self.name}.Salary is{self.salary}"


harry = Employ("Harry" , 255 , "Instrecter")
rohan=Employ("Rohan" , 420 , "Student")


print(harry.no_of_leavs)
