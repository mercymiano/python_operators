# Arithmetic operators
x = 50
y = 5

#Addition 
add = x+y
# using + in strings
print ("first " + "last")
#Subtration
sub = x-y
#Multiplication
mul = x*y
#Division (float)
div1 = x/y
#Division 
div2 = x//y
#Modulus returns the remainder when the number is divided
mod = x%y

print(add)
print(sub)
print(mul)
print(div1)
print(div2)
print(mod)

#Relational operators (returns the values true or false)
a = 100
b = 110

#Greater than
print(a>b)
#Less than
print(a<b)
#Equal to
print(a==b)
#Not equal to
print(a!=b)
#Greater to or equal to
print(a>=b)
#Less than or equal to
print(a<=b)

#Logical operators returns the values true of false
z = 70
#Logical and
print(z>20 and z<71)
#Logical or
print(z<67 or z>50)
#Logical not
print(not(z>20 and z<71))

#Bitwise operators
c= 10
d= 4
#bitwise and (&)
print(c&d)
#bitwise or (|)
print(a|d)
#bitwise not -inverts all bits
print(~c)
#bitwise XNOT (^)
print(c^d)

print(c>>2)
print(c<<2)

#membership operator
x = 98, 70, 50, 90
y = 40, 80, 11, 24
# in - returns true if the value is found in the sequence
print (70 in y)
print (90 in x)
# not in -returns true if the value isn't in the sequence
print (10 not in x)

#identity operator
x1 = 67
x3 = 67
y2 = "cars"
z = "cars"
# is not - returns true if the operands are not identical
print (x1 is not z)
print (y2 is not z)
# is - returns true if the operands are identical
print (z is y2)