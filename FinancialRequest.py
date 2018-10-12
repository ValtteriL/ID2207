class FinancialRequest:

    EmployeeID=None
    department = None
    ExtreBudget = None
    target = None
    details = None

    def __init__(self, EmployeeID, department, ExtreBudget, target,details):
        self.EmployeeID = EmployeeID
        self.department = department
        self.ExtreBudget = ExtreBudget
        self.target = target
        self.details = details

    def printFR(self):
        print('EmployeeID:{}'.format(self.EmployeeID))
        print('Department{}'.format(self.department))
        print('ExtreBudget:{}'.format(self.ExtreBudget))
        print('target:{}'.format(self.target))
        print('Details={}'.format(self.details))