import json

def ping_pong_app(environ, start_response):
    if environ['REQUEST_METHOD'] == 'GET' and environ['PATH_INFO'] == '/ping':
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [b'pong']
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']
    

def server_request_info(environ, start_response):
    if environ['REQUEST_METHOD'] == 'GET' and environ['PATH_INFO'] == '/info':
        method = environ['REQUEST_METHOD']
        url = environ['PATH_INFO']
        protocol = environ['SERVER_PROTOCOL']
        data = {
            'method' : method,
            'url' : url,
            'protocol' : protocol
        }
        json_response = json.dumps(data)
        start_response('200 OK', [('Content-Type', 'application/json')])
        return [json_response.encode('utf-8')]
    else:
        start_response('400 Not Found', [('Content-Type', 'text/plain')])
        return [b'Not Found']