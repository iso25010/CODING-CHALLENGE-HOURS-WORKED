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

    def __str__(self):
        rec="{0:}'s monthly pay is {1:} copper".format(self.name,self.getWage())
        return(rec)

class Evidence():
    def __init__(self):
        self.lPhone_m=dict()
        
    def addPhone_m(self,date,phone_m):
        self.lPhone_m[date]=phone_m

    def __str__(self):
        return self.lPhone_m.__str__()
    


# {'employee number':'logged hours at work', 'number of calls', 'total call-time in minutes','# feedback rated 4+'}
phone_m = {1:[180,1200,4783,223],2:[175,1213,4565,275],3:[155,1008,4145,180],4:[160,1005,4315,138],5:[185,1265,6200,264],6:[160,1052,4532,184]}

#employee_d1:{Name:[employee number, base pay/hour]}
employees_d1 = {'Joe': [1, 110], 'Sue': [2, 120], 'Bo': [3, 95],'Li': [4, 90],'Ty': [5, 80], 'Vi': [6, 86]}

e=Employee('Gogo',1,150)
e.calculateWage(180)
print(e)

ev=Evidence()
ev.addPhone_m(date(2022,9,6),phone_m)
print(ev)
