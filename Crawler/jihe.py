
# set()是一个无序的不重复元素集合

#创建集合
jihe1 = set()
jihe2 = {'A','123','[LIST,22]','apple','草莓'}
print(jihe2)


jihe2.add('A')  #1.添加元素
print(jihe2)

jihe2.update('[1]')     #添加元素
print(jihe2)

jihe2.remove('[')   #2.移除元素，元素不存在会报错
print(jihe2)

jihe2.discard(666)  #移除元素，元素不存在不会报错
print(jihe2)

jihe2.pop()     #随机删除一个元素
x = jihe2.pop()
print(x)
print(jihe2)

jihe3 = set(('1','2'))      #在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）
print(jihe3)
jihe3.pop()
print(jihe3)

print(len(jihe3))       #3.计算集合元素个数

jihe3.clear()       #4.清空集合元素
print(jihe3)

"A" in jihe2    #5.判断元素是否在集合中存在


jihe4 = jihe2.copy()        #6.copy集合
print(jihe4)

jihe6 = {"777","333"}
jihe5 = jihe6.union(jihe2)      #7.集合合并
print(jihe5)

