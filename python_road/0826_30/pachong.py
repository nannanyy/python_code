#爬虫demo
#思路：http协议--请求--数据解析--去重--数据存储--多线程

import urllib.request
from bs4 import BeautifulSoup


class pachong0:


    def __init__(self,new_url):
        self.url = new_url
        print("----init方法----")


    def true_url(self,url):       #校验是否可访问URL
        if "http" in url:
            return True
        else:
            return False


    def huoqu_yuanma(self,url):          #请求url，获取源码
        re = urllib.request.urlopen(url,timeout=5)
        yuanma = re.read().decode()
        #print(yuanma)
        return yuanma


    def jiexi_yuanma(self,yuanma):     #数据解析,<area  xx="xx" href="url"
        code_urls = BeautifulSoup(yuanma,"html.parser")
        tags = code_urls.find_all('a')
        urls = set()
        for tag in tags:
            url = tag['href']
            urls.add(url)
        print(urls)                     #可去重
        print(len(urls))
        is_url = set()
        for url in urls:
            if self.true_url(url):
                is_url.add(url)
        return is_url


#测试验证
url = "https://baidu.com"
test = pachong0(url)
cods = test.huoqu_yuanma(url)
jiexi_yuanma = test.jiexi_yuanma(cods)
print(jiexi_yuanma)
print(len(jiexi_yuanma))


