from employee import SalrayEmployee, HourlyEmployee, CommissionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print("Current Employees:")
        for i in self.employees:
            print(i.fname, i.lname)
        print('---------------------')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('------------------------')


def main():
    my_company = Company()

    employee1 = SalrayEmployee("Aniket", "Shandilya", 20000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee("Himanshu", "Kumar", 40, 500)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee("Palkesh", "Bagi", 15000, 5, 200)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()


main()
