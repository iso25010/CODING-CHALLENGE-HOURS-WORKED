#write code to subtract 2 numbers nearest each other.
#print results as shown
#nums = [25, 73, 42, 20, 95, 9, 27, 16, 55, 3]
#output: 'Difference of closest pair is: 27-25=2'

#bonus: subtract all numbers in closest pairs
#output:['27-25=2','20-16=4','9-3=6','55-42=13','95-73=22']

class Sub():
    def __init__(self,numbers):
        self.nums=numbers
        #[25, 73, 42, 20, 95, 9, 27, 16, 55, 3]
        self.nums.sort()
        #[3, 9, 16, 20, 25, 27, 42, 55, 73, 95]
        self.diffs= None
        self.determineDiffs()

    def determineDiffs(self):
        self.diffs=[(x,self.nums[i],x-self.nums[i]) for i,x in enumerate(self.nums[1:])]
        #[(9, 3, 6), (16, 9, 7), (20, 16, 4), (25, 20, 5), (27, 25, 2), (42, 27, 15), (55, 42, 13), (73, 55, 18), (95, 73, 22)]
        self.diffs.sort(key=self.getMinDiff)
        #[(27, 25, 2), (20, 16, 4), (25, 20, 5), (9, 3, 6), (16, 9, 7), (55, 42, 13), (42, 27, 15), (73, 55, 18), (95, 73, 22)]

    def getMinDiff(self,aCompute):
        return aCompute[-1]
        #the last member of Tuple is the diff

    def __str__(self):
        str='Difference of closest pair is: '
        for i,x in enumerate(self.diffs):
            if i==0:
                str+='{0}-{1}={2}\n'.format(x[0],x[1],x[2])
            str+='{0}-{1}={2}, '.format(x[0],x[1],x[2])
        return str[:-2]
        #cut off the 2 last chars ", "


nums = [25, 73, 42, 20, 95, 9, 27, 16, 55, 3]
s=Sub(nums)
print(s)

