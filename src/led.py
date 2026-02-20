"""
O que é: Arquivo de configuração do hardware dos LEDs.
O que faz:
  Cria variáveis globais (ao aplicativo) para acesso aos LEDs
  Neste caso, o LED endereçável RGB conectado no pino 8 da
  placa ESP32-C3 supermini plus.
O que espera-se que esteja neste arquivo:
  Criação das variáveis e funções para uso dos LEDs.
Referências:
  https://www.w3schools.com/python/python_classes.asp
  https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

"""
from machine import Pin
import config
config.led=Pin(8, Pin.OUT)
