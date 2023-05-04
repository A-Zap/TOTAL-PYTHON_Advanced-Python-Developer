my_list= ['a','b','c']
print(type(my_list))

my_list= ['a','b','c']
result= len(my_list)
print(result)

my_list= ['a','b','c']
result= my_list[0:2]
print(result)

my_list= ['a','b','c']
my_list2= ['d','e','f']
print(my_list + my_list2)

my_list= ['a','b','c']
my_list2= ['d','e','f']
list3= my_list + my_list2
list3.append('g')    #list3[0]= 'alpha'
print(list3)

my_list= ['a','b','c']
my_list2= ['d','e','f']
list3= my_list + my_list2
list3.append('g')  
list3.pop(0) #delete

list1= ['g','o','b','m','c']
newlist1=list1.sort()
print(type(newlist1))

list1= ['g','o','b','m','c']
list1.sort()
list1.reverse()
print(list1)


