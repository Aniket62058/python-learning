print("hello world")

# Type Conversion
a = int(10.6)
print(a)  # a=10
a = float(10)
print(a)  # a=10.0

s1 = "String's demo"  # Double quotes are useful if single quote is literally part of the String

print(s1)  # s1 = String's demo

# s2 = 'String's demo'  # This would cause an error because the single quote would end the String
#  and python does not know what to do with the rest


s = input('Enter your name\n')  # for taking input as string
print("Hi " + s)

a = int(input("Enter an integer number\n"))  # for taking input as int
print("Entered number was : ", a)

a = float(input("Enter a float number\n"))  # for taking input as float
print("Entered number was : ", a)
