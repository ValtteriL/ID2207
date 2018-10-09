from EmployeeRecord import EmployeeRecord
from helpers import cer, ver, uer, aer, rer, vemr, uemr


# initialize database
def init():

    # What each position can do
    # not completed yet
    global Privileges 
    Privileges = {
        "CSStaff": ['q', 'cer', 'ver', 'uer'],
        "CSManager":['q', 'ver', 'aer', 'rer'],
        "FManager": ['q'],
        "AManager": ['q'],
        "PManager": ['q', 'vemr'],
        "HR": ['q', 'vemr', 'uemr'],
        "Subteam": ['q']
    }

    # Available actions
    # key: (description, function)
    global Actions
    Actions = {
        "q": ("logout",None),
        "cer": ("create EventRequest", cer),
        "ver": ("view EventRequest", ver),
        "uer": ("update Eventrequest", uer),
        "aer": ("accept EventRequest", aer),
        "rer": ("reject EventRequest", rer),
        "vemr": ("view EmployeeRecord", vemr),
        "uemr": ("update EmployeeRecord", uemr)
    }

    # Create some users
    # EmployeeRecord(firname, lastname, password, position)
    global Employees
    Employees = {
        "css": EmployeeRecord("kalle", "kehveli", "secret", "CSStaff"),
        "csm": EmployeeRecord("seppo", "taalasmaa", "password", "CSManager"),
        "fm": EmployeeRecord("ismo", "laitela", "hunter", "FManager"),
        "am": EmployeeRecord("sauli", "niinistö", "12345", "AManager"),
        "pm": EmployeeRecord("sauli", "niinistö", "12345", "PManager"),
        "hr": EmployeeRecord("sauli", "niinistö", "12345", "HR"),
        "st": EmployeeRecord("sauli", "niinistö", "12345", "Subteam")

    }

    # List to hold EventRequests
    global eventRequestList
    eventRequestList = []