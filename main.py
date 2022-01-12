# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('su')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
x = "Suraji"
print("python is " + x)

x = "apple is "
y = " Good"
z = x+y
print(z)

x = 4
y = 5
z = x + y
print(z)
x = int(1)
r = int(2.0)
z = int("3")
print(x)
print(r)
print(z)
txt = "bangladesh is my country"
print(txt.capitalize())
print(txt.upper())



x = str("s1")
y = str(4)
print(x)
print(y)
name = "BANGLADESH"
str1 = name.lower()
print(name)
print(str1)
x = "hello, word"
b = x.split(",")
print(b)
a = "hello"
b = "Word"
c = a + " " + b
print(c)
age = 32
text = "my name is panda, my age is {}"
print(text.format(age))
quantity = 3
itemno = 456
price = 34.54
myorder = " i want {} pieces of item {} for {} dollars"
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno =4
price = 82.9
myorder = "I want to pay {2} dollars for {0} per pieces of item {1}"
print(myorder.format(quantity, itemno, price))
txt = "my country name bangladesh"
x = len(txt)
print(x)
name = "hi how are you"
print(name)
print(name.startswith("hy"))
print(name.endswith("you"))
txt = "h\te\tl\tl\to"
print(txt.expandtabs(1))
print(txt.expandtabs(4))
print(txt.expandtabs(8))

name = "geeks FOR geeks"

print(name.capitalize())

# demonstration of individual words
# capitalization to generate camel case
#txt = "bangladesh is my country"
name1 = "geeks"
name2 = "f\to\tr"
name3 = "geeks"
print(name1.capitalize() + name2.capitalize() + name3.capitalize())
print(name2.expandtabs(9))


txt = " bangmadesh is my country"
x = text.find("is")
print(x)

txt = "per item {price:.2f} taka"
print(txt.format(price = 33));


num1 = 4
num2 = 6
print(f"{num1} + {num2} +  = {num1 + num2}")
num3 = "bangladesh {price} taka"
print(num3.format(price = 20))
print(num3.upper())
str1 = " bangladesh is country it is our this"
#print(str1.count("is"))
print(str1.find("l"))

txt = "Hello, welcome to my world."
y = len(txt)
print(y)
x = txt.count("w",1 ,27)

print(x)

num = "12@34.9056sd"
print(num)
print(num.isdigit())
print(num.isalpha())
print(num.isalnum())
print(num.isdecimal())



txt = "Hello World"
x = txt.strip()
print(x)


fruits = ["apple", "banana", "cherry"]
print(fruits[1])
txt = "12 + 3"
print(txt.isnumeric())

txt = " "
print(txt.isspace())

txt = "Bangladesh Is My Country!"
print(txt.istitle())
a = "bangladesh"
b = "BANGLADESH"
print(a.isupper(), b.isupper())

txt = "bangladesh"
print(txt)
print(txt.replace("bang","dhaka"))

txt = "he ll-hpr-re-you"
print(txt.split("-"))

txt = "bangladesh How country"
print(txt.partition("How"))

a = 233
b = 23
if a > b:
    print("b is the greater than a")
else:
    print("b is the not greater than a")
#python List
