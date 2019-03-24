counter = 100
miles = 100.0
name = "rancor"
print(counter, miles, name)

a = b = c = 1
print(a, b, c)

d, e, f = 1, 2, "reboot"
print(d, e, f)

g, h, i, j = 20, 5.66, True, 4 + 3j
print(type(g), type(h), type(i), type(j))

k = 11
print(isinstance(k, int))


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

var1 = 1
var2 = 23
print(var1, var2)
del var1, var2

print(5 + 4)
print(4.3 - 2)
print(3 * 7 - 1)
print(2 / 4)
print(2 // 4)
print(17 % 3)
print(2 ** 5)

str1 = "Beautiful"
print(str1)
print(str1[0:-1])
print(str1[0])
print(str1[2:5])
print(str1[2:])
print(str1 * 2)
print(str1 + " Girl")

print('Ab\ncd')
print(r'Ab\ncd')

word = 'Python'
print(word[0],word[5])
print(word[-1],word[-6])


