from selenium import webdriver
from os import getlogin
import platform

class Beto(object):
    time = 'Philadelphia 76ers'
    nomeCasa = ''
    nomeVisitante = ''
    maiorOddCasa = 0
    maiorOddVisitante = 0
    lugarCasa = ''
    lugarVisitante = ''
    ptsCasa = None
    ptsVisitante = None
    ultimoGap = ''
    montante = 10
    liga = ''
    mercados = []
    caminhosSB = {}
    caminhoVisitanteBetWay = '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div/div[3]/div'
    caminhoCasaBetWay = '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[3]/div/div[1]/div[2]/div/div[4]/div/div[1]/div[2]/div[2]/div/div[3]/div'
    dicionarioOddsVisitante = {}
    dicionarioOddsCasa = {}
    dictLiga = {}
    dictPrints = {}
    testeWinWin = False
    testeSniper = False
    testeAposta = True
    sistemaOperacional = platform.system()

    # Configurações webdrivers
    usuario = getlogin()
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--window-size=1920,1080")
    headless = False
    if headless:
        opcoes.add_argument("--headless")

    # Driver SportingBet
    if sistemaOperacional == 'Windows':
        caminhoDriver = f'/Users/{usuario}/Desktop/beto/chromedriver'
    else:
        caminhoDriver = '/usr/bin/chromedriver'

    driverSportingBet = webdriver.Chrome(caminhoDriver,  options=opcoes)

    # # Driver BetWay
    # driverBetWay = webdriver.Chrome(caminhoDriver,  options=opcoes)

    # Driver BetWarrior
    # driverBetWarrior = webdriver.Chrome(caminhoDriver,  options=opcoes)

    def __init__(self, liga):
        print('Beto - Iniciando.')
        # Casas de aposta
        from apostas.sportingbet.sportingBet import SportingBet
        Beto.SportingBet = SportingBet()
        # from apostas.betway.betWay import BetWay
        # Beto.BetWay = BetWay()
        # from apostas.betwarrior.betWarrior import BetWarrior
        # Beto.BetWarrior = BetWarrior()

        # Outros atributos
        Beto.liga = liga
        if self.sistemaOperacional == 'Windows':
            caminhoInfos = f'C:/Users/{Beto.usuario}/Desktop/beto/apostas/infos.txt'
        else:
            caminhoInfos = f'/home/{Beto.usuario}/Área de Trabalho/beto/apostas/infos.txt'
        dicionarioGeral = dict(eval(open(caminhoInfos, encoding="utf8", mode = 'r').read()))
        Beto.dictLiga = dicionarioGeral[Beto.liga]
        Beto.mercados = list(Beto.dictLiga['mercados'].keys())
        for mercado in Beto.mercados:
            Beto.dictPrints.update({mercado: ''})
        Beto.caminhosVisitanteSB = []
        Beto.caminhosCasaSB = []

        # Bot Telegram
        from mobile.telegram.MestreBetoBot import MestreBetoBot
        Beto.MestreBetoBot = MestreBetoBot()
        MestreBetoBot.execucaoBot(self=Beto.MestreBetoBot)

    def odds(self, mercado):
        self.lugarVisitante = max(Beto.dicionarioOddsVisitante, key=Beto.dicionarioOddsVisitante.get)
        self.maiorOddVisitante = Beto.dicionarioOddsVisitante[self.lugarVisitante]
        self.lugarCasa = max(Beto.dicionarioOddsCasa, key=Beto.dicionarioOddsCasa.get)
        self.maiorOddCasa = Beto.dicionarioOddsCasa[self.lugarCasa]
        novoPlacar = f'\n{Beto.nomeVisitante} X {Beto.nomeCasa}\n' + mercado + f'\n{self.lugarVisitante} - {self.maiorOddVisitante} X {self.maiorOddCasa} - {self.lugarCasa}'
        if novoPlacar != Beto.dictPrints[mercado] and (self.maiorOddVisitante != 0 or self.maiorOddCasa != 0):
            print(novoPlacar)
            self.MestreBetoBot.enviaMensagem(novoPlacar)
            Beto.dictPrints[mercado] = novoPlacar

    def operacaoWinWin(self, mercado):
        custoProbabilidadeVisitante = float(str(1 / self.maiorOddVisitante)[0:4])
        custoProbabilidadeCasa = float(str(1 / self.maiorOddCasa)[0:4])
        verificaGap = (custoProbabilidadeVisitante + custoProbabilidadeCasa) < 1
        if verificaGap or self.testeWinWin:
        # if True:
            if self.maiorOddVisitante > self.maiorOddCasa:
                contaStakeVisitante = (self.montante * self.maiorOddCasa) / (self.maiorOddVisitante + self.maiorOddCasa)
                stakeVisitante = float(str(contaStakeVisitante)[:len(str(int(contaStakeVisitante)))+3])
                contaStakeCasa = self.montante - stakeVisitante
                stakeCasa = float(str(contaStakeCasa)[:len(str(int(contaStakeCasa)))+3])
            else:
                contaStakeCasa = (self.montante * self.maiorOddVisitante) / (self.maiorOddCasa + self.maiorOddVisitante)
                stakeCasa = float(str(contaStakeCasa)[:len(str(int(contaStakeCasa)))+3])
                contaStakeVisitante = self.montante - stakeCasa
                stakeVisitante = float(str(contaStakeVisitante)[:len(str(int(contaStakeVisitante)))+3])
            receitaVisitante = float(str(round(stakeVisitante * self.maiorOddVisitante, 2)))
            lucroVisitante = float(str(round(receitaVisitante - self.montante, 2)))
            lucroPercentualVisitante = str(round(lucroVisitante / self.montante * 100, 2))
            receitaCasa = float(str(round(stakeCasa * self.maiorOddCasa, 2)))
            lucroCasa = float(str(round(receitaCasa - self.montante, 2)))
            lucroPercentualCasa = str(round(lucroCasa / self.montante * 100, 2))
            if (lucroVisitante > 0 and lucroCasa > 0) or self.testeWinWin:
                mostraGap = '\nGap Encontrado!' + \
                f'\nReceita {Beto.nomeVisitante}: {stakeVisitante} * {self.maiorOddVisitante} = R${receitaVisitante}' + \
                f'\nLucro {Beto.nomeVisitante}: {receitaVisitante} - {self.montante} = R${lucroVisitante} ({lucroPercentualVisitante} %)' + \
                f'\nReceita {Beto.nomeCasa}: {stakeCasa} * {self.maiorOddCasa} = R${receitaCasa}' + \
                f'\nLucro {Beto.nomeCasa}: {receitaCasa} - {self.montante} = R${lucroCasa} ({lucroPercentualCasa} %)' + \
                f'\nCapital investido: R${self.montante}\n'
                print(mostraGap)
                Beto.MestreBetoBot.enviaMensagem(mostraGap)
                try:
                    caminhoOdd = Beto.dictLiga["mercados"][mercado]["Casa"][self.lugarCasa]
                except:
                    caminhoOdd = eval(f'Beto.caminhoCasa{self.lugarCasa}')
                fezApostaCasa = eval(f'self.{self.lugarCasa}.aposta(stake=stakeCasa, caminhoOdd=caminhoOdd, odd=self.maiorOddCasa, sniper=False, nomeTime=Beto.nomeCasa)')
                if fezApostaCasa:
                    eval(f'self.{self.lugarCasa}.fechaAposta()')
                    print(f'Antiga aposta de {self.nomeCasa} ({self.lugarCasa}) fechada!')
                    Beto.MestreBetoBot.enviaMensagem(f'Antiga aposta de {self.nomeCasa} ({self.lugarCasa}) fechada!')
                    self.operacaoSniper(lugar='Visitante', mercado=mercado, stakeSniper=stakeVisitante, oddSniper=self.maiorOddVisitante)



    def operacaoSniper(self, lugar, mercado, stakeSniper, oddSniper):
        nomeTime = eval(f'Beto.nome{lugar}')
        print(f'Snipando Odd {nomeTime} de {oddSniper}.')
        Beto.MestreBetoBot.enviaMensagem(f'Snipando Odd {nomeTime} de {oddSniper}.')
        snipado = False
        while not snipado:
            self.SportingBet.odds(mercado)
            # self.BetWay.odds(mercado)
            # self.BetWarrior.odds(mercado)
            self.odds(mercado)
            oddLugar = eval(f'self.maiorOdd{lugar}')
            condicaoSniper = oddLugar >= oddSniper
            if condicaoSniper:
                casaDeAposta = eval(f'self.lugar{lugar}')
                try:
                    caminhoOddSniper = Beto.dictLiga["mercados"][mercado][lugar][casaDeAposta]
                except:
                    caminhoOddSniper = eval(f'Beto.caminho{lugar}{casaDeAposta}')
                snipado = eval(f'self.{casaDeAposta}.aposta(stake=stakeSniper, caminhoOdd=caminhoOddSniper, odd=oddSniper, sniper=True, nomeTime=Beto.nome{lugar})')
                eval(f'self.{casaDeAposta}.fechaAposta()')
                print(f'Antiga aposta de {nomeTime} ({casaDeAposta}) fechada!')

# Beto('NBA')