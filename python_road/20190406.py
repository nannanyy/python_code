#数据结构
#list可修改，元组、字符串不可以
#list基本方法
ab = [66.25, 333, 333, 1, 1234.5, "nannan"]
print(ab.count(333), ab.count(1), ab.count("0"))

ab.insert(2, -1)
print(ab)

ab.append(333)
print(ab)

print(ab.index(333))

ab.remove(333)
print(ab)

ab.reverse() #倒叙排列列表中的元素
print(ab)

ab.remove('nannan')
ab.sort()
print(ab)

ac = list.copy(ab)
print(ac)

#将列表当作堆栈使用，后进先出，append（）进，pop（）出
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
stack.pop()
print(stack)

#将列表当队列使用，但效率不高
from collections import deque
queue = deque(["A","B","C"])
queue.append("D")
queue.append("E")
queue.popleft()
print(queue.popleft())
print(queue)

#列表推导式
vec1 = [2, 4, 6]
print([3 * x for x in vec1])
print([[x,x**2] for x in vec1])

freshfruit = [' banana','  loganberry','passion fruit ']
print([weapon.strip() for weapon in freshfruit])
print([3 * x for x in vec1 if x > 3])
print([3 * x for x in vec1 if x < 2])
vec2 = [4,3,-9]
print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])
print([vec1[i]*vec2[i]] for i in range(len(vec1)))
print([str(round(355/113,i)) for i in range(1,6)])

#嵌套列表解析
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print([[row[i] for row in matrix] for i in range(4)])
ab = [-1, 1, 66.25, 333, 333]
del ab[0]
print(ab)
del ab[2:3]
print(ab)
del ab[:]
print(ab)

#元组和序列，元组由若干逗号分隔组成
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
u= t, (1,2,3)
print(u)

#集合，无序的不重复元素集
ab = {1, 2, 2, 3, 3, 5, 6, 7, 8, 9, 0}
print(ab)
ac = {1,3,5,7,9}
print(ab - ac)
print(ab | ac)
print(ab & ac)
print(ab ^ ac)
ad= {x for x in 'abc1234567890' if x not in 'abc'}
print(ad)

#字典，set{}
tel = {'jack':4098,'sape':4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel ['irv'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)
a = dict([('a',1),('b',2),('c',3)])
print(a)

#遍历技巧
for k, v in a.items():
    print(k,v)
for i, v in enumerate(['11','22','33']):
    print(i,v)

question = ['name','quest','favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(question,answer):
    print('What is your {0}?  It is {1}.'.format(q,a))
for i in reversed(range(1,10,2)):
    print(i)
basket = ['A','B','C','D']
for f in sorted(basket):
    print(f)



