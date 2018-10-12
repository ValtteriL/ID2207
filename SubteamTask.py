## creat sub-team task
class SubteamTask:
    
    taskname=None
    department=None
    time=None
    details=None
    assignedTo=None

    # Constructor
    def __init__ (self,taskname,department,time,details):

        self.taskname=taskname
        self.department=department
        self.time=time
        self.details=details
        
    # Print Task
    def printtask(self):

        print('Task name:{}'.format(self.taskname))
        print('Department:{}'.format(self.department)) 
        print('Time:{}'.format(self.time))
        print('Task Details:{}'.format(self.details))
        
        if self.assignedTo:
            print('Assigned to: {} {}'.format(self.assignedTo.firstname, self.assignedTo.lastname))
