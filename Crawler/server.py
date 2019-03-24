from os import environ
from wsgiref.simple_server import make_server


def parse_args(string_arg):
    params = string_arg.split('&')
    params_dic = dict()
    for param in params:
        kv = param.split('=')
        assert len(kv) == 2
        k = kv[0]
        v = kv[1]
        params_dic[k] = v
    return params_dic


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    a = environ['QUERY_STRING']
    b = parse_args(a)
    print(b)
    return [b'<h1>Hello, web!</h1>']


httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')

# 开始监听HTTP请求:
httpd.serve_forever()