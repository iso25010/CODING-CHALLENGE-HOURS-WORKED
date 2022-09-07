chars = ['a', 'b']
nums = [1, 2, 3]

comb=[{n-1:chars[:n-1]} for n in nums]
print(comb)