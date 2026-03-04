# ===================================
#        VARIABLES & DATA TYPES
# ===================================

#Assign an integer to a variable and convert it to float.
a=15
print(float(15))

#Take two variables, swap their values without using a third variable.
a=5
b=6
a,b=b,a
print(a,b)

#Convert a string "123.45" into a float and then into an integer.
print(int(float("123.45")))

#Write a program that prints the memory address of two variables and compares them.
a=5
b=5 # python uses same memory for small integers this code might not work for large values or othher data types
print(id(a))
print(id(b))
if id(a)==id(b):  # if a is b: also works as it checks whether two variable stored at same memory location or pointing at same or not 
    print("stored at same memory location. ")

#Assign the same value to three variables in one line.
a,b,c=1,2,3
print(a,b,c)

#Check whether two variables point to the same object.
a=[1,2,3]
b=[1,2,3]
if a is b:
    print(f"yes {a} and {b} pointing at same object")
else:
    print(f"opps {a} and {b} are at different postion")

#Create a variable that changes type three times in one program.
a=5
print(a,f"hie I'm {type(a)} here")

a=6.9
print(a,f"hie I'm {type(a)} now")

a="hola"
print(a,f"hie I'm {type(a)} now")

a=(1,2)
b=(1,2)

if a == b:
    print(a,b,"satisfies == comparison operator" )
if a is b:
    print(a,b," satisfies 'is' identity operator")


# ===================================
#        NUMBERS & BOOLEAN LOGIC 
# ===================================

#Write a program to check if a number is positive, negative, or zero.
a = int(input("enter a number to check +ve -ve or 0: "))
if a>0:
    print("positive")
elif a<0:
    print("Negative")
else:
    print("Zero") 


#Check whether a number is even or odd without using %
a=int(input("enter a number to check odd or even : "))
if (a//2)*2 == a:
    print("even number")
else:
    print("odd number")

#       (OR)
if (a & 1) == 0:   #as even end with 0 and odd ends with 1
    print("even no.")
else:
    print("odd no.")

#Write a program to check if a number is divisible by both 3 and 5.
a=int(input("enter a no. to check divisibility with 3 or 5: "))
if (a % 3) == 0 & (a % 5) == 0:
    print(a, " is divisible by both 3 and 5")
else:
    print(a," is not divisible by 3 and 5")

#Write a program that evaluates all boolean combinations of True and False.
print("A\tB\tAND\tOR\tXOR")
print("-" * 35)

for i in [False, True]:
    for j in [False, True]:
        print(f"{i}\t{j}\t{i and j}\t{i or j}\t{i ^ j}")

print("\nA\tNOT A")
print("-" * 15)

for i in [False, True]:
    print(f"{i}\t{not i}")

#Show floating-point precision error using Python
if (0.1 + 0.2) == 0.3: #don't assume floats are exact precision from base 2 and base 10 changes hence never compare float using == 
    print(True)
else:
    print(False)

#Write a program to compare 0, False, and None.
a=0
b=False
c=None

print(f"a = {a},b = {b}, c = {c}")
print("type comparison:")
print(a,"=",type(a),b,"=",type(b),c,"=",type(c))

print("Value coparison:")
print(f"a==b : {a==b}, b==c : {b==c},a==c : {a==c}")

print("Identity comparison: ")
print(f"a is b :{a is b}, b is c :{b is c}, a is c : {a is c}")

print("boolean comparison: ")
print(f"bool of a : {bool(a)}, bool of b : {bool(b)}, bool of c : {bool(c)}")

#Write a program that demonstrates short-circuiting in logical operators.
#Python dose not always evalute both sides of logical operators

a = 41
b = "hie"
print(a % 2 == 0 and bool(b))
print("AND evaluated the first condition and its was false hence it didn't check the second condition ")
print(a % 2 !=0 or bool(b))
print("OR checked the first condition and as it was true it didn't check the second condition")

# ===================================
#               STRINGS 
# ===================================

#Reverse a string without using slicing.
s="hello"
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)

