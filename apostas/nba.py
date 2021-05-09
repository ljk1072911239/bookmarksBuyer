from BETO import Beto

beto = Beto('NBA')
# beto.betway.login()
# beto.sportingbet.login()
# beto.betWarrior.login()
beto.SportingBet.liga()
# beto.BetWay.liga()
# beto.BetWarrior.liga()
# beto.BetWay.achaParticipante()
while True:
    for mercado in Beto.mercados:
        beto.SportingBet.odds(mercado=mercado)
        # beto.BetWay.odds(mercado=mercado)
        # beto.BetWarrior.odds(mercado=mercado)
        beto.odds(mercado=mercado)
        beto.operacaoWinWin(mercado=mercado)
