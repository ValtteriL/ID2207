import sys
sys.path.append('../')
import FinancialRequest

# test setup of FinancialRequest
def setUp(EmployeeID, department, ExtreBudget, target,details):
    
    request = FinancialRequest.FinancialRequest(EmployeeID, department, ExtreBudget, target, details)

    assert request.EmployeeID == EmployeeID 
    assert request.department == department
    assert request.ExtreBudget ==  ExtreBudget
    assert request.target ==  target
    assert request.details == details