#Count vowels and consonants in a string.
vowel=['a','e','i','o','u']
count_vowel=0
count_consonant=0
s=input("enter a string to check vowels and consonants: ")
for i in s.lower():
    if i in vowel:
        count_vowel+=1
    else:
        count_consonant+=1
print("Total vowels",count_vowel,"\nTotal consonants",count_consonant)

#Check whether a string is a palindrome.
s=input("enter a string to check if palindrome: ")
if s == s[::-1]:
    print("string is palindrome")
else:
    print("not a palindrome")

#Find frequency of each character in a string.
s="mississippi"
for i in set(s):
    count_s=0
    for j in s:
        if i == j:
            count_s+=1
    print("frequency of",i,"is",count_s)

#       (or)
s="mississippi"
freq={}
for ch in s:
    if ch in freq.keys():
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in freq:
    print(f"{ch} frequency is {freq[ch]}")

#Remove all spaces from a string.
s="I love playing dungens and dragons"
print(s.replace(" ",""))

#           (or)
no_space=""
for i in s:
    if i != " ":
        no_space+=i
print(no_space)
        
#Check whether two strings are anagrams.
s1 = "worth"
s2 = "throw"
if len(s1) != len(s2):
    print(f"{s1} and {s2} not anagram")
elif sorted(s1.lower())== sorted(s2.lower()):
    print(f"{s1} and {s2} are anagrams")

#Extract digits from a string
s = "xyz123def456gh789"
numbers = "0123456789"
digits=""
for cha in s:
    if cha in numbers:
        digits+=cha
print(digits)

#Find the longest word in a sentence
s="I love playing dungens and dragons"
words=s.split()
maxi=words[0]
for i in words:
    if len(i)>len(maxi):
        maxi=i
print(maxi)

#Count words in a string without using split().
s="Difficulties strengthen the mind, as labor does the body"
words=[]
sub_word=""
 
for letter in s:
    if letter == " ":
        words.append(sub_word)
        sub_word=""
        
    else:
        sub_word+=letter
words.append(sub_word)
print(len(words))

# ===================================
#               LISTS 
# ===================================

#Create a list of numbers and find:sum,max,min.
l=[1,2,3,4,5]
sums=0
maxi=l[0]
mini=l[len(l)-1]
for i in l:
    sums+=i
    if i>maxi:
        max=i
    if i<mini:
        min=i
print(f"sum is {sums} max is {maxi} min is {mini}")

