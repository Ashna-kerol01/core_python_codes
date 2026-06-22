'''
#NON - RETUEN##
#APPEND - add at the end of the list [non return)
lis = [22,33,37,55,33,12,48,33,11,9]
print(lis)
#lis.append(99)

#INSERT - add in the start or middle (on particular index number)
lis.insert (3,99)
print(lis)

#EXTAND (iterable) - we can add iterables ->non return f()
#iterable = containers(list ,tuple,set,dict)

print(lis)
lis.extend(["we","are","humans"])
print(lis)


#concatenate  -  we can only concate relevant datatypes (works as an extend)

#lis1 = [22,33,37,55,33,12,48,33,11,9]
#lis2 = [66,77,88]

#r = lis1 +lis2
print(r)

## WRITTEN FUNCTIONS ##

#COUNT = WRITTEN FREQUENCY OF THE ELEMENTS

lis = [22,33,37,55,33,12,48,33,11,9]
d = lis.count(33)
print(d)

d = lis.count(303)
print(d)

#INDEX - WRITTEN INDEX NUMBER (element [start,stop])
#stop = search before the given index

lis = [22,33,37,55,33,12,48,33,11,48,9]
idx1 = lis.index(33)
print(idx1)

idx2 = lis.index(33,2)
print(idx2)

idx3 = lis.index(33,idx2 + 1)
print(idx3)

#idx = lis.index(33,2,4) {it search before the 4 which means to the 3rd index only}
#print(idx)

#functions vs methods #  have to find the solution
#A FUNCTION IS INDEPENTEND .      FUNCTION CALLED DIRECTLY  BY FUNCTION NAME       
#A METHOD BELONGS TO AN OBJECT OR CLASS .      METHOD CALLED USING DOT OPERARTOR(.)[PERIOD OPERATOR]        METHOD DEFINE UNDER CLASS 

#sum() , max(),min(),len()

lis = [22,33,37,55,33,12,48,33,11,48,9]

a = sum(lis)
print(a)

b = max(lis)
print(b)

c = min(lis)
print(c)

d =len(lis)
print(d)

name = ["kabir","raj","alok","aman","bhupesh"] #WILL COMPARE ON THE BASIS OF THE ASCCI VALUE
e = max(name) # AND THE COMPARISON IS KNOWN AS LEXOGRAPHICAL COMPARISION 
print(e)

f = min(name)
print(f)
'''
## DELETATION FUNCTIONS ##

#POP#  DELETE LAST ELEMENT(-1)  or WHEN WE PASS INDEX NUMBER IT WILL DELETE THE ELEMENT ON THAT INDEX    [return function]
lis = [33,4,90,12,11,33,6,9,33,1]
print(lis)
a = lis.pop(2)
print(lis)
print("deleted element:" , a)

#REMOVE#  pass element in the parameter  [non return function]
lis = [33,4,90,12,11,33,6,9,33,1]
print(lis)
lis.remove(12)
print(lis)
lis.remove(33)
print(lis)


#CLEAR#    REMOVE ALL THE ELEMENTS OF THE LIST , OR CLEAR THE LIST  [NON RETURN FUNCTION]

lis = [33,4,90,12,11,33,6,9,33,1]
lis.clear()
print(lis)

# del statment  - delete reference not the object [ delete does not directly delete data or free memory . instead ,it unbinds the variables name from the object . if that object no longer has any
#any acitvity  reference pointing to it , python automatic garbage collector will eventually destroy the object and reclaim its memory 
lis = [33,4,90,12,11,33,6,9,33,1]
del lis
print(lis)


























