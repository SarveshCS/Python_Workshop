# Membership Operators
list1 = [1, 2, 3, 4, 5]
tuple1 = (1, 2, 3, 4, 5)
string1 = "Hello"

print("Membership Operators:")
print("Is 3 in list1?", 3 in list1)
print("Is 6 in list1?", 6 in list1)
print("Is 3 not in list1?", 3 not in list1)
print("Is 'H' in string1?", 'H' in string1)
print("Is 'h' in string1?", 'h' in string1)

# Identity Operators
a = 10
b = 10
c = a
d = 20
e = 10.0

print("\nIdentity Operators:")
print("Is a identical to b?", a is b)
print("Is a identical to c?", a is c)
print("Is a identical to d?", a is d)
print("Is a identical to e?", a is e)
print("Is a not identical to d?", a is not d)