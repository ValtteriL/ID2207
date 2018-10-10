from subteamtask import subteamtask
import database

def cstt():
    print('\n##Creating New Sub-team Task##')

    taskname=input('Task Name:')
    department=input('Department:')
    time=input('Task Time:')
    details=input('Task Details:')

    task=subteamtask(taskname,department,time,details)
    database.subteamtasklist.append(task)
    print('\n')

def vstt():
    if len(database.subteamtasklist)>0:
        print('\nChoose Sub-team Task to View')
        for index ,items in enumerate (database.subteamtasklist):
            print('{}={}'.format(index,items.taskname))
        choice=int(input('>'))
        if choice<len(database.subteamtasklist):
            print('\n## Viewing Sub-team Task##')
            database.subteamtasklist[choice].printtask()
        else:
            print('Invalid selection')

    else:
        print('There are no Sub-team Task!')

    print('\n')

# Update existing Sub-team Task
def ustt():
    if len(database.subteamtasklist) > 0:
        print("\nChoose Sub-team Task to update")
        for index, items in enumerate(database.subteamtasklist):
            print("{} = {}".format(index, items.taskname))
        choice = int(input(">"))
        if choice < len(database.subteamtasklist):

            # Prompt user to change information. If user simply presses enter, old value is kept
            print("\n## Updating Sub-team Task {} ##".format(choice))
            taskname = input('Task Name ({}): '.format(database.subteamtasklist[choice].taskname))
            department = input('Task Name ({}): '.format(database.subteamtasklist[choice].department))
            time = input('Task Name ({}): '.format(database.subteamtasklist[choice].time))
            details = input('Task Name ({}): '.format(database.subteamtasklist[choice].details))
            
           

            # replace the old sub-teamtask with the new data
            database.subteamtasklist[choice] = subteamtask(
                c(database.subteamtasklist[choice].taskname, taskname),
                c(database.subteamtasklist[choice].department, department),
                c(database.subteamtasklist[choice].time, time),
                c(database.subteamtasklist[choice].details, details)        
                )

        else:
            print("Invalid selection!")
    else:
        print("There are no Sub-team Task!")
    print("\n")

# helper function to determine whether user want to change attribute or not
def c(old, new):
    if new != '':
        return new
    else:
        return old

