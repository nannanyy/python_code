#创建一个迭代器，iter(),next(iter)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return  x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
"""
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""

#生成器
import sys
def fibonacci(n):   #生成器函数 - 斐波那契函数
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)   #f是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()

