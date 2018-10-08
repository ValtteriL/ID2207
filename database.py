from EmployeeRecord import EmployeeRecord

# What each position can do
# not completed yet
Privileges = {
    "CSStaff": ['q', 'cer', 'ver', 'uer'],
    "CSManager":['q', 'ver', 'aer', 'rer'],
    "FManager": ['q'],
    "AManager": ['q'],
    "PManager": ['q'],
    "HR": ['q'],
    "Subteam": ['q']
}

# Available actions
# key: (description, function)
Actions = {
    "q": ("logout",None),
    "cer": ("create EventRequest", None),
    "ver": ("view EventRequest", None),
    "uer": ("update Eventrequest", None),
    "aer": ("accept EventRequest", None),
    "rer": ("reject EventRequest", None),
    "vemr": ("view EmployeeRecord", None),
    "uemr": ("update EmployeeRecord", None)
}

# Create some users
# EmployeeRecord(firname, lastname, password, position)
Employees = {
    "css": EmployeeRecord("kalle", "kehveli", "secret", "CSStaff"),
    "csm": EmployeeRecord("seppo", "taalasmaa", "password", "CSManager"),
    "fm": EmployeeRecord("ismo", "laitela", "hunter", "FManager"),
    "am": EmployeeRecord("sauli", "niinistö", "12345", "AManager"),
    "pm": EmployeeRecord("sauli", "niinistö", "12345", "PManager"),
    "hr": EmployeeRecord("sauli", "niinistö", "12345", "HR"),
    "st": EmployeeRecord("sauli", "niinistö", "12345", "Subteam")

}