chars = ['a', 'b']
nums = [1, 2, 3]

comb=[{n-1:chars[:n-1]} for n in nums]
comb1={n-1:chars[:n-1] for n in nums}
print(comb)
#[{0: []}, {1: ['a']}, {2: ['a', 'b']}]
print(comb1)
#{0: [], 1: ['a'], 2: ['a', 'b']}