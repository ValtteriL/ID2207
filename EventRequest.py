class EventRequest:

    # Attributes
    clientname = None
    eventname = None
    starttime = None
    endtime = None
    details = None
    budget = None

    accepted = False
    rejected = False
    
    # Constructor
    def __init__(self,clientname,eventname,starttime,endtime,details,budget):
       
        self.clientname = clientname
        self.eventname = eventname
        self.starttime = starttime
        self.endtime = endtime
        self.details = details
        self.budget = budget

    # Print EventRequest details
    def printDetails(self):
        print("Client name: {}".format(self.clientname))
        print("Event name: {}".format(self.eventname))
        print("Start time: {}".format(self.starttime))
        print("End time: {}".format(self.endtime))
        print("Details: {}".format(self.details))
        print("Budget: {}".format(self.budget))
        print("Rejected: {}".format(self.rejected))

