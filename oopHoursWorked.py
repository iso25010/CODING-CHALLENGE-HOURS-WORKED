class Empl():
    def __init__(self,h,w,n,r):
        self.hours=h
        self.totalHours=self.hours*w
        self.name=n
        self.salary=r*self.totalHours
        
    def __str__(self):
        return(
        '{0} made {1:.0f} Silver in {2} hours.'.format(self.name, self.salary, self.totalHours)
        )

class Evidence():
    def __init__(self,hours,weeks,emplo):
        self.lHours=hours
        self.lWeeks=weeks
        self.lEmplo,self.lRates=self.decouple(emplo)
    def decouple(self,emplo):
        lE=list()
        lR=list()
        for item in emplo:
            i=item.split(',')
            lE.append(i[0])
            lR.append(float(i[1]))
        return(lE,lR)
    def __iter__(self):
        self.i=-1
        return self
    def __next__(self):
        self.i+=1
        try:
            return(Empl(self.lHours[self.i],self.lWeeks[self.i],self.lEmplo[self.i],self.lRates[self.i]))
        except IndexError:
            raise StopIteration
    def __str__(self):
        report=''
        for person in self:
            report+=person.__str__() + '\n'
        return(report)






hours=[22, 17, 27, 40, 45]
weeks=[48, 50, 42, 46, 43]
emplo=['John,1', 'Eric,1.5', 'Terry,2', 'Michael,4', 'Graham,2']

ev=Evidence(hours,weeks,emplo)
print(ev)
