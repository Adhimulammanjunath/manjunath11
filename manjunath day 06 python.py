
s1=input("enter string: ")
fst = s1[-1].upper()
lst = s1[-1].upper()
print(fst+s1[1:len(s1)-1]+fst)

print(s1.replace('h','h'))
print(s1.replace('d',"d"))



n=128
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")




# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]



n=128
tem = n
strl = ""
while n!=0:
    rem =n%10
    check= temp %n
    n = n //10
if n % 1==0 and n % 2==0 and n % 8==0:
    print("yes")
else:
    print("No")



n = 128678
temp = n
str1 = ""
while n!= 0:
    rem = n%10
    check = temp % n
    n = n//10

    

# if f1==0:
  #  print("yes")
    # else:
    # print("no")



n = int(input(" enter number : "))
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")




l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

 #print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)




# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)


# * Eg:2
#  s2 = {9, 9, 89,7.76, 8+7J,(8, 7, 5),"truck",'e'}
 # print(s2) --> error


# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)




s1 = {8, 78, 67, 'u'}
s1.add(43)
print(s1)

# pop() # to delete one element randonly
# s1.pop()
# print(s1)

# remove ()
# s1.remove(978)
# print(s1)

# discard()
# s1.discarrd(8967)
# print (s1)


# clear()
#l1 = {}
# print(type(l1)--. datatype is dict




# clear()

l1 = {}
print(type(l1)) 


s1 = set() # --> to create empty set
print(type(s1))



s1 = {8,9,0}
s1.clear()
print(s1)



s1 = {8,9,0}
del s1
print(s1)
'''''

# join the sets
# union() --> to combine 2 sets
'''
s1 = {9,0,8}
s2 = {9.90,"caed",'t',56}
s3 = s1.union(s2)
print(s3)
'''
# intersection() --> to get common elements inside set
'''
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.intersection(s2))
''
# difference{}
s1 = {4,5,6}
s2 = {5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))

