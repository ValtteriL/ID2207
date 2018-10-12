class Project:

    workers = None # list of EmployeeRecords who are assigned to this project
    tasks = [] # list of SubteamTasks that are assigned to workers
    plans = [] # list of SubteamPlans made by workers

    def __init__(self, workers):
        self.workers = workers

