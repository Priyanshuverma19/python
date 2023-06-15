class Employ:
    no_of_leavs = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary =  asalary
        self.role = arole 


    def printdetails(self):
        return f"Name is{self.name}.Salary is{self.salary}"
    @classmethod
    def change_leaves(cls ,newleaves):
        cls.no_of_leavs = newleaves

    @classmethod
    def from_str(cls , string):
        params = string.split("-")
        return cls(params(0),params(1) ,params(2))


harry = Employ("Harry" , 255 , "Instrecter")
rohan=Employ("Rohan" , 420 , "Student")
karan = Employ.from_str("karan-333-student")
print(karan.salary)

# print(harry.no_of_leavs)
