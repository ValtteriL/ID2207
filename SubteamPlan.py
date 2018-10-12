class SubteamPlan:

    EmployeeID=None
    department = None
    Time=None
    details = None

    def __init__(self, EmployeeID, department, Time, details):
        self.EmployeeID = EmployeeID
        self.department = department
        self.Time = Time
        self.details = details

    def printFR(self):
        print('EmployeeID:{}'.format(self.EmployeeID))
        print('Department{}'.format(self.department))
        print('Time:{}'.format(self.Time))
        print('Details={}'.format(self.details))