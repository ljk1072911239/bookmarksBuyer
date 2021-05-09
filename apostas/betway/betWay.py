import datetime
from apostas.BETO import Beto

class BetWay(Beto):

    driverBetWay = Beto.driverBetWay
    data = str(datetime.datetime.now().day).zfill(2) + str(datetime.datetime.now().month).zfill(2) + str(datetime.datetime.now().year)[2:]

    def __init__(self):
        print('BetWay - Iniciando.')
        url = 'https://sports.betway.com/pt/sports'
        self.driverBetWay.get(url)

    def login(self):
        print('BetWay - Fazendo login.')
        Beto.MestreBetoBot.enviaMensagem('BetWay - Fazendo login.')
        while True:
            try:
                self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[5]/div/div/form/div[1]/div[2]/input').send_keys('')
                self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[5]/div/div/form/div[1]/div[3]/input').send_keys('')
                self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[5]/div/div/form/div[2]').click()
                break
            except:
                self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[5]/div/div/form/div[1]/div[2]/input').clear()
                self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[5]/div/div/form/div[1]/div[3]/input').clear()
                pass
        while True:
            try:
                # montanteBW = float(self.driverBetWay.find_element_by_class_name('accountBalance').text.replace(',','.').replace('R$',''))
                montanteBW = 10.00
                break
            except:
                pass
        Beto.montante = montanteBW
        self.primeiraVezAposta = True

    def liga(self):
        print(f'BetWay - Indo para a página da {Beto.liga.upper()}.')
        self.MestreBetoBot.enviaMensagem(f'BetWay - Indo para a página da {Beto.liga.upper()}.')
        urlLiga = Beto.dictLiga['urls']['BetWay']
        self.driverBetWay.get(urlLiga)
        while True:
            try:
                jogo = self.driverBetWay.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(self.time))[0]
                jogo.click()
                print(f'BetWay - Jogo do {self.time} encontrado!')
                break
            except:
                pass

    def achaParticipante(self):
        while True:
            try:
                try:
                    self.visitante = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split('@')[0][0:-1]
                except:
                    self.visitante = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split('-')[0][0:-1]
                Beto.nomeVisitante = self.visitante
                # print(self.visitante)
                try:
                    self.casa = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split('@')[1][1::]
                except:
                    self.casa = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split('-')[1][1::]
                Beto.nomeCasa = self.casa
                # print(self.casa)
                print('BetWay - Nomes dos participantes encontrados!')
                Beto.MestreBetoBot.enviaMensagem('BetWay - Nomes dos participantes encontrados!')
                break
            except:
                pass
        while True:
            try:
                self.lupa = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[1]')
                self.lupa.click()
                break
            except:
                pass

    def odds(self, mercado):
        try:
            self.barraPesquisa = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[2]/div/input')
            while True:
                try:
                    self.barraPesquisa.clear()
                    self.barraPesquisa.send_keys(mercado)
                    try:
                        oddVisitante = float(self.driverBetWay.find_element_by_xpath(self.caminhoVisitanteBetWay).text.replace(',', '.'))
                        oddCasa = float(self.driverBetWay.find_element_by_xpath(Beto.caminhoCasaBetWay).text.replace(',', '.'))
                    except:
                        oddVisitante = 0
                        oddCasa = 0
                    break
                except:
                    try:
                        self.lupa.click()
                    except:
                        pass
                    pass
            Beto.dicionarioOddsVisitante.update({'BetWay': oddVisitante})
            Beto.dicionarioOddsCasa.update({'BetWay': oddCasa})
        except:
            oddVisitante = 0
            oddCasa = 0
            Beto.dicionarioOddsVisitante.update({'BetWay': oddVisitante})
            Beto.dicionarioOddsCasa.update({'BetWay': oddCasa})

    def aposta(self, stake, caminhoOdd, odd, sniper, nomeTime):
        oddNovaBW = float(str(self.driverBetWay.find_element_by_xpath(caminhoOdd).text).replace(',', '.'))
        if sniper:
            condicaoAposta = oddNovaBW >= odd
        else:
            condicaoAposta = oddNovaBW == odd
        if condicaoAposta:
            self.driverBetWay.execute_script("window.scrollTo(0, 300)")
            botaoOdd = self.driverBetWay.find_element_by_xpath(caminhoOdd)
            botaoOdd.click()
            while True:
                try:
                    self.driverBetWay.find_element_by_css_selector('body > div > div > div.topBar.node > div > div.topBarThirdRow.node > div > div.sidebar.collection.vertical > div.sidebarContent.node > div > div.contentAreaWrapper > div.contentArea.scrollableArea.vertical > div > div:nth-child(1) > div > div.betSlipSelectionGroupsContainer > div > div.betSlipSelectionGroupingCollection.node > div > div > div > div.collapsibleContentWidgetContainer > div > div > div > div.stakeInputContainer > div > div.stakeInputContainer > input').send_keys(str(stake).replace('.', ','))
                    break
                except:
                    pass
            botaoApostaBW = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[2]/div/div/div/button')
            oddNovaBW = float(str(self.driverBetWay.find_element_by_xpath(caminhoOdd).text).replace(',', '.'))
            if sniper:
                condicaoAposta = oddNovaBW >= odd
            else:
                condicaoAposta = oddNovaBW == odd
            if condicaoAposta:
                try:
                    botaoApostaBW.click()
                    if not self.testeAposta:
                        while True:
                            try:
                                xpathSucesso = '/html/body/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[8]/div/div[1]/div[2]'
                                textoSucesso = 'Aposta(s) feita(s) com sucesso'
                                if self.driverBetWay.find_element_by_xpath(xpathSucesso).text == textoSucesso:
                                    print(f'Aposta em {Beto.time} (BetWay) feita!')
                                    Beto.MestreBetoBot.enviaMensagem(f'Aposta em {Beto.time} (BetWay) feita!')
                                    return True
                                else:
                                    self.fechaAposta()
                                    return False
                            except:
                                pass
                    else:
                        print(f'Aposta em {Beto.time} (BetWay) feita!')
                        Beto.MestreBetoBot.enviaMensagem(f'Aposta em {Beto.time} (BetWay) feita!')
                        return True
                except:
                    self.fechaAposta()
                    return False
            else:
                return False
        return False

    def fechaAposta(self):
        if not self.testeAposta:
            try:
                botaoEliminarTudo = self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/div/span')
                botaoEliminarTudo.click()
            except:
                self.driverBetWay.execute_script("arguments[0].click();", Beto.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div/div[3]/div/div[3]/div[2]/div'))
        else:
            self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[8]/div/div[2]/div/div/div/div[1]/div[2]/div').click()
            self.driverBetWay.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div/div[3]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[3]/div/div[4]/div/div/div/div[1]/div[1]/div[2]/div/span').click()




































    def jogo(self, urlJogo):
        self.driverBetWay.get(urlJogo)

    def achaParticipanteJogo(self):
        while True:
            try:
                try:
                    self.visitante = self.driverBetWay.find_element_by_xpath(
                        '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split(
                        '@')[0][0:-1]
                except:
                    self.visitante = self.driverBetWay.find_element_by_xpath(
                        '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split(
                        '-')[0][0:-1]
                Beto.nomeVisitante = self.visitante
                try:
                    self.casa = self.driverBetWay.find_element_by_xpath(
                        '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split(
                        '@')[1][1::]
                except:
                    self.casa = self.driverBetWay.find_element_by_xpath(
                        '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[1]/div/div/h1').text.split(
                        '-')[1][1::]
                Beto.nomeCasa = self.casa
                print('BW - Nomes dos participantes encontrados!')
                break
            except:
                pass
        while True:
            try:
                lupa = self.driverBetWay.find_element_by_xpath(
                    '/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[1]/div[1]/div/div[1]/div/div[1]')
                self.driverBetWay.execute_script("arguments[0].scrollIntoView();", lupa)
                lupa.click()
                break
            except:
                pass
