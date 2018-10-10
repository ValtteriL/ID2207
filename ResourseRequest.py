class ResourseRequest:
      clientname=None
      department=None
      number=None
      field=None
      experience=None
      details=None


      def __init__(self,clientname,department,number,field,experience,details):

          self.clientname=clientname
          self.department=department
          self.number=number
          self.field=field
          self.experience=experience
          self.details=details

      def printRR(self):
          print('ClientName:{}'.format(self.clientname))
          print('Department{}'.format(self.department))
          print('Number:{}'.format(self.number))
          print('Field:{}'.format(self.field))
          print('Experience of Required Staff:{}'.format(self.experience))
          print('Details={}'.format(self.details))
