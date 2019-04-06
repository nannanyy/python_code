import random
import urllib.request
from bs4 import BeautifulSoup


def request_url(url):
    re = urllib.request.urlopen(url, timeout=1)
    content = re.read().decode()
    return content


def parse_content(content):
    res = float(content)
    return res


def request_server(op, param1, param2):
    base_url = 'http://localhost:8000/?'
    url = base_url + 'op=' + op + '&param1=' + str(param1) + '&param2=' + str(param2)
    print(url)
    content = request_url(url)
    print('content:', content)
    res = parse_content(content)
    return res


def test(op, num):
    a = 0
    unpassed_expamles = set()
    for i in range(num):
        data = [random.random(), random.uniform(-100000000, 100000000), random.randint(-100000000, 100000000)]
        param1 = random.choice(data)
        param2 = random.choice(data)
        if op == "add":
            right_res = param1 + param2
        elif op == "sub":
            right_res = param1 - param2
        elif op == 'mul':
            right_res = param1 * param2
        elif op == 'div':
            right_res = param1 / param2
        else:
            print("op参数错误")
            return None
        server_res = request_server(op, param1, param2)
        print('测试'+op+':', param1, param2, '期望：'+str(right_res), '验证:'+str(server_res))
        if right_res == server_res:
            print("测试通过\n")
            a += 1
        else:
            print("测试不通过\n")
            unpassed_expamles.add((op, param1, param2, right_res, server_res))
    print("测试通过率", a/num)
    print("未通过样本", unpassed_expamles)


test('add', 10)
test('sub', 10)
test('mul', 10)
test('div', 10)
