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

- Computador com acesso à internet e porta USB 
- Cabo de dados para conectar o computador ao dispositivo
- Dispositivo: ESP32-C3 supermini com display embutido de 0.42" 

## Como usar o dispositivo

Este guia ensina como o projeto básico do dispositivo que usaremos em CFA foi . Ele também contém a imagem do sistema de arquivos do dispositivo. Há ao menos duas maneiras (rotas) de instalar este projeto básico no dispositivo:
  
1. Instalar o firmware micropython, instalar `rshell` no desktop, clonar este repositório no desktop, copiar o conteúdo da pasta `src` para o dispositivo;
  - Característica desta maneira: o processo de instalação é mais rápido;
  - Característica desta maneira: as versões dos pacotes estão congeladas;
    - presumidamente imune a mudanças de API ou bugs introduzidos em versões mais novas;
2. Seguir passo a passo a instalação dos pacotes a partir das fontes que usei (que chamarei de fontes originais, mesmo que não sejam);
  - Característica desta maneira: permite instalar as versões mais atuais dos pacotes;
  - Característica desta maneira: o processo de instalação é mais demorado;
  - Característica desta maneira: o processo de instalação é mais detalhado/instrutivo;
  
## Características notáveis (para mim) do dispositivo

Uso um ESP32-C3 super mini com display OLED de 0.42". Abreviando, placa microcontroladora.

A placa microcontroladora tem display e um LED. 

O microcontrolador se comunica com o display através de um (chip) controlador (driver) SSD1306. O protocolo de comunicação é I2C. Os pinos do display:microcontrolador são SDA:5 SCL:6

o LED está ligado ao pino 8 (GPIO8), é um LED comum (não é RGB, não é endereçável). O comando `.on()` apaga o LED e o comando `.off()` acende o LED.

## Características notáveis (para mim) do projeto básico

O projeto básico é multithread através de `asyncio`. Com isto, é possível executar servidor HTTP e servidor WebREPL simultaneamente. Com isto, em tese, algumas pessoas podem navegar pelas páginas armazenadas no dispositivo enquanto outras podem modificar/executar programas, simultaneamente. (note as camadas na narrativa)

## Rotas

Como ainda não tenho um dispositivo funcionando, a rota 1 ainda nem está construída. Pretendo escrever o guia para a rota 2 a medida que for programando o dispositivo.

### Rota 1


### Rota 2 com comentários

1. As instruções de instalação do micropython na placa microcontroladora também apresentam os programas a instalar no desktop.
2. Micropython tem uma interface de linha de comando. No jargão, um *Read Evaluate Print Loop - REPL*. Para acessar o REPL do micropython através do desktop, um programa, como Thonny ou, pelo menos um terminal serial, é conveniente.
3. Organizar os arquivos no sistema de arquivos costuma facilitar o trabalho do programador. Micropython busca pacotes instalados no diretório corrente e no diretório `/lib` (Veja listando o atributo `sys.path` no REPL do Micropython)
<!--- 4. Uma forma de instalar pacotes na placa microcontroladora é baixando no desktop e copiar/(salvar como) usando Thonny. O (pacote de software) driver de display SSD1306 pode ser baixado de ---> 
4. Micropython tem um instalador de pacotes, chama-se `mip`. Ele pode instalar pacotes a partir da Internet, desde que haja conexão ativa. De projetos anteriores, tenho o script `lab8.py` que conecta, como cliente, a placa microcontrolada ao wifi de nome `lab8`. Sugestão: se for desenvolver em outros lugares, configure o ponto de acesso wifi desse lugar com uma rede `lab8` ou use o telefone celular como hotspot wifi. Poupará algum tempo.
5. Instale o pacote `ssd1306` com o comando `mip.install("ssd1306")` [Captura de tela](./Captura%20de%20tela%20de%202026-02-01%2010-59-25.png)
6. Teste o display importando o pacote `display.py`. Escrevi este pacote quando estava estudando o funcionamento deste display. (https://github.com/FNakano/CFA/blob/master/projetos/py-understandSH1106/src/dispssd1306b.py)
7. Instale o pacote `aiorepl` com o comando `mip.install("aiorepl")` Este pacote implementa o REPL assíncrono. [Captura de tela](./Captura%20de%20tela%20de%202026-02-01%2011-15-42.png)
8. Instale o pacote `microdot`: No browser do desktop acesse https://microdot.readthedocs.io/en/latest/intro.html , baixe o arquivo `microdot.py` e copie-o para o diretório `/lib` da placa microcontroladora. Este pacote implementa um servidor HTTP assíncrono. [Captura de tela, falha com mip.install](./Captura%20de%20tela%20de%202026-02-01%2011-22-48.png)
9. Crie, na placa microcontroladora, uma pasta para armazenar conteúdo estático do servidor web (digamos, pasta html) - pode usar Thonny para isso;

### Como as funcionalidades são implementadas

O dispositivo executa programas escritos em Python. Para isso usa o firmware Micropython (https://www.micropython.org). Existem pacotes que implementam:

- servidor HTTP assíncrono(https://microdot.readthedocs.io/en/latest/)
- interface CLI web (https://github.com/micropython/webrepl)
- Read Evaluate Print Loop (REPL) assíncrono (https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl)
- Entrada/Saída assíncrona (https://docs.micropython.org/en/latest/library/asyncio.html)
- Comunicação com display OLED (https://github.com/micropython/micropython-esp32/blob/esp32/drivers/display/ssd1306.py) 

