import sys
sys.path.append('../')
import EmployeeRecord

# test setup of EmployeeRecord
def setUp(firstname, lastname, password, position):

    record = EmployeeRecord.EmployeeRecord(firstname, lastname, password, position)

    assert record.firstname == firstname
    assert record.lastname == lastname
    assert record.password == password
    assert record.position == position


