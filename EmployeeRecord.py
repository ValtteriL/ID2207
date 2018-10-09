class EmployeeRecord:
    """Class for EmployeeRecord"""

    # data stored in this class
    firstname = None
    lastname = None
    password = None
    position = None

    # Constructor
    def __init__(self, firstname, lastname, password, position):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.position = position

    # Print EmployeeRecord details
    def printDetails(self):
        print("firstname: {}".format(self.firstname))
        print("lastname: {}".format(self.lastname))
        print("position: {}".format(self.position))

