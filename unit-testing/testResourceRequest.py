import sys
sys.path.append('../')
import ResourceRequest

# test setup of ResourceRequest
def setUp(clientname,department,number,field,experience,details):

    request = ResourceRequest.ResourceRequest(clientname,department,number,field,experience,details)

    assert request.clientname == clientname 
    assert request.department == department
    assert request.number == number
    assert request.field == field
    assert request.experience == experience
    assert request.details == details

