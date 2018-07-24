data1 = [ { "xid" : 10, "name" : 'abc' }, { "xid" : 1, "name" : 'pqr' }, { "xid" : 5, "name" : 'klm' } ]
data2 = [ (10, "abc"), (1, "pqr"), (5, "klm") ]

data1.sort(key=lambda x: x['xid'])
data2.sort(key=lambda x: x[0])

print(data1)
print(data2)
