from EmployeeRecord import EmployeeRecord
from helpersforEventRequest import cer, ver, uer, aer, rer
from helpersforEmployeeRecord import vemr, uemr
from helpersforResourceRequest import crr, vrr, drr
from helpersforProject import cp
from helpersforSubteamTask import cst, vst, ust, ast
from helpersforFinancialRequest import cfr, vfr, dfr
from helpersforSubteamPlan import csp, vsp


# initialize database
def init():

    # What each position can do
    global Privileges 
    Privileges = {
        "CSStaff": ['q', 'cer', 'ver', 'uer'],
        "CSManager":['q', 'ver', 'aer', 'rer'],
        "FManager": ['q', 'ver', 'vfr', 'dfr'],
        "AManager": ['q', 'ver', 'aer', 'rer', 'uer'],
        "PManager": ['q', 'ver', 'vemr', 'crr', 'vrr', 'drr', 'cp', 'cst', 'vst', 'ust', 'ast', 'vfr', 'vsp'],
        "HR": ['q', 'vemr', 'uemr', 'vrr'],
        "Subteam": ['q', 'vst', 'ust', 'cfr', 'csp']
    }

    # Available actions
    # key: (description, function)
    global Actions
    Actions = {
        # iteration 1
        "q": ("logout", None),
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
        "ast": ("assign SubteamTask", ast),

        # iteration 3
        "cfr": ("create FinancialRequest", cfr),
        "vfr": ("view FinancialRequest", vfr),
        "dfr": ("delete FinancialRequest", dfr),
        "csp": ("create SubteamPlan", csp),
        "vsp": ("view Subteamplan", vsp)
    }

    # Create some users
    # EmployeeRecord(firname, lastname, password, position)
    global Employees
    Employees = {

        # higher ranked employees
        "css": EmployeeRecord("John", "Doe", "12345", "CSStaff"),
        "csm": EmployeeRecord("Lisa", "Jones", "12345", "CSManager"),
        "fm": EmployeeRecord("Peter", "Parker", "12345", "FManager"),
        "am": EmployeeRecord("Mary", "Jane", "12345", "AManager"),
        "pm": EmployeeRecord("Qwen", "Stefani", "12345", "PManager"),
        "hr": EmployeeRecord("Donald", "Trump", "12345", "HR"),

        # some plain workers
        "st1": EmployeeRecord("Alfred", "King", "12345", "Subteam"),
        "st2": EmployeeRecord("Slave", "4life", "12345", "Subteam"),
        "st3": EmployeeRecord("Jenny", "Darling", "12345", "Subteam"),
        "st4": EmployeeRecord("Sophia", "Schuhmacher", "12345", "Subteam"),
        "st5": EmployeeRecord("Wernon", "Dursley", "12345", "Subteam"),

    }

    # List to hold EventRequests
    global eventRequestList
    eventRequestList = []

    # List to hold ResourceRequests
    global ResourceRequestList
    ResourceRequestList = []

    # List to hold FinancialRequests
    global FinancialRequestList
    FinancialRequestList = []