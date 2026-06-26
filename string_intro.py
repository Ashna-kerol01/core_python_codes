#3RD DATA TYPE #

## STRING ##
'''
# sequence data type (ordered)
#string has indexing (+tive and -tive both)
# string is immutable data type
#biggest data type in any language
# repeatation allowed 
'''

'''
s = "we are going to learn about string"
print(type(s),s)

print(s[0])
print(s[7:12])  #slicing
print(s[16:21])

s = "apple"
print(s)

s = s + "pineapple"
print(s)

#functions in string ##

s = "apple .is good .for health ., banana. is also good "

# s.replace(old,new,occurence)  will replace the given string 

s1 = s.replace("good","best",1)
print(s)
print(s1)

s0 = s.replace("a","$",3)
print(s)
print(s0)

#count()  wil give frequency of the charcater

r = s.count("i")
print(r)

j = s.count("good")
print(j)

#index(element, start,stop)  will give index number

r = s.index("good")
print(r)

e = s.index("good",s.index("good") + 1)
print(e)

f = s.index("good",r + 1)
print(f)

# split(delimiter , occurence ) --> returns list

lis = s.split()
print(lis)

lis = s.split(".",2)
print(lis)

#join ---> return string
#syntax =  "".join(iterable) 

lis = ["apple","pineapple","banana"]
r = " ".join(lis) #between "" we give space to make space between the elements 
print(r)


#upper -> converts the string into upper case
s1 = "aPPle IS goOD FOr HeaLTH"
print(s1)
a = s1.upper()
print(a)

#lower -> will convert the string into lower case 
b = s1.lower()
print(b)


#capitalize -> capalize the first letter of the string and converts the remaining into lower case 
c = s1.capitalize()
print(c)

#swapcase -> converts upper case into lower and lower into upper 

d = s1.swapcase()
print(d)



#boolean output function ##

s1 = "APPLE IS GOOD"

#isupper() -> test alphabet wheather they are in upper case 

a = s1.isupper() 
print(a)

#islower  -> test alphabet wheather they are in lower case
s2 = "apple is good "

b = s2.islower()
print(b)

#isalpha -> string should conatin alphabet(lower,upper both) no space allowed

s3 = "appleisgood "

c = s3.isalpha()
print(c)

#isdigit ->  string should contain all digits and not any space or other symbols

s4 = "2222333444"
d = s4.isdigit() #all digits
print(d)

'''

#string concatenation"

s1 = "monday"
s2 = "tuesday"
s3 = "wednesday"
s4 = " "

r = s1 + s4 + s2 + s4 + s3
print(r)





















print(c)







