from Project import Project
import database


## Project related helpers

# Create project
def cp():
    print('\n## Creating new Project ##')

    employees = [] # list to hold employees that are relate d to this project

    # select Employees
    if len(database.Employees) > 0:
        print("\nAvailable workers:")
        for key in database.Employees.keys():
            if database.Employees[key].position == 'Subteam':
                print("{} = {} {}, {}".format(key, database.Employees[key].firstname, database.Employees[key].lastname, database.Employees[key].position))
        print("Choose one at a time, q to stop.")
        while True:
            choice = input(">")
            if choice == 'q':
                break
            elif choice in database.Employees and database.Employees[choice].position == 'Subteam':
                employees.append(database.Employees[choice])
                print("Employee added.")
            else:
                print("Invalid selection!")
    else:
        print("There are no EmployeeRecords!")


    # create project with the workers
    project = Project(employees)

    # select EventRequest
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest to add this project to")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {}".format(index, request.clientname))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            database.eventRequestList[choice].project = project
            print("\n## Project created and added to selected EventRequest successfully ##")
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests, cannot create Project")

    print("\n")
