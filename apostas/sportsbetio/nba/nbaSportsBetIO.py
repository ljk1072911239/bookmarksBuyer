from apostas.sportsbetio.sportsbetio import SportsBetIO
from time import sleep

sportsbetio = SportsBetIO()
sportsbetio.liga('nba')
sportsbetio.achaParticipante()
while True:
    try:
        sportsbetio.oddsPartida()
        sportsbetio.geracaoDeDados()
    except:
        sleep(5)

