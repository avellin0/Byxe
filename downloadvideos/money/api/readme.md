esse readme é sobre o arquivo "byxe_api.py" , aqui em baixo vou explicar a estutura do readme
[] = oque estiver aqui dentro é exmplo
{} = citações minhas
() = explicações

# /Download 

## Primeiro você deve criar um array que tem palavras chaves de comando do 'yt-dlp' 
(Serve para evitar problemas como "parsing" ou "injeção" de comandos maliciosos) 

## Depois você cria uma variavel para capturar o stdout (return) e stder (possivel erro)
(essa variavel vai receber o stdout)
[ex: process = {vou explicar em baixo oque vem aqui}]

## Usando o subprocess.Popen tendo como argumentos : o array de comando , e fazendo uma tipagem do retorno do comando , enviando esse retorno para o process, ou seja, ao invés do retorno ir para o terminal ele é "mantido" dentro do código para ser manipulado pela variavel "process".
[ex: process = subprocess.Popen(comando, stdout=subprocess.PIPE , stder=subprocess.PIPE)]
{vou deixar uma explição sobre "Popen" e "PIPE" no final `:)`}

## Depois você cria uma função que tem um loop infinito que tem uma variavel "data" recebendo o "stdout" do comando anterior que está na variavel "process" e executa a função "read" do stdout , que precisa de um argumento dizendo a quantidade de bytes que serão lidos por cada "volta" do loop , quando não haver mais bytes para ser lidos o loop é cancelado e é retornado  o "data"

```
[ex: 
     while True:
        data = process.stdout.read(1064)
     if not data:
        break
     yield data
]
```

# /send

----------------------------------------- ----------------------------------------

# Oque significa esse "Popen" e "PIPE" ?


## Popen()

O Popen é uma classe do módulo subprocess em Python. Ela é usada para criar novos processos, conectar-se a seus pipes de entrada/saída/erro e obter o código de retorno quando o processo termina. Em outras palavras, Popen permite que você execute um comando do sistema operacional a partir do seu código Python e interaja com o processo criado.

```
import subprocess

process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = process.communicate()

print(stdout.decode())
```

Nesse exemplo, o Popen executa o comando ls -l (que lista arquivos em um diretório no Unix) e captura a saída e os erros.

Principais argumentos de Popen:

* args: O comando que você deseja executar. Pode ser passado como uma string ou como uma lista de strings.

* stdout: Define o destino da saída padrão do processo (normalmente exibida no terminal). Se for definido como subprocess.PIPE, a saída será capturada para ser usada no seu código.

* stderr: Define o destino da saída de erro padrão do processo. Se definido como subprocess.PIPE, a saída de erro será capturada para ser usada no seu código.

## PIPE

PIPE é uma constante do módulo subprocess que representa um pipeline (canal de comunicação) para a entrada (stdin), saída (stdout) e erro (stderr) de um processo.

Quando você define stdout=subprocess.PIPE ou stderr=subprocess.PIPE, você está dizendo ao Python para redirecionar essas saídas para o seu código, em vez de deixá-las aparecer diretamente no terminal. Isso permite que você leia, processe e manipule a saída do comando dentro do seu código Python.