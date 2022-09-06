def mutate(aWord):
    i=0
    mutatedW=aWord
    while True:
        try:
            I=0+i
            II=1+i
            III=2+i
            IV=3+i
            one=aWord[I]
            two=aWord[II]   
            three=aWord[III]             
            four=aWord[IV]
            if two=='C' and four=='T':
                mutatedW=mutatedW[:I+1] + mutatedW[I+1:IV+1].replace(two+three+four,two+one+four) + mutatedW[IV+1:]
                 
            i+=1
        except IndexError:
            return mutatedW

sequences = ['ATGCCATTGGCT','CCGTGCTTGTAT','ACTACCTACGT']
output=[mutate(aWord) for aWord in sequences]
print(sequences)
print (output)
