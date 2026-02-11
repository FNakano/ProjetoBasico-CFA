# ProjetoBasico-CFA

Este guia ensina como o projeto básico do dispositivo que usaremos em CFA foi construído. Ele também contém a imagem do sistema de arquivos do dispositivo. Há ao menos duas maneiras (rotas) de instalar este projeto básico no dispositivo:
  
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

