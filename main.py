


i = 1
while i <=10:
    print(i)
    i = i + 1

print("the program is End")

i = 1
while i <=100:
    print(i)
    i = i + 3

#Loop Through a List
thislist =  ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
#Print all items by referring to their index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  thislist = ["apple", "banana", "cherry"]
  i = 0
  while i < len(thislist):
      print(thislist[i])
      i = i + 1


alist = ["cat","dog","rat"]
for x in alist:
    print(x)
age = 18
if(age >= 18):
    print("adult")
else:
    print("you are adult")

age = 40
if(age >= 40):
    print("old")
else:
    print("adul")
#List Comprehension

'''num = [1, 2, 3, 4, 5]

result = [x + x  for x in num]
print(result)'''

num1 = [1,2,3,4,5,6,7]
result = [x for x in num1 if x % 2 ==0]
print(result)

newlist = ["apple","banana","mango","cherry","kiwi"]
result = [x for x in newlist if "a" in x]
print(result)

fruits = ["apple","banana","mango","cherry","kiwi"]
result = [x for x in fruits if x !=  "banana"]

print(result)
#With no if statement:
newlist = ["apple", "banana", "cherry", "kiwi", "mango"]
result = [x for x in newlist]
print(result)









