from apostas.betway.betWay import BetWay
from time import sleep
from apostas.BETO import Beto
from apostas.sportingbet.sportingBet import SportingBet

beto = Beto()
betway = BetWay()
sportingbet = SportingBet()
betway.liga('nfl')
sportingbet.liga('nfl')
betway.achaParticipante()
while True:
    try:
        betway.oddsPartida()
        sportingbet.oddsPartida()
        betway.geracaoDeDados()
        sportingbet.geracaoDeDados()
        beto.mostraPlacar()
    except Exception as e:
        print(e)
        sleep(5)
