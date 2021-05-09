# Antes de tudo, precisamos fazer algumas importações.
from selenium import webdriver
from time import sleep
import csv
import pandas as pd
from pathlib import Path
import datetime
from os import getlogin


# Definição da classe mãe sportsbetio.
class SportsBetIO(object):
    # Vamos definir algumas variáveis dela.
    # A variavel zapBot serve para sabermos se o usuário vai querer receber mensagens sobre o jogo.
    # zapBot = input('Deseja receber mensagens sobre o jogo? Digite 1 para Sim: ')
    zapBot = 2
    if zapBot == '1':
        # Se o usuário quiser receber mensagens, iniciaremos a classe Whatsapp como bot.
        from apostas.whatsapp.bot import WhatsappBot
        bot = WhatsappBot()
        bot.AbrirWPP()
    # Precisamos descobrir qual o usuario do computador, para fazermos os caminhos de arquivos serem válidos.
    usuario = getlogin()
    # Usaremos a variável timeEscolhido para que o usuário especifique qual o nome do time que quer acompanhar.
    timeEscolhido = input('Qual time você deseja acompanhar? ')
    # A variável opcoes diz respeito as preferências que teremos no nosso webdriver.
    opcoes = webdriver.ChromeOptions()
    # A preferência headless deixará o navegador invisível para nós, você pode desativá-la apenas comentando.
    # opcoes.add_argument("--headless")
    # Driver é a nossa variável em que usaremos como referência para manipular o chromedriver.
    driverSbetsio = webdriver.Chrome(f'/Users/{usuario}/Desktop/beto/chromedriver', options=opcoes)
    # Estabeleceremos a variável data para sabermos a data de execução do programa.
    # A lógica para cada componente da data, é a de primeiro utilizarmos a biblioteca datetime para recerbermos.
    # o dia por exemplo, então transformamos esse dado para uma string, e logo após preenchemos com zeros.
    # o que falta para ter 2 dígitos. Logo após, concatenamos todos os componentes.
    data = str(datetime.datetime.now().day).zfill(2) + str(datetime.datetime.now().month).zfill(2) + str(
        datetime.datetime.now().year)[2:]

    # Temos agora a função __init__, que é a de de inicialização da classe, onde sempre que a classe for
    # instanciada, ela será executada
    def __init__(self):
        # Estabeleceremos mais algumas variáveis, mas estas serão mais específicas para o Sbetsio.
        print('Iniciando SportsBet.IO.')
        url = 'https://sportsbet.io/pt/id/login'
        # Usando o método .get(), especificamos uma URL para o chromedriver ir.
        self.driverSbetsio.get(url)
        # A função sleep suspende o programa de acordo com os segundos especificados.
        sleep(2)
        # A forma while True faz com que até o break ser especificado, o programa é executado.
        while True:
            # O try-except funciona da seguinte forma:
            ## try: O programa tenta executar o que for especificado no bloco de código do try.
            ## except: Caso algum erro ocorra e o programa crashe, o programa parará o bloco de código do try
            ## e irá para o do except.
            # Importante: A forma do while True força o programa a sempre que crashar, voltar ao try, até que enfim
            # o bloco dele consiga ser executado.
            try:
                # # O método find_element_by_xpath(), permitirá que especifiquemos um caminho do xpath para que o
                # # chromedriver execute uma ação, nos casos abaixo, o clique, utilizando o método .click().
                self.driverSbetsio.find_element_by_xpath(
                    '//*[@id="root"]/div/div[1]/div/div[3]/form/fieldset/ul/li[1]/label/input').send_keys('')
                self.driverSbetsio.find_element_by_xpath(
                    '//*[@id="root"]/div/div[1]/div/div[3]/form/fieldset/ul/li[2]/label/input').send_keys('')
                self.driverSbetsio.find_element_by_xpath(
                    '//*[@id="root"]/div/div[1]/div/div[3]/form/fieldset/ul/li[4]/button').click()
                break
            except:
                pass

    # Temos agora a função liga(liga), onde especificamos qual liga queremos trabalhar.
    def liga(self, liga):
        self.liga = liga
        # Para explicar a variável urls, vamos explicar cada parte por vez:
        ## Função open: Abrimos em modo de leitura o arquivo de texto ligasBetWay.txt, que
        ## contém o nosso dicionário das ligas,e depois o lemos efetivamente usando o método .read().
        ## Função eval: Avalia uma cadeia de caracteres e transforma no tipo de dado mais adequado, neste caso,
        ## uma string.
        ## Função dict: Recebe o especificado e transforma em um dicionário.
        urls = dict(eval(open(f'C:/Users/{self.usuario}/Desktop/beto/sportsbetio/ligasSportsBet.txt', 'r').read()))
        # Na variável urlsLiga, buscaremos no dicionário urls a chave da liga especificada, e assim obteremos o
        # valor correspondente, que no caso, será a url da liga no SportingBet.
        urlLiga = urls[liga.lower()]
        print(f'Indo para a página da {liga.upper()}.')
        while True:
            try:
                sleep(3)
                self.driverSbetsio.get(urlLiga)
                sleep(5)
                self.driverSbetsio.find_element_by_link_text(self.timeEscolhido).click()
                print(f'Jogo do {self.timeEscolhido} encontrado.')
                break
            except:
                pass

    # Na função achaParticipante(localParticipante), acharemos o jogo do time especificado pelo usuario.
    def achaParticipante(self):
        self.visitante = self.driverSbetsio.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div').text
        self.casa = self.driverSbetsio.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[3]/div').text

    def oddsPartida(self):
        self.oddVisitante = self.driverSbetsio.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/ul/li[1]/button/div/div/span[2]/span[1]').text
        self.oddCasa = self.driverSbetsio.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/ul/li[2]/button/div/div/span[2]/span[1]').text
        try:
            self.pontosVisitante = self.driverSbetsio.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div[1]').text
            self.pontosCasa = self.driverSbetsio.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]').text
        except:
            self.pontosVisitante = None
            self.pontosCasa = None

    # Criaremos agora variáveis para controle de prints na tela.
    # A variável ultimoPlacar servirá para armazenamento do último placar da partida.
    ultimoPlacar = ''
    # A variável ultimaDescricao servirá para armazenamento da última descrição da partida.
    ultimaDescricao = ''
    # A variável primeiraVez nos informará se é a primeira vez que o programa está sendo executado.
    primeiraVez = True
    contador = 0

    def geracaoDeDados(self):
        # Criaremos agora a lista da partida, que armazenará o time visitante e o de casa, com os espaços
        # substituídos por underlines.
        partida = [self.visitante.split()[-1], self.casa.split()[-1]]
        # A variável pontosTimes representa uma lista que armazena 2 strings, a de Away_PTS e a Home_PTS.
        pontosTimes = ['Away_PTs', 'Home_PTs']
        # hora é a variável que representará a coluna do tempo no nosso CSV.
        hora = ['Hour', 'Minute', 'Second']
        # Por padrão, adotaremos o nome do CSV como o último nome do time visitante, "@", o último nome do time de
        # casa, isso com cada nome capitalizado, seguido de um "_", e por último a data. Não podemos esquecer de
        # especificar o tipo de arquivo.
        self.partidaCSV = f"{self.visitante.split()[-1]}@{self.casa.split()[-1]}_" + self.data + '.csv'
        # As variáveis de caminhoPartidasCSV e caminhoTimesCSV, se referem aos locais das pastas de armazenamento de
        # dados para a liga e times especificados, vale lembrar que temos a base de dados de jogos da liga, e também
        # a de cada time.
        self.caminhoPartidasCSV = f'C:/Users/{self.usuario}/Desktop/beto/sbetsio/{self.liga.lower()}/database{self.liga.upper()}/matches/'
        self.caminhoTimesCSV = f'C:/Users/{self.usuario}/Desktop/beto/sbetsio/{self.liga.lower()}/database{self.liga.upper()}/teams/'
        # Especificaremos agora os nomes dos CSVs de cada time.
        self.casaCSV = self.casa.split()[-1] + '.csv'
        self.visitanteCSV = self.visitante.split()[-1] + '.csv'
        # Concatenaremos agora os nomes dos times ao caminho correto.
        self.caminhoCasaCSV = self.caminhoTimesCSV + self.casaCSV
        self.caminhoVisitanteCSV = self.caminhoTimesCSV + self.visitanteCSV
        # A variável informacoesPartida servirá como cabeçalho para o nosso CSV da partida.
        informacoesPartida = partida + pontosTimes + hora
        # As variáveis informacoesCasa e informacoesVisitante, servirá para cabeçalho dos CSVs de cada time.
        informacoesCasa = [f'{self.casa.split()[-1]}', 'Opponent', f'{self.casa.split()[-1]}_PTs', 'Opponent_PTs',
                           'Opponent_name', f'{self.casa.split()[-1]}_Away/Home'] + hora
        informacoesVisitante = [f'{self.visitante.split()[-1]}', 'Opponent', f'{self.visitante.split()[-1]}_PTs', 'Opponent_PTs',
                                'Opponent_name', f'{self.visitante.split()[-1]}_Away/Home'] + hora
        # Utilizando a função Path, informaremos ao programa, atravé da variável partidaCSV, qual o caminho de
        # armazenagem do csv.
        partidaCSV = Path((self.caminhoPartidasCSV + self.partidaCSV))
        # Faremos a checagem de se o arquivo de CSV da partida já existe, para que a cada execução do programa,
        # seja sobrescrito um arquivo já existente.
        if partidaCSV.is_file() == False:
            # Primeiro temos que abrir o arquivo no modo de escrita (w), e chamaremos este processo de arquivo.
            with open(self.caminhoPartidasCSV + self.partidaCSV, 'w', newline='', ) as arquivo:
                # O método .writer(arquivo, delimitador), especificará qual delimitador queremos, no caso, o ";",
                # também em qual arquivo faremos isso.
                escritor = csv.writer(arquivo, delimiter=';')
                # O método .writerow() nos permite escrever uma linha no arquivo criado, que neste caso, será o
                # o cabeçalho do CSV da partida.
                escritor.writerow(informacoesPartida)
        # Faremos novamente processo anterior, porém, agora com os CSVs do time visitante e o de casa também.
        casaCSV = Path(self.caminhoTimesCSV + self.casaCSV)
        if casaCSV.is_file() == False:
            with open(self.caminhoCasaCSV, 'w', newline='', ) as arquivo:
                escritor = csv.writer(arquivo, delimiter=';')
                escritor.writerow(informacoesCasa)
        visitanteCSV = Path(self.caminhoTimesCSV + self.visitanteCSV)
        if visitanteCSV.is_file() == False:
            with open(self.caminhoVisitanteCSV, 'w', newline='', ) as arquivo:
                escritor = csv.writer(arquivo, delimiter=';')
                escritor.writerow(informacoesVisitante)
        # A variável times é uma string informa os times participantes.
        self.times = f'\n--- {self.visitante.split()[-1]} @ {self.casa.split()[-1]} ---\n'
        # pontuacao corresponde a variável de pontuação dos times
        self.pontuacao = f'--- {self.pontosVisitante} x {self.pontosCasa} ---\n'
        # A variável odds corresponde a variável de odds da partida.
        self.odds = f'- SportsBets.io {self.oddVisitante} x {self.oddCasa} SportsBets.io -\n'
        # placar armazena os dados de times, pontuacao e odds.
        self.placar = self.times + self.pontuacao + self.odds
        # Para evitarmos que toda hora o placar seja mostrado na tela, colocaremos uma condicional para que
        # ele só seja exibido se for diferente do último exibido.
        if self.placar != self.ultimoPlacar:
            print(self.placar)
            # Se o placar for diferente do último, daremos à variável ultimoPlacar o valor do novo placar.
            self.ultimoPlacar = self.placar
            # Colocaremos agora uma condicional para que, caso o usuário deseje receber mensagens no whatsapp,
            # as mensagens sejam enviadas.
            if self.zapBot == 1:
                # Caso seja a primeira vez que alguma mensagem esteja sendo enviada, os times serão informados.
                if self.primeiraVez:
                    self.bot.EnviarMensagens(self.times)
                    # Agora que os times foram informados, não há mais necessidade de informálos, apenas os
                    # placares e odds já servem.
                    self.primeiraVez = False
                # Agora serão enviadas, por whatsapp, as pontuações e odds
                self.bot.EnviarMensagens(self.pontuacao + self.odds)
            # A string oddsPartida, armazena, separados por ";", as odds do time visitante e de casa.
            # O método .join() permite que os elementos de uma lista sejam unidos por uma string especificada,
            # formando uma nova string.
            self.oddsDaPartida = ';'.join([str(self.oddVisitante), str(self.oddCasa)])
            # Agora precisamos fazer o mesmo para cada time
            # Lembrando que sempre o time do CSV aparece na segunda coluna dos times, por isso é necessário
            # inverter ordens.
            self.oddsVisitante = ';'.join([str(self.oddCasa), str(self.oddVisitante)])
            self.oddsCasa = ';'.join([str(self.oddVisitante), str(self.oddCasa)])
            # O mesmo processo será repetido, porém agora com os pontos de cada time.
            self.pontosPartida = ';'.join([str(self.pontosVisitante), str(self.pontosCasa)])
            self.pontosVisitante = ';'.join([str(self.pontosCasa), str(self.pontosVisitante)])
            self.pontosCasa = ';'.join([str(self.pontosVisitante), str(self.pontosCasa)])
            # Vamos agora criar uma string que informará a hora da captação das informações.
            self.tempo = ';'.join([str(datetime.datetime.now().hour), str(datetime.datetime.now().minute),
                                   str(datetime.datetime.now().second) + '\n'])
            # Precisamos agora colocar as situações de cada time, se é em casa ou não, que estão jogando
            self.situacaoCasa = 'Home'
            self.situacaoVisitante = 'Away'
            # Criaremos agora as variáveis que seão utilizadas para inserção de linhas nos CSVs, sempre
            # unidos por ";", para que depois possam ser separados.
            self.adicionaInformacoesPartida = ';'.join([self.oddsDaPartida, self.pontosPartida, self.tempo])
            self.adicionaInformacoesVistante = ';'.join(
                [self.oddsVisitante, self.pontosVisitante, self.visitante.split()[-1], self.situacaoCasa, self.tempo])
            self.adicionaInformacoesCasa = ';'.join(
                [self.oddsCasa, self.pontosCasa, self.casa.split()[-1], self.situacaoVisitante, self.tempo])
            # Abriremos agora cada CSV criado anteriormente, mas de modo de inserção, usando a anexação ('a'),
            # e depois vamos inserir as informações adequadas para cada um.
            with open(self.caminhoPartidasCSV + self.partidaCSV, 'a') as inserirPartidas:
                inserirPartidas.write(self.adicionaInformacoesPartida)
            with open(self.caminhoCasaCSV, 'a') as inserirCasa:
                inserirCasa.write(self.adicionaInformacoesVistante)
            with open(self.caminhoVisitanteCSV, 'a') as inserirVisitante:
                inserirVisitante.write(self.adicionaInformacoesCasa)
        # Para termos análises da partida, utilizaremos a biblioteca Pandas para criarmos um dataframe com as
        # informações registradas nos CSVs criados.
        # Precisamos especificar o local do arquivo e o delimitador, que no nosso caso é o ';'.
        analisePartida = pd.read_csv(self.caminhoPartidasCSV + self.partidaCSV, delimiter=';')
        # A variavel descricaoPartida, nos retorna uma descrição de dados das colunas de cada time, srredondados
        # para 2 casas decimais
        self.descricaoPartida = str(
            analisePartida[[self.visitante.split()[-1], self.casa.split()[-1]]].describe().round(
                2))
        # Faremos agora uma condicional para qua a cada 1000 execuções da função, o relatório da partida seja
        # gerado e possivelmente enviado ao usuário via whatsapp.
        # Lembrando que só será enviado um novo relatório caso ele seja diferente do último, na mesma lógica
        # dos placares.
        if self.contador % 1000 == 0:
            if self.descricaoPartida != self.ultimaDescricao:
                print(self.descricaoPartida)
                if self.zapBot == 1:
                    self.bot.EnviarMensagens(self.descricaoPartida)
                self.ultimaDescricao = self.descricaoPartida
        self.contador+=1
