#class compostition.

print('Class Composition : Instantiating one class inside another class.')
print('- When there is no inheritance relation between two classes')
print('  yet one class needs a function of other, we use class composition.')
print('\n\n')

class salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = pay*12 +bonus

    def annual_salary(self):
        return self.salary

class employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        self.pay = pay
        self.bonus = bonus

        # instantiate class salary to use its function annual_salary.
        self.obj_of_salary = salary(pay,bonus)

    def total_salary(self):
        return self.obj_of_salary.annual_salary()       #obj_of_salary is object of salary and
                                                        #can call any function of class salary.



ashu = employee('ashu',21,100000,100000)

print('Instantiating class employee and calling its function.')
#ashu is obj of employee and can call its function.
print(ashu.total_salary())
