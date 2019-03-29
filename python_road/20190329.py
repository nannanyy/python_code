#L局部作用域->E闭包函数外的函数中->G全局作用局->B内置作用域，builtins内置作用域
import builtins
print(dir(builtins))    #预定义的内置变量

#global nonlocal，内部作用域修改外部作用域的关键字
num = 1
def fun1 ():
    global num
    print(num)
    num = 123
    print(num)
fun1()
print(num)

def outer():    #修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
    num = 10


    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()

a = 10
def test(a):    #a作为全局变量
    a = a+1
    print(a)
test(a)