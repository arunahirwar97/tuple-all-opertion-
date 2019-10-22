tuple1 = 'a','r','u','n'
tuple2 = 'a','h','i','r','w','a','r'
print(tuple1)
print (tuple2)
a = tuple1 + tuple2
print ('concatanent tuple : ',a)
b = len (a)
print('lenth of tuple : ',b)
c = list(a)
print('tuple convert in the list :',c)
d = max(c)
print('maximum in the both tuple : ',d)
d = min(c)
print('minimum in the both tuple : ',d)
e = "arun ahirwar "
f = tuple(e)
print("string convert into tuple : ",f)
g = f[::-1]
print ("reverse in the tuple : ",g)
h = len(g)
print ("Lenth of the reversed tuple : ",h)
print('\t\t       Other technique of the revesed tuple ')
i =tuple(reversed(f))
print ('Other technique of the revesed tuple',i)