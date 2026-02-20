# ProjetoBasico-CFA

![](./4929270778520341423.jpg)


Esta é a documentação do dispositivo que usaremos em CFA durante algum tempo com o objetivo de entender como programar e como construir dispositivos. Existem algumas maneiras para aproveitá-la:

1. Saber quais são as funcionalidades implementadas, em nível bastante abstrato;
2. Como ligar o dispositivo e acessar suas funcionalidades;
3. Replicar o dispositivo;
4. Compreender a estratégia de documentação (ex.: para reaplicá-la para um outro dispositivo);
5. Compreender em que ordem (ou se existe ordem) para desenvolver este dispositivo;
6. Compreender como partes do software/hardware funcionam (ex.: para reusar essas partes);

## Quais são as funcionalidades implementadas

O dispositivo está programado para conectar-se a um ponto de acesso WiFi e permitir que, através do navegador web, seja possível:
  
- acender/apagar um LED embutido no dispositivo;
- apresentar mensagens em sua tela;
- acessar uma interface em linha de comando (CLI) e nela executar comandos Python;
- criar, ler, gravar, apagar arquivos armazenados no dispositivo; 
- essas funcionalidades podem ser usadas por vários usuários simultaneamente.


## Como ligar o dispositivo e acessar suas funcionalidades

Antes de ligar o dispositivo, criar uma rede WiFi de 2.4GHz com nome **lab8** e senha **lab8arduino**. Isto pode ser feito ajustando um ponto de acesso WiFi ou configurando um telefone celular como hotspot WiFi.

Ligar o dispositivo conectando-o, através do conector USB, a um carregador ou a um computador (talvez seja possível conectar a um telefone celular através de um cabo OTG).

Quando ligado e pronto para operar um número como 192.168.0.6 é mostrado na tela do dispositivo. Caso, depois de ligado por mais de 30 segundos, a tela não apresentar nada, ou ser preenchida com letras, ou apresentar o número 0.0.0.0, há algum problema. Neste ponto, o que é possível fazer com o que se sabe até agora é checar se a rede WiFi foi criada corretamente e reiniciar o dispositivo, desligando-o, esperando uns segundos e religando.

Com o dispositivo ligado e pronto para operar, usar um computador ou telefone celular, abrir o navegador web e digitar o endereço `http://dv01.local:5000/`. Uma tela como a da foto abaixo deve aparecer no navegador:
  
![](./Captura%20de%20tela%20de%202026-02-11%2018-55-08.png)


As rotas que podem ser acessadas no servidor são:

| rota | efeito no navegador | efeito no dispositivo |
| --- | --- | --- |
| / | mostra a página index.html | - |
| /hello | mostra o texto 'hello from dv01.local' | - |
| /led | mostra o texto on caso o LED esteja apagado, off caso o LED esteja aceso | - |
| /led/on | mostra o texto on | apaga o LED |
| /led/off | mostra o texto off | acende o LED |
| /message | mostra o texto que está sendo mostrado no display | - |
| /message?text="xxx" | mostra o texto passado como argumento em 'text' | mostra no display o texto passado como argumento em 'text' |
| /www/webrepl/webrepl.html | Mostra a página para acesso a interface de comando (REPL) | para conectar, substituir o número da porta de 5000 para 8266 na caixa de texto ao lado do botão connect e, em seguida, apertar o botão|

Experimente as funcionalidades.

## Como replicar o dispositivo

### Materiais e ferramentas

- Computador com Linux, acesso à internet e porta USB 
- Cabo de dados para conectar o computador ao dispositivo
- Dispositivo: ESP32-C3 supermini com display embutido de 0.42" 

### Procedimento

