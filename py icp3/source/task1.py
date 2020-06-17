class Employee:
    num_of_emps = 0

    def __init__(self, name, family, salary, dept):
        self.name = name
        self.family = family
        self.salary = salary
        self.dept = dept
        Employee.num_of_emps = Employee.num_of_emps + 1

    def set_age(self):
        print(self.name)

    def avg_sal(myList):
        count = 0
        sum = 0
        for x in myList:
            sum = sum + x.salary
            count = count + 1
        print('avg salary:' + str(sum / count))


class FullTime_Employee(Employee):
    def __init__(self, name, family, salary, dept, company):
        super().__init__(name, family, salary, dept)
        self.company = company

    def get_company(list_emp, name):
        for x in list_emp:
            if (name == x.name):
                print('company of ' + name + ' is: ' + x.company)
                break
            else:
                print('No emp')
                break


emp1 = Employee('emp1', 'emp1-family', 5000, 'HR')
emp2 = Employee('emp2', 'emp2-family', 10000, 'BA')

fulltimeemp1 = FullTime_Employee('femp1', 'facebookemp1-family', 12000, 'SE', 'Facebook')
fulltimeemp2 = FullTime_Employee('femp2', 'facebookemp2-family', 13000, 'SSE', 'Google')
list_femps = {fulltimeemp1, fulltimeemp2}

list_emp = {emp1, emp2}
Employee.avg_sal(list_emp)
print('num of employees:' + str(Employee.num_of_emps))
FullTime_Employee.get_company(list_femps, 'femp1')