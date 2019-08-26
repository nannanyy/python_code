#作业：输入一个无序整数数组，调整数组中数字的顺序， 所有偶数位于数组的前半部分，使得所有奇数位于数组的后半部分
#思路：定义整数list>遍历list>条件判断偶数，存到list1>其他，存到list 2>合并list1+list2打印

'''
list = [1,10,8,7,3,29,66];
list1 = [];
list2 = [];
for i in list:
    if i%2 == 0:
        list1.insert(0,i)   #问题：列表索引定义变量，使返回结果只返回一个最终结果[66, 8, 10, 29, 3, 7, 1]，降低复杂度
    else:
        list2.insert(0,i)
    print(list1+list2)
'''

#定义类，方法实现
class Even01:       #声明类，对象

    def __init__(self,new_arr):     #__init__方法，初始化对象
        self.arr = new_arr
        print("----init方法----")

    # 定义方法
    def is_even(self,n):            #定义偶数
        return n % 2 == 0

    def number01(self):             #定义偶数奇数排序
        if len(self.arr)==0 :
            return
        i = 0
        j = len(self.arr)- 1

        while i<j :
            if(not self.is_even(self.arr[i])) and self.is_even(self.arr[j]):        #i奇数，j整数，互换
                temp = self.arr[i]
                self.arr[i] = self.arr[j]
                self.arr[j] = temp
                i += 1
                j -= 1
            elif self.is_even(self.arr[i]) and self.is_even(self.arr[j]):            #i偶数，j偶数，i++
                i += 1
            elif (not self.is_even(self.arr[i])) and (not self.is_even(self.arr[j])):#i奇数，j奇数，j--
                j -= 1
            else:         #i偶数，j奇数，i++,j--
                i += 1
                j -= 1

#测试验证
arr = [0,1,2,3,4,5,6,7,8,9,10]
test = Even01(arr)
test.number01()
for num in test.arr:
    print(str(num) + ',',end='')


















'''
#1.7
zhuanyi = r"this is a line with \n"   #r,\转义不生效
print(zhuanyi)

a = 'this'
b = 'is'
c = 'string'
print((a+" "+ b + " " + c + "  ")*3)        #+连接， *加倍
print(len(a))    #len()打印字符串长度
print(a[1:])
print(a[0])
print(a[:-1])
print(a[0:3])
print(a[0:-1:2])

#1.8
input("\n\n按下Enter键后退出")
'''