# Question: 1 Write a program to print the follwoing pattern:
# 12345
# 12345
# 12345
# 12345
#
#
# Solution: 1
n=5   
for i in range(0,n):
 for j in range(0,n):
  print(j+1, end= '')
 print("\n")



# Question: 2
# Print following pattern:
# 01234
# 0123
# 012
# 01
# 0
#
# Solution2:
n=5
for i in range(0,n):
  for j in range(0,n-i):
   print(j, end= '')
  print("\n")
 


# Question: 3
# WAP tp print:
# 12345
#  2345
#   345
#     45
#       5
#



Solution: 3
n=6
for i in range(0,n):
  for j in range(0,n):
    if i>j:
     print(" ")
    else:
     print(j+1, end='')
print("\n") 


#
#
#
#
# Q-4 Find the factorial of a 5

# Sol:
n=5
fact=1
for i in range(1,n+1):
 fact= fact*i
print(fact, end='') 
print("\n")

#
#
# Q-5 Ceack if a number is prime number or not
#
#
# Sol:
n=23
k=0
for i in range(1,n+1):
 if (n%i)==0:
  k+=1
if k==2:
  print("Number is a prime number")
else:
 print("Number is not a prime number")


# Q-6 WAP tp print the following patter:
# 1
# 22
# 333
# 4444
# 55555
#
# Sol:
n=5
for i in range(0,n):
 for j in range(0,n):
  if i>=j:
   print (i+1, end='')
 print("\n")   



# Q-7 WAP to print the follwoing pattern
# 11111
# 2222
# 333
# 44
# 5
#
# Sol:
n=5
for i in range(0,n):
 for j in range(0,n):
  if (i<=j):
   print (i+1, end='')
 print("\n")   



#
# Q-8 WAP to print the following patter:
# 1
# 12
# 123
# 1234
# 12345
#
#
# Sol:
n=5
for i in range(0,n):
 for j in range(0,n):
  if (i>=j):
   print (j+1, end='')
 print("\n")   


#
# Q-9 WAP to print to print the reverse of a number
#
# Sol:
n=353
rev=0
while n>0:
 x= n%10
 rev=(rev*10)+x
 n//=10
print(rev)





# Q-10 WAP to print and check if the number is pallindrome or not
#
#
# Sol:
n=353
y=n
rev=0
while n>0:
 x= n%10
 rev=(rev*10)+x
 n//=10
print(rev)
if rev==y:
 print("The number is a pallindrome numer")
else:
 print("The number is not a pallindrome number")






 
# Q.11 WAP to print and check if the number is armstrong number or not
#
# Sol:
n=352
y=n
num=0
while (n>0):
 x=n%10
 num+=x*x*x
 n//=10
print(num)
if num==y:
 print("the number is armstrong number")
else:
 print("the number is not an armstromng number")




# Q12-WAP To find the number in an array by linear search:
#
# Sol:
a=[]
n=int(input("Enter the range of an array: "))
for i in range(0,n):
    val=int(input("enter the value in an array: "))
    a.append(val)
Target=int(input("Enter the value to be searched: ")) 
for i in range(0,n):
    if(Target==a[i]):
        print("Found")
 


# Q.13 Binary Search
#
#
# Sol:
a=[]
n=int(input("Enter the range of an array: "))
for i in range(0,n):
    val=int(input("enter the value in an array: "))
    a.append(val)
Target=int(input("Enter the value to be searched: ")) 
for i in range(0,n):
 min=0
 max=n-1
 while min<=max:
    mid=(min+max)//2
    if a[mid]==Target:
     print("Found at the position",mid)
     break
    elif a[mid]<Target:
        min=mid+1
    else:
        max=mid-1
        

#
# Q-14 Find the number using bubble sort and binary search to find a nummber
#
# Sol:
a=[]
n=int(input("Enter the range of an array: "))
for i in range(0,n):
    val=int(input("enter the value in an array: "))
    a.append(val)
for i in range(0,n):
    for j in range(0,n-i-1):
        if(a[j]>a[j+1]):
            k=a[j]
            a[j]=a[j+1]
            a[j+1]=k
for i in range(0,n):
    print(a[i])
Target=int(input("Enter the value to be searched: ")) 
for i in range(0,n):
 min=0
 max=n-1
while min<=max:
    mid=(min+max)//2
    if a[mid]==Target:
     print("Found at the position",mid)
     break
    elif a[mid]<Target:
        min=mid+1
    else:
        max=mid-1
 



#
# Q.15 Selection sorting
#
# Sol:
a=[]
n=int(input("Enter the range of an array: "))
for i in range(0,n):
    val=int(input("enter the value in an array: "))
    a.append(val)
for i in range(0,n):
    min=a[i]
    for j in range(i+1,n):
        if(a[j]<min):
            k=a[j]
            a[j]=a[i]
            a[i]=k
for i in range(0,n):
    print(a[i])





# Q17-Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
#
# Eg:
#
# Case 1:
# base = 2
# exponent = 5
# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
#
# Sol-
def exponent(base, exp):
 value=1
 for i in range(0,exp):
  value=value*base
 return value



base=5
exp=5
v=exponent(base,exp)
print(v)


# Q Print the following pattern
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
#
#
# Sol:
n=6
for i in range(0,n):
 for j in range(0,i):
  print('*', end='')
 print("\n")  
for i in range(1,n-2):
 for j in range(1,n-i):
  print('*', end='')
 print("\n")




#
# Q-. Write a function to generate a Python list of all the even numbers between m and n
#
# Sol-
def list(m,n):
 for i in range(m,n):
  if (i%2==0):
   print(i)

m=5
n=25
list(m,n)

 


