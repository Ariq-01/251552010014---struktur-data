data = ['one', 'two', 'three', 'four', 'five']
value_ind = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


raw_nd = dict(zip(data, value_ind))
print('Raw Data Dictionary:', raw_nd)


hash_map = dict(zip(data, value_ind))
print('Hash Map:', hash_map)


print("test  HashMap:")
for key in hash_map:
    print(f'Key: {key}, Value: {hash_map[key]}')