#Reverse a list in-place.
l=[1,2,3,4,5]
for i in range(len(l)//2):
    l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
print(l)

#Remove duplicates from a list.
l=[1,1,3,4,4,5,2,6,6]
l1=[]
for i in l:
    if i in l1:
        continue
    else:
        l1.append(i)
print(l1)

#Find the second largest number in a list.
l=[1,7, 3, 4, 5, 2, 6]
maxi=float('-inf')
second_maxi=float('-inf')
for num in l:
    if num > maxi:
        second_maxi = maxi
        maxi = num
    elif num > second_maxi and num < maxi:
        second_maxi = num
print(f"second maximum value in the list is {second_maxi}")

#Merge two lists alternately.
l1=[1,2,3,4]
l2=[5,6,7,8,9,10]
new_list=[]
i=j=0
while i < len(l1) or j < len(l2):
    if i <len(l1):
        new_list.append(l1[i])
        i+=1
    if j < len(l2):
        new_list.append(l2[j])
        j+=1
print(new_list)

#Rotate a list by k positions.
l = list(map(int,input("enter the list elements seperated by spaces: ").split()))
k=int(input("position of rotation: "))
direction=input("enter direction: ").lower()
rotated_list=[]

if not l:
    print("empty list please enter list!")

else:
    k %= len(l)
    if direction == "left":
        rotated_list=l[k:]+l[:k]
    elif direction == "right":
        rotated_list=l[-k:]+l[:-k]
    else:
        print('invalid direction')
        rotated_list=None
    
    if rotated_list is not None:
        print(rotated_list)


#Check if a list is sorted.
l=[1,2,3,4,5,6]
f=0
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        f=1
        break
if f==0:
    print("sorted")
else:
    print("unsorted")

#Flatten a nested list.
nes_l=[[1, 2, 3, 4], [3, 4.9], [5, 6]]
flat_l=[]
for lis in nes_l: 
    for item in lis:
        flat_l.append(item)
print(flat_l)

#Find all pairs with sum equal to k
l = list(map(int,input("enter list element sep by spaces: ").split()))
k=int(input("enter number to list pairs equal to it: "))
s=set()
for i in range(len(l)):
    for j in range(len(l)-1):
        if i != j :
            if l[i]+l[j]==k:
                s.add(tuple(sorted((l[i], l[j]))))  #sorted function gives out a list thats what converted to a tuple
print(s)

#Create a copy of a list and prove it is a deep copy.
#copy(points at same list)
l=[1,2,3,4,5,6]
l1=l
l1[1]=30
print(l,"\n",l1)
#output
# [1, 30, 3, 4, 5, 6] 
# [1, 30, 3, 4, 5, 6]

#shallow copy
l=[1,2,3,4,5,6]
l1=l[:] #l.copy() or copy.copy(l)
l1[1]=30
print(l,"\n",l1)
#output
# [1, 2, 3, 4, 5, 6] 
# [1, 30, 3, 4, 5, 6]

#shallow copy form reference to the child object(points at same sub list)
l=[[1,2],[3,4],[5,6]]
l1=l[:]
l1[0][0]=33
print(l,"\n",l1)
# output
# [[33, 2], [3, 4], [5, 6]] 
# [[33, 2], [3, 4], [5, 6]]

#deep copy
import copy
l=[[1,2],[3,4],[5,6]]
l1=copy.deepcopy(l)
l1[0][0]=33
print(l,"\n",l1)
# output
# [[1, 2], [3, 4], [5, 6]] 
# [[33, 2], [3, 4], [5, 6]]

#Sort a list without using sort()
l=[1,7, 3, 4, 5, 2, 6]
for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j+1]<l[j]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)




# ===================================
#        TUPLES & SETS
# ===================================
#Convert a list to a tuple and vice versa.
l=[1,7, 3, 4, 5, 2, 6]
t=tuple(l)
l=list(t)
print(l,"\n",t)

#Check if an element exists in a tuple.
t=tuple(map(int,input("enter elements of tuple: ").split()))
s=int(input("enter element to search: "))
if s in t:
    print(f"yes {s} is in tuple {t} at index {t.index(s)}.")
else:
    print(f"No element {s} is not in tuple {t}")

#Find union, intersection, difference of two sets.
s1={1,2,3,4}
s2={5,6,7,8}
print(f"union of set 1 {s1} and set 2 {s2} is {s1 | s2}")
print(f"Intersection of set 1 {s1} and set 2 {s2} is {s1 & s2}")
print(f"the difference of set 1 {s1} and set 2 {s2} is {s1.difference(s2)}")

#Find all unique characters in a string using a set
str='mississippi'
sets=set(str)
print(sets)

#Convert a set to a sorted list
s={8, 3, 9, 6, 2, 7, 4, 10, 1, 5}
l=list(sorted(s))
print(l)

#Find the symmetric difference of two sets
s={1,2,3,4}
s1={3,4,5,6}
print(f"set difference is {(s | s1).difference(s & s1)}")

# ===================================
#        DICTIONARIES
# ===================================

#Create a dictionary from two lists.
l=['apple','banana','cherry']
l1=[1,2,3]
dic={}
for i in range(len(l)):
    dic[l[i]]=l1[i]
print(dic)

#       (or)

l=['apple','banana','cherry','plum']
l1=[1,2,3]
dic={}
for i in range(len(l)):
    if i<len(l1):
        dic[l[i]]=l1[i]
    else:
        dic[l[i]]=None
print(dic)

#       (or)
l=['apple','banana','cherry']
l1=[1,2,3]
dic=dict(zip(l,l1))
print(dic)

