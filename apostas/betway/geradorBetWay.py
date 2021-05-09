# Importações
from os import getlogin, path, makedirs
login = getlogin()

# Primeiro, vamos definir o texto que nosso gerador tem que colar nos arquivos.
# Este texto deve conter as coisas básicas do programa para ser executado, com os métodos de classes necessários,
# além de informar o que deve ser alterado.
gerador = '''from betway.betWay import BetWay
from time import sleep

betway = BetWay()
betway.liga('{liga}')
betway.achaParticipante()
while True:
    try:
        betway.oddsPartida()
        betway.geracaoDeDados()
    except:
        sleep(5)
\n'''

# Vamos agora abrir o dicionário de ligas que já temos. Vale lembrar que este dicionário contém nas chaves o nome da
# liga, e nos valores as urls dela.
# Vamos salvar esta abertura na variável carregaDicionario.
carregaDicionario = open(f'C:/Users/{login}/Desktop/beto/betway/ligasBetWay.txt', 'r')
# Se o dicionário não existir, criaremos um novo
try:
    # Na variável dicionario, leremos o conteúdo do arquivo ligasBetWay.txt, e transformaremos em um dicionário.
    dicionario = dict(eval(carregaDicionario.read()))
except:
    # Caso o arquivo não exista, um novo será criado com "{}" escritos, para reconhcer como um dicionário vazio.
    open(f'C:/Users/{login}/Desktop/beto/betway/ligasBetWay.txt', 'w').write('{}')
    dicionario = dict(eval(carregaDicionario.read()))
# Vamos agora fechar o arquivo, para evitar possíveis conflitos
carregaDicionario.close()
# Agora criaremos um looping que funcionará até o usuário digitar 0.
while True:
    liga = input('Insira a liga, ou 0 para parar: ').lower()
    if liga == '0':
        break
    url = input('Insira a URL dela, ou 0 para parar:  ')
    if url == '0':
        break
    # Formaremos um dicionário novo que contenha a liga e o valor dela, no caso, a url.
    chave = {liga: url}
    # Agora adicionaremos no nosso dicionário extraído do arquivo de texto uma nova chave, que contém a liga e url
    # informadas pelo usuário.
    dicionario.update(chave)
    # Precisamos agora sobrescrever o antigo arquivo, incorporando a nova chave.
    # Vamos abrir o arquivo novamente, em modo de escrita ('w').
    salvaDicionario = open(f'C:/Users/{login}/Desktop/beto/betway/ligasBetWay.txt', 'w')
    # Escreveremos p dicionário atualizado.
    salvaDicionario.write(str(dicionario))
    # Fecharemos o arquivo.
    salvaDicionario.close()
    # Vamos agora criar pastas para a liga especificada, além de gerar um modelo de programação.
    # Primeiro vamos especificar um possível caminho da liga.
    caminhoLiga = f'C:/Users/{login}/Desktop/beto/betway/{liga}'
    # Vamos agora criar a variável modelo, que condiz com o modelo de texto antes criado com a formatação correta.
    modelo = gerador.format(liga=liga)
    # Se os diretórios básicos da liga não existem, serão criadas.
    if not path.exists(caminhoLiga):
        makedirs(caminhoLiga)
        makedirs(caminhoLiga+'/database'+liga.upper())
        makedirs(caminhoLiga+'/database'+liga.upper() + '/matches')
        makedirs(caminhoLiga+'/database'+liga.upper() + '/teams')
        # Vamos agora criar o arquivo python para colocarmos o modelo.
        with open(caminhoLiga+f'/{liga.lower()}BetWay.py', 'w') as arquivo:
            arquivo.write(modelo)
    print(f'Pasta da liga {liga.upper()} criada e pronta para usar!')