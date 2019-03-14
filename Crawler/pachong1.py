import urllib.request

def hqyuanma(url):
    re = urllib.request.urlopen(url,timeout=2)
    yuanma = re.read().decode()
    print(yuanma)
    return yuanma

hqyuanma("https://souche.com")