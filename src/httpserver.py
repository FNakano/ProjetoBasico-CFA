"""
O que é:
  Arquivo de configuração e execução do servidor HTTP
O que faz:
  Define rotas e as co-rotinas que são escutadas para
  atendimento das requisições (de rotas)
  Cria o servidor HTTP na variável local app
O que espera-se que esteja neste arquivo:
  Todas as definições de rotas.
"""
import config
from microdot import Microdot, send_file

app = Microdot()
config.app=app

# default route
@app.route('/')
async def index(request):
  return send_file('www/index.html')

# plain text response
@app.route('/hello')
async def index(request):
  return f"Hello from {config.myhostname}.local"

# LED

def ledtowebresponse (value):
  if (value) : return 'on'
  else : return 'off'

@app.route('/led')
async def led(request):
  return ledtowebresponse(config.led.value())

@app.route('/led/on')
async def ledon(request):
  config.led.on()
  return ledtowebresponse(config.led.value())

@app.route('/led/off')
async def ledoff(request):
  config.led.off()
  return ledtowebresponse(config.led.value())

import display
@app.get('/message')
# GET request parameter
# http://device001.local:5000/message?text="ttt zzz"
# write message text in display
# this example "ttt zzz" is displayed with double
# quotes and space but results in non-fatal error "UnicodeError:"
async def message(request):
  txt=request.args.get('text', None)
  if txt is not None :
    display.message([txt])
  return config.messages

# Static files
# https://github.com/miguelgrinberg/microdot/blob/main/examples/static/static.py
@app.route('/www/<path:path>')
async def static(request, path):
  if '..' in path:
    # directory traversal is not allowed
    return 'Not found', 404
  return send_file('www/' + path)
