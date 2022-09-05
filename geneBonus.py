def mutate(aWord):
    i=0
    while True:
        try:
            one=aWord[0+i]
            two=aWord[1+i]   
            three=aWord[2+i]             
            four=aWord[3+i]
            if two=='C' and four=='T':
                aWord=aWord.replace(two+three+four,two+one+four)
                return(aWord)
            i+=1
        except IndexError:
            return aWord

sequences = ['ATGCCATTGGCT','CCGTGCTTGTAT','ACTACCTACGT']
output=[mutate(aWord) for aWord in sequences]
print (output)
