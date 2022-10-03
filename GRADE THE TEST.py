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

    

answers=[['John', 'A', 'B', 'A', 'C', 1166, 1989], ['Eric', 'B', 'C', 'C', 'B', 1066, 1939], ['Michael', 'A', 'C', 'D', 'B', 1066, 1945]]
template=['A', 'C', 'D', 'B', 1066, 1945]

g=GradeTests(template,answers)
g.correct()
print(g.getResults())


    