1. Instalar o firmware micropython - veja https://www.micropython.org/download/ESP32_GENERIC_C3/
   - lembre de dar ao seu usuário acesso à porta USB com o comando `sudo usermod -a -G dialout <username>` (https://support.arduino.cc/hc/en-us/articles/360016495679-Fix-port-access-on-Linux)
   - as portas existentes são criadas no diretório `/dev` e têm o prefixo tty. Geralmente `ttyACM?` ou `ttyUSB?`;
2. Testar o envio de comandos python usando a IDE Thonny;
6. Executar no dispositivo, através do Thonny: `import webrepl_setup`. Isto habilita webREPL (https://github.com/micropython/webrepl)
5. Sair do Thonny
2. Instalar `rshell` no desktop - execute `pip3 install rshell` - veja https://github.com/dhylands/rshell
3. Clonar este repositório no desktop - `git clone https://github.com/FNakano/ProjetoBasico-CFA.git`
4. Copiar o conteúdo da pasta `src` para o dispositivo;
   1. Com o dispositivo conectado ao computador através da porta USB, execute `rshell --port /dev/ttyACM0` se necessário, ajuste a porta;
   2. No rshell execute `cp -r src/* /pyboard`
5. Reiniciar o dispositivo, deve funcionar como em https://github.com/FNakano/ProjetoBasico-CFA?tab=readme-ov-file#como-ligar-o-dispositivo-e-acessar-suas-funcionalidades

## Como o dispositivo foi feito, como os pacotes e o programa estão organizados

O ESP32-C3 supermini com display embutido de 0.42" 
é uma placa de desenvolvimento, ou placa microcontroladora, ou placa, ... baseada no microcontrolador ESP32-C3. O microcontrolador contém um processador com arquitetura RISC-V e controladores de periféricos como WiFi, Bluetooth, SPI, I2C, UART, ... (https://documentation.espressif.com/esp32-c3_datasheet_en.pdf). Nos ESP32 os pinos são mapeados através de multiplexes de maneira que a atribuição de pinos pode ser modificada. Essa placa em particular vem com um display OLED com driver SSD1306 que implementa o protocolo I2C, conectado aos pinos 5 e 6 da placa microcontroladora. Também tem um LED conectado ao pino 8.

A placa microcontrolada recebe programas através da porta USB (ié, a placa contém componentes adicionais, conexões e programas que permitem transmissão de dados e programas entre a UART do microcontrolador e a porta USB do computador). Quando o programa transmitido é o firmware MicroPython, este é construído de maneira a controlar o microcontrolador.

MicroPython, como outros Python, executa um *Read Evaluate Print Loop - REPL* que recebe comandos através da UART/porta USB, executa os comandos, envia os resultados pela UART/porta USB em um loop. É peculiar ao MicroPython a organização da memória FLASH que não armazena o MicroPython em um sistema de arquivos. É possível pensar que o sistema operacional tem um console/prompt Python e um sistema de arquivos.

A pessoa que programa o dispositivo usa uma IDE como Thonny para gerenciar os arquivos e editar/executar os programas.

Há dois pacotes Python de importância especial: `boot.py` e `main.py`. Os dois são executados durante o boot do firmware. Primeiro `boot.py` e depois `main.py`. Nesta placa microcontroladora, `boot.py` não pode ser interrompido pela IDE, já `main.py` pode ser interrompido pela IDE.

O projeto básico documentado aqui é composto pelos seguintes pacotes: `display.py`, `lab8.py`, `startsystem.py`, `config.py`, `httpserver.py`, `led.py`, `main.py`. Os outros pacotes podem ou não ser usados por este projeto. Os pacotes `/lib/ssd1306.py`, `/lib/microdot.py` e `aiorepl.py` são usados por este projeto mas não foram escritos no escopo deste projeto. 

`config.py` contém variáveis globais. Algumas podem ser modificadas pelo usuário, outras não. Isto é indicado dentro do arquivo.

`lab8.py` contém os comandos que devem ser executados para conexão à rede WiFi.

`httpserver.py` contém as rotas do servidor HTTP e respectivos comandos. O conteúdo estático está na pasta `www`.

`led.py` contém comandos para configuração do LED embutido.

`display.py` contém comandos e funções para configurar e usar o display OLED.

`startsystem.py` contém os comandos que agrupam as linhas (threads) de execução - a execução é assíncrona usando `asyncio`. As linhas são o servidor web e o servidor REPL.

`main.py` importa o pacote `startsystem` o que faz o programa executar.

## Compreender a estratégia de documentação

Há vários públicos que podem interessar-se em um projeto. Por exemplo, quem quer apenas saber o que o dispositivo faz, ou quem quer usar o dispositivo, ou quem quer replicar, ou quem quer dar manutenção, ... cada um desses públicos busca documentação de formas diferentes e em ordem/formato diferente.

Até onde consegui alcançar, acredito que existe como organizar a documentação de maneira que esta tenha os assuntos ordenados em ordem crescente de complexidade. Desta maneira a documentação fica organizada e os públicos conseguem escolher bem o que saltar e o que ler da documentação.

A ordem é:

1. Só saber o que o dispositivo faz;
2. Usar o dispositivo;
3. Replicar o dispositivo;
4. Saber como o particular dispositivo foi feito;
4. Saber como o particular dispositivo foi projetado;
5. Saber como o particular dispositivo foi documentado;
6. Saber como dispositivos podem ser desenvolvidos e que documentação de andamento do projeto foi gerada.


## Compreender em que ordem (ou se existe ordem) para projetar e desenvolver dispositivos;

Acredito que não exista ordem para projetar e desenvolver dispositivos. Claro que é possível usar técnicas de engenharia (de software e/ou de hardware). Essas técnicas são muito eficazes, quando se sabe o que cada parte faz, o que nem sempre é o caso. 

Quando o projeto é indefinido, convém usar uma parte do tempo buscando componentes e funcionalidades interessantes e anotando o resultado da exploração, talvez, em um diário. Algo parecido foi feito em https://github.com/FNakano/CFA/tree/master/projetos/py-understandSH1106

Quando esta exploração é feita com o objetivo de *construir algo interessante*, em algum momento, somos capazes de compor parte dos elementos buscados, chegando a *algo interessante*. Cabe considerar os requisitos dados por quem encomendou o projeto.

O *interessante* pode ser *algo relevante para uma comunidade científica*, aí estamos falando de pesquisa, revisão sistemática, ...

Também pode ser inspirador ver projetos feitos por outros grupos em anos anteriores em https://github.com/FNakano/CFA há uma relação de projetos de anos anteriores e respectivos links.

## Compreender como partes do software/hardware funcionam (ex.: para reusar essas partes);

### asyncio

https://docs.micropython.org/en/latest/library/asyncio.html

### aiorepl

https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl

### microdot

https://microdot.readthedocs.io/en/latest/

### display OLED

https://github.com/FNakano/CFA/tree/master/projetos/py-understandSH1106


## Características notáveis (para mim) do dispositivo

Uso um ESP32-C3 super mini com display OLED de 0.42". Abreviando, placa microcontroladora.

A placa microcontroladora tem display e um LED. 

O microcontrolador se comunica com o display através de um (chip) controlador (driver) SSD1306. O protocolo de comunicação é I2C. Os pinos do display:microcontrolador são SDA:5 SCL:6

o LED está ligado ao pino 8 (GPIO8), é um LED comum (não é RGB, não é endereçável). O comando `.on()` apaga o LED e o comando `.off()` acende o LED.

## Características notáveis (para mim) do projeto básico

O projeto básico é multithread através de `asyncio`. Com isto, é possível executar servidor HTTP e servidor WebREPL simultaneamente. Com isto, em tese, algumas pessoas podem navegar pelas páginas armazenadas no dispositivo enquanto outras podem modificar/executar programas, simultaneamente. (note as camadas na narrativa)

