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
    # print(code_obj)
    urls = code_obj.find_all('a')      #用find_all方法，根据共有标签a，找到源码中所有URL
    print(urls)                        #打印list格式
    for u in urls:
        print(u)                       #打印格式好看~
    return


url = "https://baidu.com"              #定义变量data
code = hqyuanma(url)                   #调用获取源码方法
jiexi(code)                            #调用解析HTML，返回HTML中所有URL

