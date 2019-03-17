import urllib.request
from bs4 import BeautifulSoup   #调用bs4包的Be功能，解析源码


#定义方法，返回URL源码！
def hqyuanma(url):
    re = urllib.request.urlopen(url, timeout=2)
    yuanma = re.read().decode()
    # print(yuanma)
    return yuanma


#定义方法，解析源码！
def jiexi(yuanma):
    code_obj = BeautifulSoup(yuanma, "html.parser")     #解析
    tags = code_obj.find_all('a')      #用find_all方法，根据共有标签a，找到源码中所有URL
    urls = set()                       #创建空集合，set()
    for tag in tags:
        url = tag['href']              #提取a中URL，也可用 tag.get('href')
        urls.add(url)                  #给空集合添加元素，集合名.add(集合数据)
    print(len(urls))                   #打印集合长度
    return urls



url = "https://baidu.com"              #定义变量data
code = hqyuanma(url)                   #调用获取源码方法
urljihe = jiexi(code)                  #打印方法，得到return!!
print(urljihe)

