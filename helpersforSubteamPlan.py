from SubteamPlan import SubteamPlan
import database


## SubteamPlan related helpers

# Create SubteamPlan
def csp(currentuser):

    print('\n## Creating new Sub-team plan ##')
    project = None

    # Select project (that has this user as worker)
    if len(database.eventRequestList) > 0:
        print("Choose project to create SubteamPlan for")
        for index, event in enumerate(database.eventRequestList):
            if event.project:
                # this event has project
                if currentuser in event.project.workers:
                    # this worker is in the workers of the project
                    print("{} = {}".format(index, event.eventname))

        choice = int(input('>'))
        if choice < len(database.eventRequestList) and database.eventRequestList[choice].project and currentuser in database.eventRequestList[choice].project.workers:
            project = database.eventRequestList[choice].project
        else:
            print("Invalid selection") 
    else:
        print("No EventRequests, there are thus no projects")


    # Create plan and add it to the project
    if project:
        print('\n## Creating new Sub-team plan ##')
        EmployeeID = input('EmployeeID:')
        department = input('Department: ')
        Time = input('Time: ')
        details = input('The More Details:')

        plan = SubteamPlan(EmployeeID, department, Time, details)

        # add plan to the project
        project.plans.append(plan)

    print('\n')


# View SubteamPlan
def vsp():

    print('\n## Creating new Sub-team plan ##')
    project = None


    # Select project
    if len(database.eventRequestList) > 0:
        print("Choose project to create SubteamPlan for")
        for index, event in enumerate(database.eventRequestList):
            if event.project:
                # this event has project
                print("{} = {}".format(index, event.eventname))

        choice = int(input('>'))
        if choice < len(database.eventRequestList) and database.eventRequestList[choice].project:
            project = database.eventRequestList[choice].project
        else:
            print("Invalid selection") 
    else:
        print("No EventRequests, there are thus no projects")


    # Select plan
    if project:
        if len(project.plans) > 0:
            print("Choose plan to view")
            for index, plan in enumerate(project.plans):
                print("{} = {},{}".format(index, plan.EmployeeID, plan.department))
            choice = int(input('>'))
            if choice < len(project.plans):
                print("## Viewing SubteamPlan ##")
                project.plans[choice].printFR()
            else:
                print("Invalid selection")
        else:
            print("This project has no plans")

    print('\n')
