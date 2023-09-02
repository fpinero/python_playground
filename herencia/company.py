from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employess(self):
        print('----- Current Employees -----')
        for i in self.employees:
            print(i.fname, i.lname)
        print('----- End of the list -----')
    
    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paychek for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}') #f is for formating, first field is separator, second field is decimals for a float number
            print ("---------------------------------------")

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Trini', 'Mazo', 50000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('Sancho', 'Tai', 25, 50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Pedro', 'Valenzuela', 29000, 34, 16)
    my_company.add_employee(employee3)

    my_company.display_employess()
    my_company.pay_employees()

main()
