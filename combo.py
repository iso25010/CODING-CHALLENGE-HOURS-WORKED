chars = ['a', 'b']
nums = [1, 2, 3]

comb=[{n-1:chars[:n-1]} for n in nums]
comb1={n-1:chars[:n-1] for n in nums}
comb2=[[comb1[x], x] for x in comb1]
print(comb)
#[{0: []}, {1: ['a']}, {2: ['a', 'b']}]
print(comb1)
#{0: [], 1: ['a'], 2: ['a', 'b']}
print(comb2)
#[[[], 0], [['a'], 1], [['a', 'b'], 2]]
