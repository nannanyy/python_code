class Person:

    def __init__(self, n, g, a):    # 构造函数，_私有方法，没有真正的私有化，不管是方法还是属性，为了编程的需要，约定加了下划线 _ 的属性和方法不属于API，不应该在类的外面访问，也不会被from M import * 导入
        self.name = n
        self.gender = g
        self.age = a

    def speak(self):
        print(" %s 说：我是 %s。" % (self.name, self.gender))
        # 光标选中后，option+enter+file格式化
        # Refactor多个重命名


# 实例化类
p = Person('yy', '女', 16)

# p.speak()
p.__init__('yy', '女', 16)
