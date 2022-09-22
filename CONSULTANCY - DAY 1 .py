#bonus : to further impress your client, convert into dictionary with a list of numbers as below
#employees_d2: {'Joe':[1,110],'Sue':[2,120],'Bo':[3,95],'Li':[4,90],'Ty':[5,80],'Vi':[6,86]}

employees_d2= {x[0]:[int(y) for y in x[1:]]  for x in [e.split(',')[:-1] for e in 'Joe,1,110,M*Sue,2,120,F*Bo,3,95,M*Li,4,90,F*Ty,5,80,M*Vi,6,86,F'.split('*')]}

for k,v in employees_d2.items():
    print('Name: {0:<7} measures: {1:>3}, {2:>3}'.format(k,v[0],v[1]))

