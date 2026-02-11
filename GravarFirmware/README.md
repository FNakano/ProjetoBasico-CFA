# Gravar firmware

Para instalar Micropython no ESP32-C3 supermini uso as instruções em https://micropython.org/download/ESP32_GENERIC_C3/

## Erros e, quando encontro, consertos

Frequentemente (para mim) ocorrem erros de comunicação ao substituir o firmware micropython. Não verifiquei o motivo mas encontrei um jeito de contornar. O erro particular a que me refiro ocorre na execução de `esptool --port /dev/ttyACM0 erase_flash`, ocorre um stop interaction, como mostrado na captura de tela abaixo.

![](./Captura%20de%20tela%20de%202026-01-31%2010-22-37.png)


O jeito de contornar é usar Arduino IDE, configurado para programar ESP32, com um sketch básico (bare minimum) e enviá-lo para o ESP. Em o envio terminar com sucesso (ainda não vi ocorrer diferente), `esptool --port /dev/ttyACM0 erase_flash` foi executado sem erros.
