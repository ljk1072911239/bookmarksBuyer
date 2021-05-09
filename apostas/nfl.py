from sportingbet.sportingBet import SportingBet
from betway.betWay import BetWay
from BETO import Beto
from time import sleep

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
