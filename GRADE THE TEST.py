
#output: 'TestScores: 1 of 6 (17%),3 of 6 (50%),6 of 6 (100%)'
class GradeTests():
    def __init__(self,cTemplate,answers,pTemplate,gTable):
        self.template=cTemplate
        self.answers=answers
        self.pTemplate=pTemplate
        self.gTable=gTable
        self.results=dict()
        #[total,good,good/total,p,grade]
        self.points=dict()

    #Advanced: Score tests 1 point for multiple choice(letter), 2 points for correct year.
    def correct(self):
        for x in self.answers:
            self.results[x[0]] = tuple([self.pTemplate[i] if t==x[1:][i] else 0 for i,t in enumerate(self.template)])
        self.gradeStudents()

    def gradeStudents(self):
        
        total=0
        wrong=0
        for k,v in self.getResults().items():
            p=0
            for x in v:
                p+=x
            total=len(v)
            wrong=v.count(0)
            good=total-wrong
            grade=self.mark(p)
            self.points[k]=[total,good,good/total,p,grade]
    
    def mark(self,points):
        for k,v in self.gTable.items():
            if points>=v:
                grade=k
        return grade

    def getResults(self):
        return self.results 

    def __str__(self):
        #output: 'TestScores: 1 of 6 (17%),3 of 6 (50%),6 of 6 (100%)'

        str=''
        for v in self.getResults().values():
            str+='{0} of {1} ({2:>2.0f}%), '.format(v.count(1),len(v),v.count(1)/len(v))
        return str
    

answers=[['John', 'A', 'B', 'A', 'C', 1166, 1989], ['Eric', 'B', 'C', 'C', 'B', 1066, 1939], ['Michael', 'A', 'C', 'D', 'B', 1066, 1945]]
template=['A', 'C', 'D', 'B', 1066, 1945]
pTemplate=[1,1,1,1,2,2]
grading_table = {'F':0,'D':2,'C':4,'B':6,'A':7}

g=GradeTests(template,answers,pTemplate,grading_table)
g.correct()
print(g)
print(g.getResults())
print(grading_table)
print(g.points)


    
