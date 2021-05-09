from BETO import Beto


def oddEStakeSniper(stakeFeita, oddFeita, comissao):
    minimaPorcentagem = comissao / 100
    minimoLucro = stakeFeita * oddFeita * minimaPorcentagem
    receitaFeita = round(stakeFeita * oddFeita, 2)
    stakeRestante = round(receitaFeita - minimoLucro - stakeFeita, 2)
    oddRestante = round(receitaFeita / stakeRestante, 2)
    return stakeRestante, oddRestante


stake, odd = oddEStakeSniper(stakeFeita=100, oddFeita=2.5, comissao=1)
mercado = 'Money Line'

beto = Beto('NBA')
# beto.betway.login()
# beto.sportingbet.login()
# beto.betWarrior.login()
# beto.SportingBet.liga()
# beto.BetWay.liga()
beto.BetWarrior.liga()
# beto.BetWay.achaParticipante()
while True:
    beto.operacaoSniper(lugar='Casa', mercado=mercado, stakeSniper=stake, oddSniper=odd)
    break
