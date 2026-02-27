"""
O que é:
  Arquivo de definição de variáveis globais
O que faz:
  Cria variáveis globais (ao aplicativo) Algumas podem
  ser configuradas pelo usuário, outras são internas ao
  programa e são apropriadamente inicializadas durante a
  execução do programa.
O que espera-se que esteja neste arquivo:
  Definição das variáveis globais ao aplicativo.
"""

# User configured global variables (this package users may modify)
# wifi_id = 'lab8'               # nome da rede
# wifi_password = 'lab8arduino'  # senha da rede
wifi_id = 'aula'               # nome da rede
wifi_password = 'aula1234'  # senha da rede
myhostname = 'dv01'            # nome do dispositivo

# Program internal global variables (this package users should not modify)
disp=None       # handle for the display
led=None        # handle for a led
wifi_if=None    # handle for the wifi interface
app=None        # handle for Microdot application (web server)
messages=None   # message currently displayed
