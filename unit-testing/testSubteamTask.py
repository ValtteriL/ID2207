import sys
sys.path.append('../')
import SubteamTask

# test setup of SubteamTask
def setUp(taskname,department,time,details):

    task = SubteamTask.SubteamTask(taskname,department,time,details)

    assert task.taskname == taskname
    assert task.department == department
    assert task.time == time
    assert task.details == details