#Count frequency of elements in a list using dictionary.
l=[1,1,2,3,4,4,4,5,2,6,5,4]
dic={}
for i in l:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

#Find the key with the maximum value.
dic={1: 2, 2: 2, 3: 1, 4: 4, 5: 2, 6: 1}
maxi = float('-inf')
for key in dic.keys():
    if dic[key]>maxi:
        maxi = dic[key]
        max_key=key
print(f"The key {max_key} has maximum value {maxi} in dictionary {dic}")

#Reverse keys and values of a dictionary.
dic={'apple':1,'banana':2,'cherry':3}
swap_dic={}
for key,val in dic.items():
    swap_dic[val]=key
print(swap_dic)

#Merge two dictionaries.
cl1={'math':40,'chem':45}
cl2={'chem':50,'phy':33}
merge_cl=cl1 | cl2
print(merge_cl)

#Remove a key safely from dictionary.
dic={'math': 50, 'chem': 50, 'phy': 33}
dic.pop('phy', None)
print(dic)

#Check if a key exists.
n=int(input('enter tot number of key value pairs: '))
dic={}
for i in range(n):
    key=input("enter keys(string datatype): ").lower()
    dic[key]=int(input('enter values(int format): '))

search_key=input('enter key to search: ').lower()
if search_key in dic:
    print('yes key is present')
else:
    print('no key is not present')

#Sort dictionary by keys.
my_dict = {"year": 1964, "brand": "Ford", "model": "Mustang"}
l=sorted(my_dict.keys())
key_sort_dic={}
for i in l:
    key_sort_dic[i]=my_dict[i]
print(key_sort_dic)

#       (or)
my_dict = {"year": 1964, "brand": "Ford", "model": "Mustang"}
key_sort_dic = dict(sorted(my_dict.items()))
print(key_sort_dic)

#Sort dictionary by value
d={'apple':3,'banana':1,'cherry':2}
d_val=sorted(d.items(), key=lambda item : item[1])
print(d_val)

##Find sum of all values in dictionary
d={'apple':3,'banana':1,'cherry':2}
sums=0
for i in d.values():
    sums+=i
print(sums)

#Convert dictionary values to a list.
d={'apple':3,'banana':1,'cherry':2}
l=[]
for i in d.values():
    l.append(i)
print(l)

#Create nested dictionary for student data.
n= int(input('enter number of students: '))
student_data={}
for i in range(n):
    key=input(f"enter student {i}'s name: ")
    data={}
    data['age']=int(input(f"ener the {key}'s age:" ))
    data['marks']=int(input(f"enter {key}'s marks: "))
    student_data[key]=data
print(student_data)

#Access and update nested dictionary values.
student_data = {
    'student1': {'name': 'Alice','age': 20,'grade': 'A',},
    'student2': {'name': 'Bob','age': 21,'grade': 'B'}
}
student_data['student1']['grade']='B'
print(student_data)

#Delete all items from a dictionary.
d={'apple':3,'banana':1,'cherry':2}
print(d.clear())

#Find common keys between two dictionaries.
d={'a':1,'b':2,'c':3}
d1={'b':4,'d':5}
print(d.keys() & d1.keys())

# ===================================
#        LOOPS (for / while)
# ===================================

#Find factorial of a number.
n=int(input('enter number: '))
fac=1
if n==0 | n==1:
    print(f"The factorial of {n} is {fac}")
elif n <0:
    print('please enter a positive number!')
else:
    for i in range(2,n+1):
        fac*=i
    print(f"The factorial of {n} is {fac}")

#Generate Fibonacci series.
n=int(input('enter the number till where you want the fibonacci series to be: '))
a,b=0,1
print(a,b, end=' ')
for i in range(2,n):
    temp=b
    b=a+b
    a=temp
    print(b,end=' ')

#Count digits in a number.
n=int(input('enter a huge number: '))
count=0
while n:
    n=n//10
    count+=1
print("Total number of digits in {n} is {count}")

