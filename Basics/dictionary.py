# unordered,


map={1:'dharmesh',1:'dharmesh',1:'dharmesh'}

for k in map.keys():
    print(map[k])

# deleting the values  in MAP
del map[1]

map[2]='upahdyay'



# testing key
print ( 2 in map)
print ( 'upahdyay' in map)
print ( 1 in map)


# new Dictionary from keys
map =dict.fromkeys((10,11,12),'Geeky')

print(map)

for (k,v) in map.items():
    print(k,v)



map.update({111:'dharmesh'})

print(map)