import testEmployeeRecord
import testEventRequest
import testFinancialRequest
import testResourceRequest
import testSubteamPlan
import testSubteamTask

if __name__ == "__main__":
    
    print("Testing EmployeeRecord")
    testEmployeeRecord.setUp("firstname", "lastname", "password", "position")

    print("Testing EventRequest")
    testEventRequest.setUp("clientname","eventname","starttime","endtime","details","budget")

    print("Testing FinancialRequest")
    testFinancialRequest.setUp("EmployeeID", "department", "ExtreBudget", "target", "details")

    print("Testing ResourceRequest")
    testResourceRequest.setUp("clientname","department","number","field","experience","details")

    print("Testing SubteamPlan")
    testSubteamPlan.setUp("EmployeeID", "department", "Time", "details")

    print("Testing SubteamTask")
    testSubteamTask.setUp("taskname","department","time","details")

    print("All tests passed!")

