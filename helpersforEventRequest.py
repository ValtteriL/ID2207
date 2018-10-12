from EventRequest import EventRequest
import database


## EventRequest related helpers

# Create new EventRequest
# appends the new Event to the eventRequestList
def cer():
    print("\n## Creating new EventRequest ##")
    clientname = input('client name: ')
    eventname = input('eventname: ')
    starttime = input('The start time: ')
    endtime = input('The end time: ')
    details = input('The more details: ')
    budget = input('The expected budget: ')

    request = EventRequest(clientname, eventname, starttime, endtime, details, budget)
    database.eventRequestList.append(request)
    print("\n")


# View EventRequest
def ver():
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest to view")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {}".format(index, request.clientname))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            print("\n## Viewing EventRequest ##")
            database.eventRequestList[choice].printDetails()
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests!")
    print("\n")


# Update existing EventRequest
def uer():
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest to update")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {}".format(index, request.clientname))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):

            # Prompt user to change information. If user simply presses enter, old value is kept
            print("\n## Updating EventRequest {} ##".format(choice))
            clientname = input('client name ({}): '.format(database.eventRequestList[choice].clientname))
            eventname = input('eventname ({}): '.format(database.eventRequestList[choice].eventname))
            starttime = input('The start time ({}): '.format(database.eventRequestList[choice].starttime))
            endtime = input('The end time ({}): '.format(database.eventRequestList[choice].endtime))
            details = input('The more details ({}): '.format(database.eventRequestList[choice].details))
            budget = input('The expected budget ({}): '.format(database.eventRequestList[choice].budget))

            # replace the old EventRequest with the new data
            database.eventRequestList[choice] = EventRequest(
                c(database.eventRequestList[choice].clientname, clientname),
                c(database.eventRequestList[choice].eventname, eventname),
                c(database.eventRequestList[choice].starttime, starttime),
                c(database.eventRequestList[choice].endtime, endtime),
                c(database.eventRequestList[choice].details, details),
                c(database.eventRequestList[choice].budget, budget)
                )

        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests!")
    print("\n")

# helper function to determine whether user want to change attribute or not
def c(old, new):
    if new != '':
        return new
    else:
        return old


# Accept EventRequest
def aer():
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest to accept")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {}".format(index, request.clientname))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            if not database.eventRequestList[choice].rejected:
                database.eventRequestList[choice].accepted = True
                print("\n## EventRequest accepted ##")
            else:
                print("This EventRequest has been Rejected!")
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests!")
    print("\n")


# Reject EventRequest
def rer():
    if len(database.eventRequestList) > 0:
        print("\nChoose EventRequest to reject")
        for index, request in enumerate(database.eventRequestList):
            print("{} = {}".format(index, request.clientname))
        choice = int(input(">"))
        if choice < len(database.eventRequestList):
            database.eventRequestList[choice].rejected = True
            print("\n## EventRequest rejected ##")
        else:
            print("Invalid selection!")
    else:
        print("There are no EventRequests!")
    print("\n")