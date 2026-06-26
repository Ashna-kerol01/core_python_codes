
#SLICING##
# SLICING = TO GET SUB-SEQUENCE FROM SEQUENCE 
#SLICING DONE IN TUPLE, LIST , STRING
# SYNTAX OF SLICING =  T[START:END:JUMP]   #END BEFORE THE ENDING POINT [END IS OMMIT ]
#                        [start:stop:step]

#    0   1  2    3  4   5  6    7    8    9    10  11          [index number]
t = (23,44,"hi",67,100,29,355,91.9,2000,"bye",-11,455)
#   -12 -11 -10 -9  -8 -7 -6    -5  -4   -3    -2 -1

'''
#print(t[8],t[-4])
print(t)
a = t[2:10]
print(a)

b = t[-10:-2]
print(b)

c = t[-10:10]
print(c)
'''
a = t[2:10:4]
print(a)

a = t[9:1:-1]
print(a)

b = t[-3:-9:-1]
print(b)

a = t[2:10:-1]   #will give empty tuple
print(a)

c = t[2:]   #we can omit end point if we want to consider a end point of list .
print(c)

a = t[2: : 3]
print(a)

b = t[-8: :-2]
print(b)

c = t[-3:-10 :2]  #will give empty tuple 
print(c)

a = t[1:10:-2]  #will give empty tuple 
print(a)

b = t[::2]
print(b)

d = t[::-1]  #WILL GIVE REVERSE TUPLE OR WILL REVERSE THE TUPLE 
print(d)

#first five = t[ :5]   [ in case when we don't know the list and the value ]
#last five = t[-5: ]

print(t[::4])

t = (22,33,44)

print(type(t))

t1 = (23,)
print(type(t1))

t2 = 44,55,90,100   # another representation of tuple without paranthese

print(type(t2))

#index(),len(),max(),min(),sum(),count()

#sum
a = sum(t2)
print(a)

  
#max
a = max(t2)
print(a)

#min
a = min(t2)
print(a)

#len
a = len(t2)
print(a)

#count
a = count(t2)
print(a)

#index
a = index(t2[90])
print(a)










