def app(environ, start_response):
    """Simplest possible application object"""
    print(environ)
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return body