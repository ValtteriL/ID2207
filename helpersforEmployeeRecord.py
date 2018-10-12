from EmployeeRecord import EmployeeRecord
import database


## EmployeeRecord related helpers

# View EmployeeRecord
def vemr():
    if len(database.Employees) > 0:
        print("\nChoose EmployeeRecord to view")
        for key in database.Employees.keys():
            print("{} = {} {}, {}".format(key, database.Employees[key].firstname, database.Employees[key].lastname, database.Employees[key].position))
        choice = input(">")
        if choice in database.Employees:
            print("\n## Viewing EmployeeRecord ##")
            database.Employees[choice].printDetails()
        else:
            print("Invalid selection!")
    else:
        print("There are no EmployeeRecords!")
    print("\n")

# Update EmployeeRecord
def uemr():
    if len(database.Employees) > 0:
        print("\nChoose EmployeeRecord to update or create a new one")
        for key in database.Employees.keys():
            print("{} = {} {}, {}".format(key, database.Employees[key].firstname, database.Employees[key].lastname, database.Employees[key].position))
        choice = input(">")
        if choice in database.Employees:
            # update existing record
            print("\n## Updating existing EmployeeRecord ##")
            firstname = input("firstname ({}): ".format(database.Employees[choice].firstname))
            lastname = input("lastname ({}): ".format(database.Employees[choice].lastname))
            password = input("password ({}): ".format(database.Employees[choice].password))
            position = input("position ({}): ".format(database.Employees[choice].position))

            # replace the old EmployeeRecord with the new data
            database.Employees[choice] = EmployeeRecord(
                c(database.Employees[choice].firstname, firstname),
                c(database.Employees[choice].lastname, lastname),
                c(database.Employees[choice].password, password),
                c(database.Employees[choice].position, position)
                )
        else:
            # create new record
            print("\n## Creating new EmployeeRecord ##")
            firstname = input("firstname: ")
            lastname = input("lastname: ")
            password = input("password: ")
            position = input("position: ")

            # create new EmployeeRecord with the new data
            database.Employees[choice] = EmployeeRecord(
                firstname,
                lastname,
                password,
                position
            )

    else:
        print("There are no EmployeeRecords!")
    print("\n")


# helper function to determine whether user want to change attribute or not
def c(old, new):
    if new != '':
        return new
    else:
        return old