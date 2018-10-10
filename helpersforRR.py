from ResourseRequest import ResourseRequest
import database
#creat ResourseRequest

def crr():
    print('\n##Creating new ResourseRequest##')
    clientname=input('ClientName:')
    department=input('Department: ')
    number=input('The Number of Requested Staff: ')
    field=input('The Field of Requested Staff: ')
    experience=input('The Experience of Requested Staff ')
    details=input('The More Details:')

    rrequest=ResourseRequest(clientname,department,number,field,experience,details)
    database.ResourseRequestList.append(rrequest)
    print('\n')

def vrr():
    if len(database.ResourseRequestList)>0:
        print('\nChoose ResourseRequest to View')
        for index ,request in enumerate (database.ResourseRequestList):
            print('{}={}'.format(index,request.clientname))
        choice=int(input('>'))
        if choice<len(database.ResourseRequestList):
            print('\n## Viewing ResourseRequest##')
            database.ResourseRequestList[choice].printRR()
        else:
            print('Invalid selection')

    else:
        print('There are no ResourseRequests!')

    print('\n')

def drr():
    if len(database.ResourseRequestList)>0:
        print('\nChoose ResourseRequest to Delet')
        for index ,request in enumerate (database.ResourseRequestList):
            print('{}={}'.format(index,request.clientname))
        choice=int(input('>'))
        if choice<len(database.ResourseRequestList):
            del database.ResourseRequestList[choice]
            print('Delet successfully!')
        else:
            print('Invalid selection')
    else:
        print('There are no ResourseRequests')
    
    print('\n')            
        
