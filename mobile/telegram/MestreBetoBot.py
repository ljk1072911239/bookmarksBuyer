from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
import telegram
from apostas.BETO import Beto

class MestreBetoBot(Beto):
    OPERACAO, TIME, ODD, STAKE = range(4)
    operacaoEscolhida = ''
    stake = 0
    odd = 0
    dicionarioNBA = {'Blazers': 'Portland Trail Blazers',
                     'Clippers': 'Los Angeles Clippers',
                     'Grizzlies': 'Memphis Grizzlies',
                     'Jazz': 'Utah Jazz',
                     'Kings': 'Sacramento Kings',
                     'Lakers': 'Los Angeles Lakers',
                     'Mavs': 'Dallas Mavericks',
                     'Nuggets': 'Denver Nuggets',
                     'Pelicans': 'New Orleans Pelicans',
                     'Rockets': 'Houston Rockets',
                     'Suns': 'Phoenix Suns',
                     'Spurs': 'San Antonio Spurs',
                     'Wolves': 'Minnesota Timberwolves',
                     'OKC': 'Oklahoma City Thunder',
                     'Warriors': 'Golden State Warriors',
                     '76ers': 'Philadelphia 76ers',
                     'Bulls': 'Chicago Bulls',
                     'Bucks': 'Milwaukee Bucks',
                     'Cavs': 'Cleveland Cavaliers',
                     'Celtics': 'Boston Celtics',
                     'Hawks': 'Atlanta Hawks',
                     'Heat': 'Miami Heat',
                     'Hornets': 'Charlotte Hornets',
                     'Knicks': 'New York Knicks',
                     'Magic': 'Orlando Magic',
                     'Nets': 'Brooklyn Nets',
                     'Pacers': 'Indiana Pacers',
                     'Pistons': 'Detroit Pistons',
                     'Raptors': 'Toronto Raptors',
                     'Wizards': 'Washington Wizards',
                     }
    snipado = False
    bot = telegram.Bot(token='1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE')

    def __init__(self) -> None:
        # self.beto = Beto('NBA')
        if not self.testeAposta:
            # self.BetWay.login()
            self.SportingBet.login()
            # self.beto.BetWarrior.login()
        print('Iniciando o Telegram.')
        updater = Updater("")
        self.updater = updater
        dispatcher = updater.dispatcher
        self.dispatcher = dispatcher
        stringTime = '🕒 Blazers|🥊 76ers|🦞 Clippers|🐮 Bulls|🐻 Grizzlies| 🇬🇷 Bucks|🕷 Jazz|💘 Cavs|👑 Kings|👴🏿 Celtics|🤴🏿 Lakers|🥶 Hawks|👱🏻‍♂️ Mavs|🔥 Heat|🃏 Nuggets|🏀 Hornets|🌱 Pelicans|🌹 Knicks|🚀 Rockets|🎩 Magic|🌞 Suns|1️⃣3️⃣ Nets|🧽 Spurs|🅿️ Pacers|🐺 Wolves|🔝 Pistons|⛈️ OKC|🦎 Raptors|💦 Warriors|🧙‍♀️ Wizards'

        def pararExecucao(update: Update, context: CallbackContext):
            update.message.reply_text('Operação cancelada!', reply_markup=ReplyKeyboardRemove())
            context.job_queue.stop()
            return ConversationHandler.END

        conversa = ConversationHandler(
            entry_points=[CommandHandler('start', self.time, Filters.user(user_id=1375793777))],
            states={
                self.TIME: [MessageHandler(Filters.regex('^(' + stringTime + ')$'), self.operacao)],
                self.OPERACAO: [MessageHandler(Filters.regex('^(🤑 Win Win)$'), self.conexaoBeto), MessageHandler(Filters.regex('^(🎯 Sniper)$'), self.oddSniper)],
                self.ODD: [MessageHandler(Filters.user(user_id=1375793777), self.stakeSniper)],
                self.STAKE: [MessageHandler(Filters.user(user_id=1375793777), self.conexaoBeto)]
            },
            fallbacks=[CommandHandler('stop', pararExecucao)],
        )
        dispatcher.add_handler(conversa)

    def execucaoBot(self):
        self.updater.start_polling()
        self.updater.idle()

    def oddSniper(self, update: Update, context: CallbackContext) -> int:
        self.operacaoEscolhida = ''.join(update.message.text.split()[1:])
        print('Operação Escolhida:', self.operacaoEscolhida)
        update.message.reply_text('Escolha a Odd:', reply_markup=ReplyKeyboardRemove())
        return self.ODD

    def stakeSniper(self, update: Update, context: CallbackContext) -> int:
        self.odd = float(update.message.text.replace(',', '.'))
        print('Odd:', self.odd)
        update.message.reply_text('Escolha a Stake:')
        return self.STAKE

    def operacao(self, update: Update, context: CallbackContext) -> int:
        Beto.time = self.dicionarioNBA[update.message.text.split()[1]]
        print('Time escolhido:', Beto.time)
        reply_keyboard = [['🤑 Win Win'], ['🎯 Sniper']]
        update.message.reply_text('Qual operação deseja fazer?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),)
        return self.OPERACAO

    def time(self, update: Update, context: CallbackContext) -> int:
        reply_keyboard = [
                            ['🕒 Blazers', '🥊 76ers'],
                            ['🦞 Clippers', '🐮 Bulls'],
                            ['🐻 Grizzlies', ' 🇬🇷 Bucks'],
                            ['🕷 Jazz', '💘 Cavs'],
                            ['👑 Kings', '👴🏿 Celtics'],
                            ['🤴🏿 Lakers', '🥶 Hawks'],
                            ['👱🏻\u200d♂️ Mavs', '🔥 Heat'],
                            ['🃏 Nuggets', '🏀 Hornets'],
                            ['🌱 Pelicans', '🌹 Knicks'],
                            ['🚀 Rockets', '🎩 Magic'],
                            ['🌞 Suns', '1️⃣3️⃣ Nets'],
                            ['🧽 Spurs', '🅿️ Pacers'],
                            ['⛈️ OKC', '🔝 Pistons'],
                            ['💦 Warriors', '🦎 Raptors'],
                            ['🐺 Wolves', '🧙\u200d♀️ Wizards']
                        ]
        update.message.reply_text('Escolha o time:', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),)
        return self.TIME


    def conexaoBeto(self, update: Update, context: CallbackContext):
        if self.operacaoEscolhida != 'Sniper':
            self.operacaoEscolhida = ''.join(update.message.text.split()[1:])
            print('Operação Escolhida:', self.operacaoEscolhida)
        else:
            try:
                self.stake = float(update.message.text.replace(',', '.'))
                print('Stake:', self.stake)
            except:
                import os
                import sys
                import psutil
                import logging
                try:
                    p = psutil.Process(os.getpid())
                    for handler in p.get_open_files() + p.connections():
                        os.close(handler.fd)
                except Exception as e:
                    logging.error(e)
                python = sys.executable
                os.execl(python, python, *sys.argv)
        update.message.reply_text('Iniciando a operação.', reply_markup=ReplyKeyboardRemove())
        Beto.SportingBet.liga()
        # Beto.BetWay.liga()
        # Beto.BetWarrior.liga()
        # Beto.BetWay.achaParticipante()
        if self.operacaoEscolhida == 'WinWin':
            update.message.reply_text('Fazendo o WinWin.', reply_markup=ReplyKeyboardRemove())
            context.job_queue.run_repeating(self.execucaoWinWin, interval=0)
        elif self.operacaoEscolhida == 'Sniper':
            update.message.reply_text('Fazendo o Sniping.')
            if Beto.time == Beto.nomeCasa:
                self.lugar = 'Casa'
            else:
                self.lugar = 'Visitante'
            context.job_queue.run_repeating(self.execucaoSniper, interval=0)
        # return ConversationHandler.END

    def execucaoWinWin(self, context):
        for mercado in Beto.mercados:
            Beto.SportingBet.odds(mercado=mercado)
            # Beto.BetWay.odds(mercado=mercado)
            # Beto.BetWarrior.odds(mercado=mercado)
            self.odds(mercado=mercado)
            Beto.operacaoWinWin(self=self, mercado=mercado)

    def execucaoSniper(self, context):
        lugar = self.lugar
        self.SportingBet.odds('Money Line')
        # self.BetWay.odds('Money Line')
        # self.BetWarrior.odds('Money Line')
        self.odds(mercado='Money Line')
        oddLugar = eval(f'self.maiorOdd{lugar}')
        condicaoSniper = oddLugar >= self.odd
        if condicaoSniper:
            casaDeAposta = eval(f'self.lugar{lugar}')
            try:
                caminhoOddSniper = Beto.dictLiga["mercados"]['Money Line'][lugar][casaDeAposta]
            except:
                caminhoOddSniper = eval(f'self.beto.caminho{lugar}{casaDeAposta}')
            snipado = eval(f'self.{casaDeAposta}.aposta(stake=self.stake, caminhoOdd=caminhoOddSniper, odd=self.odd, sniper=True, nomeTime=self.time)')
            eval(f'self.{casaDeAposta}.fechaAposta()')
            print(f'Antiga aposta de {self.time} ({casaDeAposta}) fechada!')
            context.job_queue.stop()

    def enviaMensagem(self, texto):
        self.bot.send_message(chat_id=0, text=texto)

# MestreBetoBot()
