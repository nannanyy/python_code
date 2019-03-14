import urllib.request

def hqyuanma(yuming):
    re = urllib.request.urlopen(yuming)
    yuanma = re.read()
    print(yuanma)
    return yuanma

hqyuanma("https://souche.com")