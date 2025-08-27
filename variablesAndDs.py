from decimal import Decimal

# to print something
print(10)

# variable declaration
length = 20  # int
height = 20.40  # float
name = "Bahubali"  # string
isValid = True  # boolean

# Arithmetic
a = 20
b = 3
print(a // b)  # 6 (floor division)
print(a**b)  # 8000 (power)

# Comparison
print(a > b)
print(a == b)

# Logical
print(a > b and b < a)
print(a > b or b > a)
print(not (a == b))


# data structures
# collection

# list
listA = [10, 20, 30]  # ordered and mutable
print(listA[1])  # 20

# tuple
tupleB = (20.34, 34.67, 20.34, 20.34, 60.34)  # ordered but immutable
print(tupleB.index(20.34))  # 0 first occurance
print(tupleB.count(20.34))  # 3

# Set
setC = {"bahubali", 200, 200, True, "bahubali"}  # set of unique values + unordered
# can't add any dictionary into a set -> error TypeError: unhashable type: 'dict'
print(setC)  # {200, True, 'bahubali'}
# print(setC[0])  # set is unordered -> error TypeError: 'set' object is not subscriptable

# Dictionary
dictD = {"name": "bahubali", "age": 28}  # keys in quotes
print(dictD["name"])

# type check
print(type(dictD))  # <class 'dict'>
print(type(dictD) == dict)  # True

# error handling with float value
floatA = 0.004
floatB = 0.004
floatSum = floatA + floatB
print(floatSum)
print(floatSum == 0.4)
# some float values like 0.1 + 0.2 then the sum will not be 0.3
# sum will be 0.30000000000000004
# to avoid such error its better to use Decimal
oddFloatA = Decimal("0.1")
oddFloatB = Decimal("0.2")
print(oddFloatA + oddFloatB)  # 0.3