#Reverse a number.
n=int(input('enter a two or more digit number: '))
r=0
while n:
    a = n % 10
    r = r*10 + a
    n = n//10
print(f'reverse is {r}')

#Check whether a number is prime.
n=int(input('enter a number: '))
if n == 1:
    print("non prime")
else:
    f=1
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            f=0
    if f==1:
        print('Prime')
    else:
        print('Non Prime')


#Print all prime numbers in a range
n=int(input('enter a number: '))
if n<=1:
    print("no prime number in the range of 0 to",n)
else:
    for i in range(2,n+1):
        f=1
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                f=0
        if f == 1:
            print(i,end=' ')

#Find GCD of two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)

#       (or)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

while y != 0:
    x, y = y, x % y

print(x) 

#Find LCM of two numbers.
import math
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

lcm = (x*y)//math.gcd(x,y)
print(lcm)

#Check Armstrong number.
n=int(input('enter a number:'))
num=n
arm=0
while n:
    a = n % 10
    arm+=(a**3)
    n=n//10
if num == arm:
    print(f'{num} is an armstrong number!')
else:
    print(f'{num} is not an armstrong number!')

#Check perfect number.
n = int(input('enter the number: '))
per_num=0
for i in range(1,n):
    if n % i == 0 :
        per_num+=i
if n == per_num:
    print(f'{n} is a perfect number!')
else:
    print(f'{n} is not a perfect number')

#patterns 
#1. Square Pattern 
for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()

#2. Right-angled triangle
for i in range(5):
    for j in range(i+1):
        print('*',end=' ')
    print()

#3. Inverted right triangle
for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print() 

#4. Pyramid pattern
for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)

#5. Inverted pyramid
for i in range(5):
    print(' '*i +'* '*(5-i))

#6. Floyd’s triangle
j=1
for i in range(5):
    for k in range(i+1):
        print(j,end=' ')
        j+=1
    print()

#7. Full pyramid
for i in range(1, 5):
    print(' ' * (5 - i) + '*' * (2*i - 1))

#8. Diamond pattern
for i in range(1,5):
    print(' '*(5-i-1)+'*'*(2*i-1))
for i in range(3, 0, -1):
    print(' ' * (5 - i-1) + '*' * (2*i - 1))

#9. Pascal’s triangle
for i in range(5):
    print(11**i)

#10 Hollow square
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()

#11. Hollow pyramid
n= int(input('enter a number: '))
for i in range(1,n+1):
    for j in range(2*i-1):
        if j == 0:
            print(' '*(n-i-1)+'*',end='')
        elif j==2*i-2 or i==n:
            print('*',end='')
        else:
            print(' ',end='')
    print()
        

#12. Butterfly pattern

# ======================================================
#        break, continue, pass (CONTROL FLOW)
# ======================================================

#Stop loop when number becomes greater than 50.

for i in range(45,60):
    if i >50:
        break
    else:print(i)

#Skip multiples of 3 while printing numbers.
for i in range(20):
    if i % 3 == 0:
        pass
    else:
        print(i)

#Find first number divisible by 7 in a list.
for i in range(10,30):
    if i % 7 == 0:
        print(i)
        break

# Print numbers until user enters 0.
while True:
    n =int(input('enter a number(entr zero to stop entering further!):'))
    if n == 0:
        break
    else:
        print(n)

# ===================================
#        ADVANCED LOOPS
# ===================================

#Generate squares of even numbers using comprehension.
square=[i*i for i in range(1,11) if i % 2 == 0]
print(square)

# Create a list of vowels from a string.
vowel=[i for i in 'hello my name is laptop!'.lower() if i in ['a','e','i','o','u']]
print(vowel)

#Flatten a 2D list using comprehension.
l=[[1,2,3],[4,5,6],[7,8,9]]
flatten=[j for i in l for j in i]
print(flatten)

#Create a dictionary using comprehension.
squares={i : i*i for i in range(1,10)}
print(squares)

#Filter positive numbers from a list.
l=[1,-2,-4,6,7,-10,4]
l = [i for i in l if i>0]
print(l)

