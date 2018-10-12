from SubteamTask import SubteamTask
import database


## SubteamTask related helpers

# Create SubteamTask
def cst():
    print('\n## Creating New SubteamTask ##')

    # Create task
    taskname=input('Task Name:')
    department=input('Department:')
    time=input('Task Time:')
    details=input('Task Details:')
    task=SubteamTask(taskname,department,time,details)

    # Select EventRequest (project associated with it)
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest to add this project to")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {} hasproject: {}".format(index, request.clientname, request.project is not None))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            if not database.eventRequestList[choice].project:
                print("No project associated with this project!")
            else:
                project = database.eventRequestList[choice].project # get the project associated with this EventRequest
                project.tasks.append(task) # add task to the project
                print("\n## SubteamTask created and added to selected Project successfully ##")
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests, cannot create SubteamTask")
    print('\n')


# View SubteamTask
def vst():

    project = None

    # Select EventRequest
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {} hasproject: {}".format(index, request.clientname, request.project is not None))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            # add task to the project
            # TODO
            if not database.eventRequestList[choice].project:
                print("No project associated with this project!")
            else:
                project = database.eventRequestList[choice].project # get the project associated with this EventRequest
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests, cannot view SubteamTask")

    # Select SubteamTask
    if project:
        # there is a project
        if len(project.tasks) > 0:
            # there are tasks in this project

            print("\nChoose SubteamTask to view")

            for index, task in enumerate(project.tasks):
                print("{} = {}".format(index, task.taskname))

            choice = int(input(">"))
            if choice < len(project.tasks):
                print("\n## Viewing SubteamTask ##")
                project.tasks[choice].printtask()                    ######### does this really update it?
            else:
                print("Invalid selection")
    print('\n')


# Update existing SubteamTask
def ust():

    project = None
    chosentask = None

    # Select EventRequest
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {} hasproject: {}".format(index, request.clientname, request.project is not None))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            # add task to the project
            # TODO
            if not database.eventRequestList[choice].project:
                print("No project associated with this project!")
            else:
                project = database.eventRequestList[choice].project # get the project associated with this EventRequest
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests, cannot view SubteamTask")

    # Select SubteamTask
    if project:
        # there is a project
        if len(project.tasks) > 0:
            # there are tasks in this project

            print("\nChoose SubteamTask to view")

            for index, task in enumerate(project.tasks):
                print("{} = {}".format(index, task.taskname))

            choice = int(input(">"))
            if choice < len(project.tasks):
                chosentask = project.tasks[choice]
            else:
                print("Invalid selection")

    # Update the task
    if chosentask:
        print("\n## Updating Sub-team Task {} ##".format(choice))
        taskname = input('Task name ({}): '.format(chosentask.taskname))
        department = input('Task department ({}): '.format(chosentask.department))
        time = input('Task time ({}): '.format(chosentask.time))
        details = input('Task details ({}): '.format(chosentask.details))

        # replace the old sub-teamtask with the new data            ######### does this really update it?
        project.tasks[choice] = SubteamTask(
            c(chosentask.taskname, taskname),
            c(chosentask.department, department),
            c(chosentask.time, time),
            c(chosentask.details, details)              
        )

        print("SubteamTask successfully updated")

    print('\n')


# Assign SubteamTask
def ast():

    project = None
    chosentask = None

    # Select EventRequest
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {} hasproject: {}".format(index, request.clientname, request.project is not None))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            # add task to the project
            # TODO
            if not database.eventRequestList[choice].project:
                print("No project associated with this project!")
            else:
                project = database.eventRequestList[choice].project # get the project associated with this EventRequest
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests, cannot view SubteamTask")

    # Select SubteamTask
    if project:
        # there is a project
        if len(project.tasks) > 0:
            # there are tasks in this project

            print("\nChoose SubteamTask to assign")

            for index, task in enumerate(project.tasks):
                print("{} = {}".format(index, task.taskname))

            choice = int(input(">"))
            if choice < len(project.tasks):
                chosentask = project.tasks[choice]
            else:
                print("Invalid selection")

    # Select worker
    if chosentask:
        if len(project.workers) > 0:
            print("Choose worker to assign to")
            for index, worker in enumerate(project.workers):
                print("{} = {} {}".format(index, worker.firstname, worker.lastname))
            choice = int(input(">"))
            if choice < len(project.workers):
                chosentask.assignedTo = project.workers[choice]             ######### does this really update it?  
                print("SubteamTask assigned to the selected worker")
            else:
                print("Invalid selection!")
        else:
            print("No workers associated with this project!")

    print('\n')

# helper function to determine whether user want to change attribute or not
def c(old, new):
    if new != '':
        return new
    else:
        return old

