import requests
import re

def jiexi(url):
    content = requests.get(url).text
    print(content)

    pattern = re.compile(r'<a href=(.*？).*?title>',re.S)
    results = re.findall(pattern,content)
    print(results)
    return results

jiexi("https://baidu.com")
#return content
#jiexi("https://baidu.com")
#<a href=.*？>
##


