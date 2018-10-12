from FinancialRequest import FinancialRequest
import database


## FinancialRequest related helpers

# Create FinancialRequest
def cfr():
    print('\n## Creating new FinancialRequest ##')
    EmployeeID = input('EmployeeID:')
    department = input('Department: ')
    ExtreBudget = input('ExtreBudget: ')
    target = input('The target of ExtreBudget: ')
    details = input('The More Details:')

    frrequest = FinancialRequest(EmployeeID, department, ExtreBudget, target,details)
    database.FinancialRequestList.append(frrequest)
    print('\n## FinancialRequest successfully created. ##')
    print('\n')


# View FinancialRequest
def vfr():
    if len(database.FinancialRequestList) > 0:
        print('\nChoose FinancialRequest to View')
        for index, request in enumerate(database.FinancialRequestList):
            print('{} = {}'.format(index, request.EmployeeID))
        choice = int(input('>'))
        if choice < len(database.FinancialRequestList):
            print('\n## Viewing FinancialRequest##')
            database.FinancialRequestList[choice].printFR()
        else:
            print('Invalid selection')

    else:
        print('There are no FinancialRequests!')

    print('\n')


# Delete FinancialRequest
def dfr():
    if len(database.FinancialRequestList) > 0:
        print('\nChoose FinancialRequest to Delete')
        for index, request in enumerate(database.FinancialRequestList):
            print('{} = {}'.format(index, request.EmployeeID))
        choice = int(input('>'))
        if choice < len(database.FinancialRequestList):
            del database.FinancialRequestList[choice]
            print('Deleted successfully!')
        else:
            print('Invalid selection')
    else:
        print('There are no FinancialRequests')

    print('\n')
