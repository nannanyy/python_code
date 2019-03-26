from os import environ
from wsgiref.simple_server import make_server


def op(args_dic):  # 计算器方法
    param1 = float(args_dic['param1'])
    param2 = float(args_dic['param2'])
    if args_dic['op'] == 'add':  # 加法
        return param1 + param2
    elif args_dic['op'] == 'sub':  # 减法
        return param1 - param2
    elif args_dic['op'] == 'mul':  # 乘法
        return param1 * param2
    elif args_dic['op'] == 'div':  # 除法
        return param1 / param2
    else:
        return None


def parse_args(string_arg):
    params = string_arg.split('&')
    params_dic = dict()
    for param in params:
        kv = param.split('=')
        if len(kv) == 2:
            k = kv[0]
            v = kv[1]
            params_dic[k] = v
    return params_dic


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # print(environ)
    a = environ['QUERY_STRING']
    b = parse_args(a)
    print('The parameters are:', b)
    if 'op' in b.keys():
        res = op(b)
        if res is not None:
            print("The result = ", res)
            return [str(res).encode()]
    else:
        return ['Parameter error!'.encode()]


httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()