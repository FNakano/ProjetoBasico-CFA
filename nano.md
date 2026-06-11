# Nano

Acho que, em um texto explicativo, entender suficientemente o contexto em que o texto foi escrito é uma habilidade e 
ajustar ação ao 
contexto a fim de aplicar o que foi explicado no texto é ainda outra. Informação disponível tem até demais (em certos 
assuntos). Veja este exemplo:

* No desktop uso Ubuntu. Para editar textos uso algum editor em modo gráfico (Gedit, Geany, Libre Office Text, ...). A 
interface com usuário é pensada para ser gráfica com mouse e teclado. Estou bem acostumado às teclas de acento, modo 
(CTRL, ALT, 
Win) e o clipboard dessa GUI. Decidi testar o telefone celular com ambiente de desktop. No caso, o telefone é um Galaxy 
S24FE e o ambiente é DeX. Escolhi um emulador de terminal (`Termux`) e o editor que vem pré-instalado (`nano`). É um 
outro hardware com outro ambiente e outra interface. Conectei os mesmos teclado e mouse mas como o sistema operacional 
que dá suporte é outro os atalhos são diferentes, os acentos são diferentes, ...*

Neste arquivo vou deixar anotados os atalhos de teclado que *funcionaram* no contexto atual (S24FE, Android 16, OneUI 8, 
teclado Samsung, modo DeX com fio)

Já fica um comentário: nas buscas por soluções, por exemplo, buscar "Como abrir vários arquivos no nano do termux do 
android" . O primeiro link indicado não me trouxe a informação que eu precisava, porque eu queria criar um novo arquivo. 
Em outras buscas o primeiro link apresenta informação sobre nano no Linux, ... é trabalhoso escrever um documento 
mostrando o que *funcionou* e a chance do que for mostrado *não funcionar* (em outro Android, em outro modelo de 
telefone, ...), acredito, é grande... 

`Nano` é um editor de texto para terminal modo texto. Seu projeto e documentação separam o arquivo (ié dados 
armazenados no SSD, HD, Cartão SD, ...) do buffer (área da RAM em que o programa `nano` em execução armazena e 
modifica o conteúdo do arquivo). Com essa distinção, nos é possível dizer que quando o programa `nano` lê um 
arquivo, o programa copia o conteúdo do arquivo do armazenamento para um buffer em RAM. Esse buffer é exibido 
na tela e seu conteúdo pode ser modificado pelo usuário. Quando o usuário tecla CTRL-S, o programa copia o 
conteúdo do buffer para o armazenamento. Em editores mais modernos, sequer é necessário *salvar o arquivo* (ié 
copiar o conteúdo do buffer para o armazenamento).  

## Iniciar nano a partir do Termux

No prompt do Termux, 

- Para abrir `nano` com um único buffer vazio, digitar `nano`;
- Para abrir um arquivo existente ou criar um arquivo dado seu nome, digitar `nano <nome_do_arquivo>` o nome do 
arquivo pode incluir um caminho para ele;
<!-- - Para abrir vários arquivos dados seus nomes, digitar `nano <nome_1> <nome_2> ...`; -->

## 

- Salvar o buffer no arquivo, digitar `CTRL-S`;
  - caso seja um buffer novo, sem associação com um arquivo, abre-se um prompt para digitar o nome, se o nome 
existir, sobrescreve sem pedir confirmação;

## Criar um novo buffer (este é um passo para criar um novo arquivo)

- digitar `CTRL-T`, `ALT-F`, `ENTER`
- se quiser salvar esse buffer, use `CTRL-S`

## Abrir um outro arquivo já existente

- Abrir um outro arquivo já existente, digitar `CTRL-R`
- após executar esse comando, há ao menos dois buffers de arquivos;

## Navegar entre buffers

- Mostrar próximo buffer, digitar `ALT->` (alt-seta para a direita);
- Mostrar buffer anterior, digitar `ALT-<` (alt-seta para a esquerda);

## 
 
## Marcar, Cortar e Colar texto dentro do `nano`

´nano´ usa uma marca para indicar o começo do texto a cortar. 

- ajustar a marca para a posição atual do cursor, digitar `ALT-A`;
- mover o cursor até o final do texto a cortar, usar setas do teclado;
- cortar o texto da marca até o cursor, digitar `CTRL-K`;
- se a intenção é copiar, então devolver o texto, digitar `CTRL-U`;
- mover o cursor, com as setas do teclado, até onde deseja inserir o texto;
- colar o texto, digitar `CTRL-U`;

O clipboard do `nano` é separado e não se comunica com o clipboard do Android

## Copiar texto de outro app para dentro do `nano`

Usar as ferramentas de marcar e copiar do Android e colar digitando `CTRL-SHIFT-V`


## Ligar/desligar inserção de quebra de linha

- Se a linha exceder a largura da janela, insere uma quebra de linha, digitar `ALT-L`

Isto é diferente do *line wrap* mais comum em que o texto recircula ao final da janela sem inserir uma quebra de linha.


