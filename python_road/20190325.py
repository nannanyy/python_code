#列表
list1 = ["LAG", 786, 2.32, 'WHAT', 70.2]
tinylist = [123, 'WHAT']
print(list1)
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(tinylist * 2)
print(list1 + tinylist)

a = [1, 2, 3, 4, 5, 6, 6, 6]
a[0] = 9
print(a[0])
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []
print(a)
print(a[:: 2])

#元组，不能修改
tuple1 = ('love', 786, 2.23, 'like', 70.2)
tuple2 = (123, '123', 123)
print(tuple1)
print(tuple2[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tuple2 * 2)
print(tuple2 + tuple1)
tup = ()
tup2 = (112,)
print(tup, tup2)

# 集合由一个或数个形态各异的大小整体组成，构成集合的事物或对象称作元素或是成员
s1 = set()
s2 = set('123')
student = {'Tom', 'Jim', 'Nannan', 'yy', 'Sloriac'}
print(student, s2)
if 'Jim' in student:
    print('Jim 在集合中')
else:
    print('Jim 不在集合中')
s3 = set('123456abcDEA')
s5 = set('c4aB566')
print(s3, s5)
print(s3 - s5)
print(s3 | s5)
print(s3 & s5)
print(s3 ^ s5)


# 字典，列表是有序的对象集合，字典是无序的对象集合。区别：字典当中的元素是通过键来存取的，而不是通过偏移存取
dict1 = {}
print(dict1)
dict1['one'] = "1 - 菜鸟教程"
dict1[2] = "2 - 菜鸟工具"

dict2 = {'name': 'nan', 'code': 1, 'site': 'www.home.com'}
print(dict1['one'])
print(dict1[2])
print(dict2)
print(dict2.keys())
print(dict2.values())
dict3 = ([('Aa', 1), ('Bb', 2), ('Cc', 3)])
print(dict3)
print({x: x ** 2 for x in (2, 4, 6)})
dict5 = dict(A=1, B=2, C=3)
print(dict5 )

print(tuple('z12'))