# Replace negative numbers with zero using comprehension.
l=[1,-2,-4,6,7,-10,4]
updated=[0 if x < 0 else x for x in l]
print(updated)

#Convert a nested loop into comprehension.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
even_squares=[i*i for j in matrix for i in j if i % 2 == 0 ]
print(even_squares)
 
#Find duplicate elements in a list
l=[1,2,2,3,4,4]
visited=set()
for i in l:
    if i not in visited:
        visited.add(i)
    else:
        print('duplicate',i)

# Find missing number in a sequence.
#for AP
ap = [2,4,6,10,12]
d = (ap[-1]-ap[0])//len(ap)
a = ap[0]
for i in range(0,len(ap)):
    expected=a+i*d
    if ap[i] != expected:
        print(f"missing value is {expected} at index {i}")
        break

#for GP 
gp=[3, 6, 24, 48]
a=gp[0]
r=int((gp[-1]/gp[0])**(1/len(gp)))
for i in range(len(gp)):
    expected=a*(r**i)
    if gp[i] != expected:
        print(f'missing value is {expected } at index {i}')
        break


#Check if list contains consecutive numbers.
l=[1,2,3,4,6,7,8]
for i in range(len(l)-1):
    if l[i+1]-l[i] != 1:
        print('list of numbers is not in consecutive order!')
        break

#Group words by their length.
words = ["apple", "bat", "cat", "banana", "dog", "ant"]
group_words={}
for i in words:
    if len(i) not in group_words:
        group_words[len(i)]=[i]
    else:
        group_words[len(i)].append(i)
print(group_words)

#Find first non-repeating character in a string.
s="hello it's been long since i last saw you"
for i in s:
    if i != ' ' or s.count(i) == 1:
        print(i)
        break

#       (or)
from collections import Counter

s = "hello it's been long since i last saw you"

freq = Counter(s)

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break


# Find longest common prefix in a list of strings.
strings = ["flower", "flow", "flight"]
prefix = ""

for idx in range(len(strings[0])):
    char = strings[0][idx]

    for word in strings[1:]:
        if idx >= len(word) or word[idx] != char:
            print(prefix)
            exit()

    prefix += char

#       (or)
strings = ["flower", "flow", "flight"]

prefix = ""

for chars in zip(*strings):
    if len(set(chars)) == 1:
        prefix += chars[0]
    else:
        break

print("Longest common prefix:", prefix)


# Rotate matrix by 90 degrees. (transpose + reverse)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n=len(matrix)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for row in matrix:
    row.reverse()
print(matrix)

# Check if two dictionaries are equal.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'b': 2, 'a': 1}

if len(dict1) != len(dict2):
    print(f"{dict1} and {dict2} are not equal!")
else:
    f = 1
    for key in dict1:
        if key in dict2:
            if dict1[key] != dict2[key]:
                f = 0
    if f == 1 :
        print(dict1,dict2,"are equal!")
            

# Implement bubble sort.
l=[5, 1, 4, 2, 8]
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

# Implement binary search.
l=[5, 1, 4, 2, 8, 3, 6, 9, 7, 10]
n=len(l)
num=int(input('enter the number(1-10) to search: '))
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
for i in l:
    if num < l[n//2]:
        l=l[:n//2]
    else:
        l=l[n//2:]
    if n == i:
        print('found')
    else:
        print('searching....')
#3333333333333333333333333333333333333333333333333333333333333333
#3333333333333333333333333333
#3333333333333333333333333333
#3333333333333333333333333333

l=[5, 1, 4, 2, 8, 3, 6, 9, 7, 10]
num = int(input('enter number to search from 1 to 10: '))
l=l.sort()
low = 0
high=len(l)-1
f = 0
while low <= high:
    mid=(low + high)//2
    if l[mid] == num:
        f = 1
        break
    elif num < l[mid]:
        high = mid - 1
    else:
        low = mid + 1
if f == 1:
    print(f'{num} is present at index {mid}')
else:
    print(f'{num} is not present in series!')  