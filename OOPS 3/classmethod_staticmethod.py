# classmethod, classmethod Constructor and staticmethod
    
class student:
    # class attributes
    s_id = 1001
    all_students = []
    # default constructor
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.s_id = student.s_id
        student.s_id += 1
        student.all_students.append(self)

    # named constructor
    @classmethod
    def noLname(cls,fname):
        return cls(fname,"")
    
    def printfname(self):
        print(f"First Name: {self.fname}")
        
    def printlname(self):
        print(f"Last Name: {self.lname}")
        
    def printId(self):
        print(f"Id: {self.s_id}")

    @classmethod
    def printStudents(cls):
        print(f"Students: {cls.all_students}")

    # has no connection with calss or instance variable.
    @staticmethod
    def collegefname():
        print("College Name: Terna Engineering College.")

if __name__ == "__main__":
    ashu = student("Ashu", "Tiwari")
    ashu.printfname()
    ashu.printlname()
    ashu.printId()
    #classmethod constructor
    payal = student.noLname("Payal")
    payal.printfname()
    payal.printlname()
    payal.printId()    
    #class method
    student.printStudents()
    #static method
    student.collegefname()





