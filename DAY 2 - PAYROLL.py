# wages = # hours worked * basepay

# output should be a printed list, like
#"Joe's monthly pay is 19 800 copper"
#"Sue's monthly pay is 21 000 copper"
#"Bo's monthly pay is 14 725 copper"
#"Li's monthly pay is 14 400 copper"
#"Ty's monthly pay is 14 800 copper"
#"Vi's monthly pay is 13 760 copper"

# bonus:
# client would love if bonus of 1500 copper can be added for 1100+ calls



from datetime import date

class Employee():
    def __init__(self,name,eNumber,base):
        self.name=name
        self.id=eNumber
        self.base=base
        self.wage=0

    def calculateWage(self,hours):
        self.hours=hours
        self.wage=self.base*self.hours

    def getWage(self):
        return self.wage

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def __str__(self):
        rec="{0:<9} monthly pay is {1:>4} copper".format(self.name+"'s",self.getWage())
        return(rec)

class Evidence():
    def __init__(self):
        self.lPhone_m=dict()
        self.lEmployee=dict()
        
    def addPhone_m(self,date,phone_m):
        self.lPhone_m[date]=phone_m

    def addEmployees(self,employees):
        self.lEmployee=employees

    def addEmployee(self,name,attributes):
        self.lEmployee[name]=attributes

    def __str__(self):
        return self.lPhone_m.__str__()
    
    def getPhone(self,date):
        return self.lPhone_m[date]

    def getPhoneLog(self,date,id):
        return self.getPhone(date)[id]
    
    def getPhoneLogItem(self,date,id,index):
        try:
            return self.getPhoneLog(date,id)[index]
        except:
            print('Id {0} does not exist on a date {1}.'.format(id,date))
            return None

    def getPhoneLogItemName(self,date,name,index):
        id=self.getEmplAttributesItem(name,0)
        return self.getPhoneLogItem(date,id,index)

    def getEmplAttributes(self,name):
        return self.lEmployee[name]

    def getEmplAttributesItem(self,name,index):
        return self.getEmplAttributes(name)[index]

class PayRoll():
    def __init__(self):
        self.ev=Evidence()
        self.emplo=dict()
        self.lPayRoll=dict()

    def addEvidenceRecord(self,date,phone_m):
        self.ev.addPhone_m(date,phone_m)

    def addEmployees(self,emplo):
        self.ev.addEmployees(emplo)

    def setEmployee(self,name,id,base):
        return Employee(name,id,base)
    
    def updateEmployees(self):
        for k in self.ev.lEmployee.keys():
            self.emplo[k]=self.setEmployee(k,self.ev.getEmplAttributesItem(k,0),self.ev.getEmplAttributesItem(k,1))

    def getEmplo(self):
        return self.emplo
    
    def __iter__(self):
        self.k=list(self.emplo.keys())
        self.i=-1
        return self

    def __next__(self):
        self.i+=1
        try:
            return(self.emplo[self.k[self.i]])
        except IndexError:
            raise StopIteration

    def __str__(self):
        str=''
        for x in self:
            str+=x.__str__() + '\n'
        return str

    def preparePayRoll(self,date):
        for x in self:
            x.calculateWage(self.ev.getPhoneLogItemName(date,x.getName(),0))



# {'employee number':'logged hours at work', 'number of calls', 'total call-time in minutes','# feedback rated 4+'}
phone_m = {1:[180,1200,4783,223],2:[175,1213,4565,275],3:[155,1008,4145,180],4:[160,1005,4315,138],5:[185,1265,6200,264],6:[160,1052,4532,184]}

#employee_d1:{Name:[employee number, base pay/hour]}
employees_d1 = {'Joe': [1, 110], 'Sue': [2, 120], 'Bo': [3, 95],'Li': [4, 90],'Ty': [5, 80], 'Vi': [6, 86]}

p=PayRoll()
p.addEmployees(employees_d1)
p.addEvidenceRecord(date(2022,9,28),phone_m)
p.updateEmployees()
p.preparePayRoll(date(2022,9,28))
print(p)



