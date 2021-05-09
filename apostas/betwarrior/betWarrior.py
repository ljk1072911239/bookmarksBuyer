from apostas.BETO import Beto

class BetWarrior(Beto):

    def __init__(self):
        print('BetWarrior - Iniciando.')
        url = 'https://betwarrior.bet/pt-br/sports'
        self.driverBetWarrior.get(url)

    def login(self):
        print('BetWarrior - Fazendo login.')
        Beto.MestreBetoBot.enviaMensagem('BetWarrior - Fazendo login.')
        while True:
            try:
                botaoLogin = self.driverBetWarrior.find_element_by_xpath('//*[@id="user-trigger"]/div[1]/div/div')
                botaoLogin.click()
                break
            except:
                pass
        while True:
            try:
                entradaEmail = self.driverBetWarrior.find_element_by_xpath('//*[@id="email-input"]/label/div[2]/input')
                entradaSenha = self.driverBetWarrior.find_element_by_xpath('//*[@id="password-input"]/label/div[2]/input')
                botaoEnviar = self.driverBetWarrior.find_element_by_xpath('//*[@id="login-action"]')
                entradaEmail.send_keys('leoneriribeiro@gmail.com')
                entradaSenha.send_keys('senhissima14')
                botaoEnviar.click()
                break
            except:
                pass

    def liga(self):
        while True:
            try:
                botaoPesquisa = self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div/div[2]/header/div[2]/div/div/button[2]')
                botaoPesquisa.click()
                break
            except:
                pass
        while True:
            try:
                barraPesquisa = self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[2]/div[1]/div/div/input')
                barraPesquisa.send_keys(self.time)
                break
            except:
                pass
        while True:
            try:
                jogo = self.driverBetWarrior.find_element_by_xpath(f'//*[@id="standard:level_type=list_view,level_id=/basketball/all/all/{"_".join(self.time.lower().split())}"]/div[2]/div/div[1]/div[2]/a')
                print(f'BetWarrior - Jogo do {self.time} encontrado!')
                Beto.MestreBetoBot.enviaMensagem(f'BetWarrior - Jogo do {self.time} encontrado!')
                jogo.click()
                break
            except:
                pass

    def odds(self, mercado):
        xpathVisitante = Beto.dictLiga['mercados'][mercado]['Visitante']['BetWarrior']
        xpathCasa = Beto.dictLiga['mercados'][mercado]['Casa']['BetWarrior']
        try:
            oddVisitante = float(self.driverBetWarrior.find_element_by_xpath(xpathVisitante).text.replace(',', '.'))
            oddCasa = float(self.driverBetWarrior.find_element_by_xpath(xpathCasa).text.replace(',', '.'))
        except:
            oddVisitante = 0
            oddCasa = 0
        Beto.dicionarioOddsVisitante.update({'BetWarrior': oddVisitante})
        Beto.dicionarioOddsCasa.update({'BetWarrior': oddCasa})

    def aposta(self, stake, caminhoOdd, odd, sniper, nomeTime):
        oddNova = float(self.driverBetWarrior.find_element_by_xpath(caminhoOdd).text.replace(',','.'))
        if sniper or self.testeSniper:
            condicaoAposta = oddNova >= odd
        else:
            condicaoAposta = oddNova == odd
        if condicaoAposta:
            self.driverBetWarrior.execute_script("arguments[0].click();", self.driverBetWarrior.find_element_by_xpath(caminhoOdd))
            xpathStake = '//*[@id="__next"]/div/div[2]/div[4]/div/div[2]/div/div/div[2]/div/input'
            while True:
                try:
                    cupomApostas = self.driverBetWarrior.find_element_by_xpath(xpathStake)
                    self.driverBetWarrior.execute_script("arguments[0].scrollIntoView();", cupomApostas)
                    self.driverBetWarrior.find_element_by_xpath(xpathStake).send_keys(str(stake))
                    break
                except:
                    pass
            botaoAposta = self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[4]/div/div[5]/button')
            try:
                oddNova = float(self.driverBetWarrior.find_element_by_xpath(caminhoOdd).text.replace(',', '.'))
            except:
                oddNova = float(self.driverBetWarrior.find_element_by_xpath(caminhoOdd[:-5]).text.replace(',', '.'))
            if sniper or self.testeSniper:
                condicaoAposta = oddNova >= odd
            else:
                condicaoAposta = oddNova == odd
            if condicaoAposta:
                try:
                    botaoAposta.click()
                    print(f'Aposta em {Beto.time} (BetWarrior) feita!')
                    Beto.MestreBetoBot.enviaMensagem(f'Aposta em {Beto.time} (BetWarrior) feita!')
                    return True
                except:
                    self.fechaAposta()
                    return False
            return False
        return False

    def fechaAposta(self):
        if not self.testeAposta:
            try:
                botaoLimpar = self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[3]/div/div[1]/span[2]/button')
                botaoLimpar.click()
            except:
                self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[4]/div/div[1]/span[2]/button').click()
                self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div[1]/div[2]/div[4]/div/button').click()
        else:
            self.driverBetWarrior.find_element_by_xpath('//*[@id="js-modal-content"]/div[1]/button/span').click()
            self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[4]/div/div[1]/span[2]/button').click()
            self.driverBetWarrior.find_element_by_xpath('//*[@id="__next"]/div/div[2]/div[4]/div/button').click()
