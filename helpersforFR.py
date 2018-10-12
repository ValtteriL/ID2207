from FinancialRequest import FinancialRequest
import database


# creat FinancialRequest

def cfr():
    print('\n##Creating new FinancialRequest##')
    EmployeeID = input('EmployeeID:')
    department = input('Department: ')
    ExtreBudget = input('ExtreBudget: ')
    target = input('The target of ExtreBudget: ')
    details = input('The More Details:')

    frrequest = FinancialRequest(EmployeeID, department, ExtreBudget, target,details)
    database.FinancialRequestlist.append(frrequest)
    print('\n')


def vfr():
    if len(database.FinancialRequestlist) > 0:
        print('\nChoose FinancialRequest to View')
        for index, request in enumerate(database.FinancialRequestlist):
            print('{}={}'.format(index, request.EmployeeID))
        choice = int(input('>'))
        if choice < len(database.FinancialRequestlist):
            print('\n## Viewing FinancialRequest##')
            database.FinancialRequestlist[choice].printFR()
        else:
            print('Invalid selection')

    else:
        print('There are no FinancialRequests!')

    print('\n')


def dfr():
    if len(database.FinancialRequestlist) > 0:
        print('\nChoose FinancialRequest to Delet')
        for index, request in enumerate(database.FinancialRequestlist):
            print('{}={}'.format(index, request.EmployeeID))
        choice = int(input('>'))
        if choice < len(database.FinancialRequestlist):
            del database.FinancialRequestlist[choice]
            print('Delet successfully!')
        else:
            print('Invalid selection')
    else:
        print('There are no FinancialRequests')


print('\n')
