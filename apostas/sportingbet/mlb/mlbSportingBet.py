from apostas.sportingbet.sportingBet import SportingBet
from time import sleep

sportingbet = SportingBet()
sportingbet.liga('mlb')                                                
while True:
    try:
        sportingbet.achaParticipante(
            localParticipante=
            '#main-view > ms-fixture-list > div > div > div > ms-grid > ms-event-group > ms-six-pack-event > a > div.grid-info-wrapper > ms-event-detail > ms-event-name > ms-inline-tooltip > div > div:nth-child({contaParticipante}) > div'
        )
        sportingbet.oddsPartida(
            localOdds=
            '#main-view > ms-fixture-list > div > div > div > ms-grid > ms-event-group > ms-six-pack-event > a > div.grid-group-container > div > ms-option-group:nth-child(3) > ms-option:nth-child({contaParticipante}) > ms-event-pick > div > div > ms-font-resizer',
            localPontos=
            '#main-view > ms-fixture-list > div > div > div > ms-grid > ms-event-group > ms-six-pack-event > a > div.grid-info-wrapper > ms-grid-scoreboard > ms-baseball-scoreboard > div:nth-child(2) > div:nth-child({situacao}) > div > div:nth-child(1)'
        )
        sportingbet.geracaoDeDados()
    except:
        sleep(5)
