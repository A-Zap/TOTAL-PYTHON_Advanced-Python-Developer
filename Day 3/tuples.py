my_tuple= (1,2,(10, 20),4)
my_tuple = list(my_tuple)
my_tuple= tuple(my_tuple)

print(type(my_tuple))


T= (1,2,3)
X,Y,Z = T
print(X,Y,Z)



t= (1,2,3,1)
print(t.count(1))

t= (1,2,3,1)
print(t.index(2))