hours=[22, 17, 27, 40, 45]
weeks=[48, 50, 42, 46, 43]
emplo=['John,1', 'Eric,1.5', 'Terry,2', 'Michael,4', 'Graham,2']
output=['{0} made {1:.0f} Silver in {2} hours.'.format(e.split(',')[0], float(e.split(',')[1])*hours[i]*weeks[i], hours[i]*weeks[i])  for i,e in enumerate(emplo)]
for x in output:
    print(x)
