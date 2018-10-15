import sys
sys.path.append('../')
import EventRequest

# test setup of EventRequest
def setUp(clientname,eventname,starttime,endtime,details,budget):

    request = EventRequest.EventRequest(clientname,eventname,starttime,endtime,details,budget)

    # test attributes
    assert request.clientname == clientname
    assert request.eventname == eventname
    assert request.starttime == starttime
    assert request.endtime == endtime
    assert request.details == details
    assert request.budget == budget

    # test rest of attributes that are not bound on init
    assert request.project == None
    assert request.accepted == False
    assert request.rejected == False
