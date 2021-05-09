from apostas.sportingbet.sportingBet import SportingBet
from time import sleep

sportingbet = SportingBet()
sportingbet.liga('nfl')
while True:
    try:
        sportingbet.achaParticipante(
            localParticipante=
            '#main-view > ms-fixture-list > div > div > div > ms-grid > ms-event-group:nth-child(3) > ms-six-pack-event:nth-child({contaPartida}) > a > div.grid-info-wrapper > ms-event-detail > ms-event-name > ms-inline-tooltip > div > div:nth-child({contaParticipante}) > div'
        )
        sportingbet.oddsPartida(
            localOdds=
            '#main-view > ms-fixture-list > div > div > div > ms-grid > ms-event-group:nth-child(3) > ms-six-pack-event:nth-child({contaPartida}) > a > div.grid-group-container > div > ms-option-group:nth-child(3) > ms-option:nth-child({contaParticipante}) > ms-event-pick > div',
            localPontos=
            '#main-view > ms-fixture-list > div > div > div > ms-grid > ms-event-group:nth-child(3) >  ms-six-pack-event:nth-child({contaPartida})  > a > div.grid-info-wrapper > ms-grid-scoreboard > ms-period-game-scoreboard > div > div:nth-child({situacao}) > div > div:nth-child(1)'
        )
        sportingbet.geracaoDeDados()
    except:
        sleep(5)
