from ResourceRequest import ResourceRequest
import database


## ResourceRequest related helpers

# Create ResourceRequest
def crr():
    print('\n## Creating new ResourceRequest ##')
    clientname=input('ClientName:')
    department=input('Department: ')
    number=input('The Number of Requested Staff: ')
    field=input('The Field of Requested Staff: ')
    experience=input('The Experience of Requested Staff ')
    details=input('The More Details:')

    rrequest=ResourceRequest(clientname,department,number,field,experience,details)
    database.ResourceRequestList.append(rrequest)
    print('\n')


# View ResourceRequest
def vrr():
    if len(database.ResourceRequestList) > 0:
        print('\nChoose ResourceRequest to View')
        for index, request in enumerate(database.ResourceRequestList):
            print('{} = {}'.format(index,request.clientname))
        choice=int(input('>'))
        if choice<len(database.ResourceRequestList):
            print('\n## Viewing ResourceRequest ##')
            database.ResourceRequestList[choice].printRR()
        else:
            print('Invalid selection')
    else:
        print('There are no ResourceRequests!')
    print('\n')


# Delete ResourceRequest
def drr():
    if len(database.ResourceRequestList)>0:
        print('\nChoose ResourceRequest to Delete')
        for index ,request in enumerate (database.ResourceRequestList):
            print('{} = {}'.format(index,request.clientname))
        choice=int(input('>'))
        if choice<len(database.ResourceRequestList):
            del database.ResourceRequestList[choice]
            print('Delet successfully!')
        else:
            print('Invalid selection')
    else:
        print('There are no ResourceRequests')
    
    print('\n')            
        
