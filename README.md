# Wsgi-Python
Entendendo sobre servidores web com interfaces para frameworks e aplicações com python
<hr>

links como referência: https://pypi.org/project/waitress/  e https://docs.pylonsproject.org/projects/waitress/en/stable/arguments.html

<hr>

<h1>passo a passo de como executar a aplicação</h1>

# passo 1

CRIE SEU AMBIENTE VIRTUAL => python3 -m venv nome-do-seu-ambiente-virtual 

# passo 2

<p>INSTALE O gunicorn para exercutar o servidor => pip install gunicorn</p>
<p><i>Observação:<i/> Para sitemas operacionais windows instale o waitress => pip install waitress</p>

# passo 3

<p>Execute o comando no terminal linux ou cmd windows => gunicorn myapp.wsgi:application -b 127.0.0.1:5002(ou qualquer outra porta que você quiser)</p>
<p>Com waitress execute o comando => waitress-serve --listen=*:8000 myapp.wsgi:application</p>
