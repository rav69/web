def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    # return iter([data.encode('utf-8')])
    # return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding="utf8")]
    # return [bytes(i+'\n','ascii') for i in data.split('&')]
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body