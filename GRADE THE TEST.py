
#output: 'TestScores: 1 of 6 (17%),3 of 6 (50%),6 of 6 (100%)'
class GradeTests():
    def __init__(self,aTemplate,answers):
        self.template=aTemplate
        self.answers=answers
        self.results=dict()

    def correct(self):
        for x in self.answers:
            self.results[x[0]] = tuple([1 if t==x[1:][i] else 0 for i,t in enumerate(self.template)])
        
    def getResults(self):
        return self.results 

    def __str__(self):
        str=''
        for v in self.getResults().values():
            str+='{0} of {1} ({2:>2.0f}%), '.format(v.count(1),len(v),v.count(1)/len(v))
        return str
    

answers=[['John', 'A', 'B', 'A', 'C', 1166, 1989], ['Eric', 'B', 'C', 'C', 'B', 1066, 1939], ['Michael', 'A', 'C', 'D', 'B', 1066, 1945]]
template=['A', 'C', 'D', 'B', 1066, 1945]

g=GradeTests(template,answers)
g.correct()
print(g)


    
