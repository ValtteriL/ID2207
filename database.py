from EmployeeRecord import EmployeeRecord
from helpers import cer, ver, uer, aer, rer, vemr, uemr
from helpersforRR import crr, vrr, drr
from helpersforProject import cp
from helpersforSubteamTask import cst, vst, ust, ast


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
        "PManager": ['q', 'vemr', 'crr', 'vrr', 'drr', 'cp', 'cst', 'vst', 'ust', 'ast'],
        "HR": ['q', 'vemr', 'uemr', 'vrr'],
        "Subteam": ['q', 'vst', 'ust']
    }

    # Available actions
    # key: (description, function)
    global Actions
    Actions = {
        # iteration 1
        "q": ("logout",None),
        "cer": ("create EventRequest", cer),
        "ver": ("view EventRequest", ver),
        "uer": ("update Eventrequest", uer),
        "aer": ("accept EventRequest", aer),
        "rer": ("reject EventRequest", rer),
        "vemr": ("view EmployeeRecord", vemr),
        "uemr": ("update EmployeeRecord", uemr),

        # iteration 2
        "crr": ("create ResourceRequest", crr),
        "vrr": ("view ResourceRequest", vrr),
        "drr": ("delete ResourceRequest", drr),
        "cp": ("create Project", cp),
        "cst": ("create SubteamTask", cst),
        "vst": ("view SubteamTask", vst),
        "ust": ("update SubteamTask", ust),
        "ast": ("assign SubteamTask", ast)
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

    # List to hold ResourceRequests
    global ResourceRequestList
    ResourceRequestList = []
