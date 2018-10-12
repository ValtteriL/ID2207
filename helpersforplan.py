from subteamplan import subteamplan
import database


# creat FinancialRequest

def cplan():
    print('\n##Creating new Sub-team plan##')
    EmployeeID = input('EmployeeID:')
    department = input('Department: ')
    Time = input('Time: ')
    details = input('The More Details:')

    planrequest = subteamplan(EmployeeID, department, Time, details)
    database.subteamplanlist.append(planrequest)
    print('\n')


def vplan():
    if len(database.subteamplanlist) > 0:
        print('\nChoose Sub-team Plan to View')
        for index, request in enumerate(database.subteamplanlist):
            print('{}={}'.format(index, request.EmployeeID))
        choice = int(input('>'))
        if choice < len(database.subteamplanlist):
            print('\n## Viewing Sub-team Plan##')
            database.subteamplanlist[choice].printFR()
        else:
            print('Invalid selection')

    else:
        print('There are no Sub-team Plan!')

    print('\n')





print('\n')
