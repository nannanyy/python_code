class MyClass:
    """一个简单的类实例"""
    i= 123456
    def f(self):
        return 'hello world!'

#类实例化
x = MyClass()
#访问类的属性和方法
print("MyClass类的属性i为：",x.i)
print("MyClass类的方法 f 输出为：",x.f())

"""构造方法——init——（）,在类实例化中会自动调用
self代表类的实例，而非类
self.class指向类"""
class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart
x  = Complex(3.0,-6.6)
print(x .r,x .i)

# 类的方法
class people:
    name = ''
    age = 0
    # 定义私有属性，私有属性类外部无法直接进行访问，用两个下划线开头
    ___weight = 0
    #类的方法，必须包含参数self，且为第一个参数，self代表的是类的实例，self名字可以更改不是规定死的
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.weight = w
    def speak(self):
        print("%s 说：我 %d 岁。"%(self.name,self.age))
p = people('nanan',26,120)
p.speak()

# 类的继承
class people:
    # 定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性类外部无法直接进行访问，用两个下划线开头
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说:我 %d 岁。"%(self.name,self.age))
#单继承示例
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说：我 %d 岁了，我在读 %d年级"%(self.name,self.age,self.grade))
s = student("hh",12,2,3)
s.speak()
super(student,s).speak()

#多继承
#另一个类，多继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的题目是 %s"%(self.name,self.topic))
#多重继承
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test = sample("yn",25,80,4,"Python")
test.speak()    #方法名同，默认调用的是在括号中排前的父类的方法
super(sample,test).speak()  #用子类对象调用父类已被覆盖的方法

#类的私有属性、私有方法
class Site:
    __url = ''
    def __init__(self,name,url):
        self.name = name
        self.__url = url
    def who(self):
        print('name :',self.name)
        print('url :',self.__url)
    def __foo(self):
        print('这是私有方法')
    def foo(self):
        print('这是公共方法')
        self.__foo()
x = Site('菜鸟教程','www.runoob.com')
x.who()
x.foo()
#x.__foo()   #报错，外部不能调用私有方法
#print(x.__url)  #报错，实例不能访问私有变量
#运算符重载
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d,%d)'%(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a + other.a,self.b + other.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1+v2)





