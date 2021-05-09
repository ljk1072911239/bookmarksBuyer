# from sportingbet.sportingBet import SportingBet
from apostas.betway.betWay import BetWay
from apostas.BETO import Beto
# from time import sleep

Beto('nba')
betway = BetWay()
betway.liga()
betway.achaParticipante()
while True:
    # try:
    # betway.oddsPartida()
    betway.odds()
    # betway.geracaoDeDados()
    # except Exception as e:
    #     print(e)
    #     sleep(5)
