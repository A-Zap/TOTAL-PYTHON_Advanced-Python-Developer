my_dictionary= {'c1':'value1','c2':'value2'}
print(my_dictionary)
result = my_dictionary['c1']
print(result)


customer= {'name': 'john','last_name':'lennon','weight': 88, 'height': 1.76}
query= (customer['height'])
print(query)


dic={1: 55, 2:[10,20,30], 3:{'s1': 100, 's2': 200}}
print(dic[3]['s2'])


dic = {'k1': ['a','b','c'],'k2':['d','e','f']}
print(dic['k2'][1].upper())


dic = {1:'a',2:'b'}
print(dic)

dic[3] = 'c'
print(dic)

dic[2]= 'B'  #replace
print(dic)


print(dic.items())
