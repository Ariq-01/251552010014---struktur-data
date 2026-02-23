tuple_x = (12, 331, 21,331,31,31,2,3,331,331)
print("hasil index x :", tuple_x.index(12))
print('index x of 2:', tuple_x.index(2))

#)print both of them 
print('perbandingan :', tuple_x.index(21) == tuple_x.index(31))
print('perbandingan :', tuple_x.index(21) != tuple_x.index(31))

# set tsuktur datta dengan data unk 
#method pada set 

set_x = set(tuple_x)
set_x.difference_update({331})
print("tetsing diffenct and set data")
print('dffience update:', set_x)