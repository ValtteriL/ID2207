import sys
sys.path.append('../')
import SubteamPlan

# test setup of SubteamPlan
def setUp(EmployeeID, department, Time, details):

    plan = SubteamPlan.SubteamPlan(EmployeeID, department, Time, details)

    assert plan.EmployeeID == EmployeeID
    assert plan.department == department
    assert plan.Time == Time
    assert plan.details == details


