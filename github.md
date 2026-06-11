##3aaaaaaaaaaaaaa
# Git e Github

## Com o celular

(desconfio que no desktop seja a mesma coisa...)

Quando um repositório é clonado do Github para uma pasta no termux, por exemplo executando 
`git clone https://github.com/FNakano/ProjetoBasico-CFA.git`, o diretório de controle e os arquivos (ié ./.git)
também são copiados. Isto facilita fazer `pull`, `push` e outras operações com o Github. É questão de completar 
a configuração.

No termux, completa-se a configuração ajustando o usuário e o e-mail com os comandos 
`git config --global user.name "seu nome de usuário do github"` e 
`git config --global user.email "seu email cadastrado no github"` . Essas configurações são globais no termux.
Se quiser que sejam locais ao diretório, remover `--global`

No Github há algumas alternativas e alguns passos em cada. Eu criei um token de acesso somente para atualização do 
conteúdo deste repositório. Para criar esse token entrei nas propriedades do meu usuário, selecionei Configurações
e selecionei Configurações de Desenvolvedor. Na página aberta selecionei Personal access tokens -> Fine-grained 
tokens, cliquei em gerar um novo token, selecionei o repositório, atribuí permissões de leitura e escrita para 
o conteúdo do repositório e cliquei em criar um novo token. O token gerado só é apresentado uma vez então copie e
cole em algum arquivo ou aplicativo.

O token pode ser usado na linha de comando 
do termux, em um `push`,  no lugar do password. Levou um tempo até construir a string que faz Gemini dar a resposta
certa: "how to create fine grained token to push to github using termux" . O token será necessário sempre que 
fizer `push` então o tenha à mão.

Quando atualizo um repositório, eu o envio ao github com esta sequencia de comandos:

1. `git add .`
2. `git commit -m "mensagem"`
3. `git push`


