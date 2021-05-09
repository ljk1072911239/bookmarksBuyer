from time import sleep
from apostas.BETO import Beto

class SportingBet(Beto):

    def __init__(self):
        print('SportingBet - Iniciando.')
        url = 'https://sports.sportingbet.com/pt-br/sports'
        self.driverSportingBet.get(url)
        while not self.headless:
            try:
                self.driverSportingBet.find_element_by_xpath('//*[@id="messages-with-overlay"]/div/vn-content-message/div/span').click()
                break
            except:
                pass

    def login(self):
        print('SportingBet - Fazendo login.')
        self.MestreBetoBot.enviaMensagem('SportingBet - Fazendo login.')
        while True:
            try:
                self.driverSportingBet.find_element_by_xpath('/html/body/vn-app/vn-dynamic-layout-single-slot[1]/vn-responsive-header/header/nav/vn-header-section[2]/vn-h-button[1]/vn-menu-item/a').click()
                self.driverSportingBet.find_element_by_xpath('//*[@id="username"]/input').send_keys('')
                self.driverSportingBet.find_element_by_xpath('//*[@id="password"]/input').send_keys('')
                self.driverSportingBet.find_element_by_xpath('//*[@id="login"]/form/fieldset/section/div[2]/button').click()
                break
            except:
                pass
        while True:
            try:
                montanteSportingBet = 10.00
                break
            except:
                pass
        if montanteSportingBet < Beto.montante:
            Beto.montante = montanteSportingBet
        self.primeiraAposta = True
        self.urlJogo = ''

    def liga(self):
        print(f'SportingBet - Indo para a página da {Beto.liga}.')
        try:
            Beto.MestreBetoBot.enviaMensagem(f'SportingBet - Indo para a página da {Beto.liga.upper()}.')
        except:
            pass
        urlLiga = Beto.dictLiga['urls']['SportingBet']
        self.driverSportingBet.get(urlLiga)
        while True:
            try:
                try:
                    jogo = self.driverSportingBet.find_element_by_xpath("//div[contains(text(), ' {0}')]".format(self.time))
                    self.driverSportingBet.execute_script("arguments[0].scrollIntoView();", jogo)
                    jogo.click()
                    sleep(2)
                    self.driverSportingBet.find_element_by_xpath('//*[@id="main-view"]/ng-component/ms-header/ms-dropdown-tab-bar/ul/li[1]/a/span').click()
                    print(f'SportingBet - Jogo do {self.time} encontrado!')
                    try:
                        Beto.MestreBetoBot.enviaMensagem(f'SportingBet - Jogo do {self.time} encontrado!')
                    except:
                        pass
                    break
                except:
                    for item in range(len(self.driverSportingBet.find_elements_by_xpath("//*[contains(text(), ' {0}')]".format(self.time)))):
                        try:
                            self.driverSportingBet.find_elements_by_xpath("//*[contains(text(), ' {0}')]".format(self.time))[item].click()
                            self.urlJogo = self.driverSportingBet.current_url
                            break
                        except:
                            pass
                    pass
            except:
                self.driverSportingBet.execute_script("window.scrollBy(0, 250)")
                pass

    def jogo(self, urlJogo):
        self.driverSportingBet.get(urlJogo)

    def odds(self, mercado):
        xpathVisitante = Beto.dictLiga['mercados'][mercado]['Visitante']['SportingBet']
        xpathCasa = Beto.dictLiga['mercados'][mercado]['Casa']['SportingBet']
        self.driverSportingBet.execute_script("arguments[0].scrollIntoView();", self.driverSportingBet.find_element_by_xpath(xpathVisitante))
        try:
            oddVisitante = float(self.driverSportingBet.find_element_by_xpath(xpathVisitante).text)
            oddCasa = float(self.driverSportingBet.find_element_by_xpath(xpathCasa).text)
        except:
            oddVisitante = 0
            oddCasa = 0
        Beto.dicionarioOddsVisitante.update({'SportingBet': oddVisitante})
        Beto.dicionarioOddsCasa.update({'SportingBet': oddCasa})

    def aposta(self, stake, caminhoOdd, odd, sniper, nomeTime):
        print('Fazendo aposta SportingBet!')
        self.driverSportingBet.execute_script("arguments[0].scrollIntoView();", Beto.driverSportingBet.find_element_by_xpath(caminhoOdd))
        oddNova = float(self.driverSportingBet.find_element_by_xpath(caminhoOdd).text)
        if sniper:
            condicaoAposta = oddNova >= odd
        else:
            condicaoAposta = oddNova == odd
        if condicaoAposta:
            self.driverSportingBet.find_element_by_xpath(caminhoOdd).click()
            xpathStakeSportingBet = '//*[@id="betslip"]/div[2]/div/ms-betslip-stakebar/div/div/span/ms-stake/div/ms-stake-input/div/input'
            while True:
                try:
                    cupomApostas = self.driverSportingBet.find_element_by_xpath(xpathStakeSportingBet)
                    self.driverSportingBet.execute_script("arguments[0].scrollIntoView();", cupomApostas)
                    break
                except:
                    pass
            while True:
                try:
                    self.driverSportingBet.find_element_by_xpath(xpathStakeSportingBet).click()
                    self.driverSportingBet.find_element_by_xpath(xpathStakeSportingBet).send_keys(str(stake))
                    break
                except:
                    pass
            botaoApostaSportingBet = self.driverSportingBet.find_element_by_xpath('//*[@id="betslip"]/div[2]/div/div/ms-betslip-action-button/div/button')
            oddNova = float(self.driverSportingBet.find_element_by_xpath(caminhoOdd).text)
            if sniper:
                condicaoAposta = oddNova >= odd
            else:
                condicaoAposta = oddNova == odd
            if condicaoAposta or self.testeAposta:
                try:
                    if not self.testeAposta:
                        botaoApostaSportingBet.click()
                        while True:
                            try:
                                xpathSucesso = '//*[@id="betslip"]/ms-betslip-result-container/div/ms-betslip-result-successful/div/div[1]/span[1]'
                                textoSucesso = '1 aposta(s) de um total de 1 foram efetuadas.'
                                if self.driverSportingBet.find_element_by_xpath(xpathSucesso).text == textoSucesso:
                                    print(f'Aposta em {Beto.time} (SportingBet) feita!')
                                    try:
                                        Beto.MestreBetoBot.enviaMensagem(f'Aposta em {nomeTime} (SportingBet) feita!')
                                    except:
                                        pass
                                    return True
                                else:
                                    self.fechaAposta()
                                    print(f'Aposta em {Beto.time} (SportingBet) falhada!')
                                    try:
                                        Beto.MestreBetoBot.enviaMensagem(f'Aposta em {nomeTime} (SportingBet) falhada!')
                                    except:
                                        pass
                                    return False
                            except:
                                pass
                    else:
                        print(f'Aposta em {Beto.time} (SportingBet) feita!')
                        self.driverSportingBet.find_element_by_xpath(caminhoOdd).click()
                        try:
                            Beto.MestreBetoBot.enviaMensagem(f'Aposta em {nomeTime} (SportingBet) feita!')
                        except:
                            pass
                        return True
                except Exception as e:
                    print(e)
                    print('BUCETA 2')
                    print(f'Aposta em {Beto.time} (SportingBet) falhada!')
                    try:
                        Beto.MestreBetoBot.enviaMensagem(f'Aposta em {nomeTime} (SportingBet) falhada!')
                    except:
                        pass
                    self.fechaAposta()
                    return False
            return False
        return False


    def verificaRecibo(self):
        while True:
            try:
                xpathSucesso = '//*[@id="betslip"]/ms-betslip-result-container/div/ms-betslip-result-successful/div/div[1]/span[1]'
                textoSucesso = '1 aposta(s) de um total de 1 foram efetuadas.'
                if self.driverSportingBet.find_element_by_xpath(xpathSucesso) == textoSucesso:
                    break
                else:
                    self.fechaAposta()
                    break
            except:
                pass

    def fechaAposta(self):
        if not self.testeAposta:
            try:
                botaoFecharAposta = self.driverSportingBet.find_element_by_xpath('//*[@id="betslip"]/div[1]/div[1]/ms-betslip-picks/div[1]/div/ms-betslip-v1-pick/div[2]/div/div/div[1]/div[2]/div/span')
                botaoFecharAposta.click()
            except:
                Beto.driverSportingBet.find_element_by_xpath('//*[@id="main-content"]/ms-main/ms-widget-column/ms-widget-slot/ms-bet-column/ms-tab-bar/ul/li[2]').click()
                Beto.driverSportingBet.find_element_by_xpath('//*[@id="main-content"]/ms-main/ms-widget-column/ms-widget-slot/ms-bet-column/ms-tab-bar/ul/li[1]').click()
        # else:
        #     sleep(2)
        #     self.driverSportingBet.switch_to_frame(self.driverSportingBet.find_element_by_xpath('/html/body/div[2]/div[1]'))
        #     print('trocou')
        #     # self.driverSportingBet.execute_script("arguments[0].scrollIntoView();", self.driverSportingBet.find_element_by_xpath('//*[@id="mat-dialog-0"]/lh-login-dialog/lh-login/lh-header-bar/vn-header-bar/div/div'))
        #     self.driverSportingBet.execute_script("arguments[0].click();", self.driverSportingBet.find_element_by_xpath('//*[@id="mat-dialog-1"]/lh-login-dialog/lh-login/lh-header-bar/vn-header-bar/div/div/div[3]/span'))
