#if-elif-else条件语句
var1 = 100.22
if var1:
    print("1 - if表达式条件为 true")
    print(var1)
var2 = 0
if var2:
    print("2 - if 表达式条件为 true")
    print(var2)
print("Good bye!")

print(0 == 5)
x = 2
print(x == 2)

age = int(input("请输入你家狗狗的年龄： "))
print("")
if age < 0:
    print("Are you kiding me?")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄：", human)
#退出提示
input("点击enter退出")

num = int(input("请输入一个数字： "))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2，不可以整除3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，不可以整除2")
    else:
        print("你输入的数字不可以整除2和3")


#while
number = 7
guess = -1
while guess != number:
    guess = int(input("请输入你猜的数字 "))
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字太小了 ...")
    elif guess > number:
        print("猜的数字大了...")



#循环语句
n = 100
sum1 = 0
counter = 1
while counter <= n:
    sum1 = sum1 + counter
    counter += 1
print("1 到 %d 之和为： %d" % (n, sum1))



count = 0
while count < 5:
    print(count, "小于5")
    count = count + 1
else:
    print(count, "大于或等于5")

flag = 0
while flag:
    print("欢迎学习Python")
print("Good bye")


#for语句，遍历,range,break,continue,pass
testtechnology  = ["yewu", "jiekou", "zidonghua", "xingnneg"]
for x in testtechnology:
    print(testtechnology)
for test in testtechnology:
    if test == "zidonghua":
        print("欢迎学习接口测试")
        break
    print("循环数据" + test)
else:
    print("没有循环数据！")
print("完成循环！")

for i in range(5):
    print(i)
for i in range(0, 3, 10):
    print(i)
for i in range(-10, -100, -30):
    print(i)
for i in range(len(testtechnology)):
    print(i, testtechnology[i])

list(range(5))
print(list)

for letter in "confindence":
    if letter == 'f':
        break
    print("当前字母： ", letter)
var4 = 10
while var4 > 0:
    print('当前变量值为：var4')
    var4 = var4 -1
    if var4 == 5:
        break
print("Good bye")




#质数?
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        print(n , '是质数')

for letter in 'whyhowok':
    if letter == 'o':
        pass
        print('执行pass块')
    print('当前字母：',letter)
print("Good bye!")




var3 = 11
while var3:
    num = int(input("输入一个数字 ："))
    print("你输入的数字是：", num)
print("Good buy!")









