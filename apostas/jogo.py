from sportingbet.sportingBet import SportingBet
from betway.betWay import BetWay
from BETO import Beto

beto = Beto()
betway = BetWay()
sportingbet = SportingBet()
betway.jogo('https://sports.betway.com/pt/sports/evt/6992887')
sportingbet.jogo('https://sports.sportingbet.com/pt-br/sports/eventos/club-deportivo-hispano-americano-argentino-de-ju-10987173')
betway.achaParticipanteJogo()
while True:
    # try:
    sportingbet.oddsPartida(visitante='//*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/ms-regular-option-group/div/ms-option[1]/ms-event-pick/div/div[2]',
                            casa='//*[@id="main-view"]/ng-component/div/ms-option-group-list/div[1]/ms-option-panel[1]/ms-regular-option-group/div/ms-option[2]/ms-event-pick/div/div[2]')
    # except:
    #     pass
        # print('Erro no SportingBet!')
    # try:
    betway.oddsPartida(visitante='/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/div[2]/div/div[4]/div/div[1]/div[1]/div[2]/div/div[3]/div  ',
                       casa='/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/div[2]/div/div[4]/div/div[1]/div[2]/div[2]/div/div[3]/div',
                       moneyLine='/html/body/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div/div[5]/div/div[2]/div[1]/div[2]/div[1]/span',
                       padrao=False)
    # except:
    #     try:
    #         betway.driverBetWay.find_element_by_xpath("//span[contains(text(), '{Money}')]").click()
    #     except:
    #         pass
        # print('Erro no BetWay!')
    # try:
    beto.mostraPlacar()
    beto.verificaGap()
    # except:
        # pass
    # except:
    #     sleep(5)
