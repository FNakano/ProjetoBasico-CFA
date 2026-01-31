# ProjetoBasico-CFA

Frequentemente ocorrem erros de comunicação ao substituir o firmware micropython. Não verifiquei o motivo mas encontrei um jeito de contornar. O erro particular a que me refiro ocorre na execução de `esptool --port /dev/ttyACM0 erase_flash`, ocorre um stop interaction, como mostrado na captura de tela abaixo.
O jeito de contornar é usar Arduino IDE, configurado para programar ESP32, com um sketch básico (bare minimum) e enviá-lo para o ESP. Com isto, `esptool --port /dev/ttyACM0 erase_flash` foi executado sem erros.
