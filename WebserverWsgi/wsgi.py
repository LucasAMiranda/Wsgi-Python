import waitress

'''
def application(amb, start_response):
    with open("index.html", 'rb') as arq:
        body = arq.read()
        status = "200 ok"
        headers = [('Content-type', 'text/html')]
        start_response(status, headers)
        print(amb)
        return[body]
'''


def application(amb, start_response):
    body = "<h1>Ola mundo dos servidores web</h1><input type='text'><button>Enviar</button>".encode()
    status = "200 OK"
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    return [body]
