import EmployeeClass as ec
import PayrollDeductionClass as pdc

def main():
    emp=ec.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

    deductions = []

    deductions.append(pdc.PayrollDeduction('food court', 8/14/2022, 22.5, 39119))
    deductions.append(pdc.PayrollDeduction('giftcontribution', 8/12/2022, 25.0, 58475))
    deductions.append(pdc.PayrollDeduction('food court', 8/17/2022, 15.25, 21547))
    deductions.append(pdc.PayrollDeduction('vending machine', 8/22/2022, 3.0, 58475))
    deductions.append(pdc.PayrollDeduction('vending machine', 8/5/2022, 2.75, 58475))

    netpay = emp.get_msalary()
    
    for i in deductions:
        if i.get_empID() == emp.get_idnum():
            netpay-=i.get_charge_amt()


    print('*** Employee Pay ***')
    print(f'Name: {emp.get_name()}')
    print(f'ID Number: {emp.get_idnum()}')
    print(f'Department: {emp.get_depar()}')
    print(f'Gross Pay: {"${:,.2f}".format(emp.get_msalary())}')
    print(f'Net Pay: {"${:,.2f}".format(netpay)}')

main()