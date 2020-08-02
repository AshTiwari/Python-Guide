#class aggregation.

print('Class Aggregation : Passing object of one calss to another class.')
print('- Similar to class composition but in here,')
print('  instead of instantiating object of one class inside another calss')
print('  we create object outside and pass it to other object.')
print('\n\n')


class salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = pay*12 +bonus

    def annual_salary(self):
        return self.salary

class employee:
    def __init__(self,name,age,salary_obj):
        self.name = name
        self.age = age

        # instantiate class salary to use its function annual_salary.
        self.obj_of_salary = salary_obj

    def total_salary(self):
        return self.obj_of_salary.annual_salary()       #obj_of_salary is object of salary and
                                                        #can call any function of class salary.

salary_obj = salary(100000,100000)

ashu = employee('ashu',21,salary_obj)

print('Instantiating class employee and calling its function.')
#ashu is obj of employee and can call its function.
print(ashu.total_salary())


