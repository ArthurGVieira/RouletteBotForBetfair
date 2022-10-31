import telebot

# Definições do BOT do Telegram
CHAVE_API = ''
ID_GRUPO = []


class Bot:
    def __init__(self):
        self.bot = telebot.TeleBot(CHAVE_API)
        pass

    def mandar_msg_sinal(self, tipo, nome_roleta, numeros):
        mensagem1 = self.bot.send_message(ID_GRUPO,
                                     " \U000026A0\U000026A0 POSSÍVEL SINAL \U000026A0\U000026A0\n\n\n "
                                     "\U0001F4B0 Repetição na {TIPO} \U0001F4B0\n\n"
                                     " \U0001F3B0  {ROLETA}  \U0001F3B0\n\n\n"
                                     "   {NUMEROS}\n\n\n \U000026AB  \U000026AB  \U000026AB  \U000026AB  \U000026AB  \U000026AB  \U000026AB \n"
                                     " Abra as roletas e ESPERE \n A confirmação do sinal... "
                                     "\n \U000026AB  \U000026AB  \U000026AB  \U000026AB  \U000026AB  \U000026AB  \U000026AB \n".format(
                                         TIPO=tipo, ROLETA=nome_roleta,
                                         NUMEROS=',  '.join(map(str, numeros))))
        return mensagem1.id

    def mandar_msg_confirmado(self, tipo, nome_roleta, numeros):

        aposta1 = 0
        aposta2 = 0

        if tipo == 'Dúzia 1':
            aposta1 = 'Dúzia 2'
            aposta2 = 'Dúzia 3'
        if tipo == 'Dúzia 2':
            aposta1 = 'Dúzia 1'
            aposta2 = 'Dúzia 3'
        if tipo == 'Dúzia 3':
            aposta1 = 'Dúzia 1'
            aposta2 = 'Dúzia 2'
        if tipo == 'Linha 1':
            aposta1 = 'Linha 2'
            aposta2 = 'Linha 3'
        if tipo == 'Linha 2':
            aposta1 = 'Linha 1'
            aposta2 = 'Linha 3'
        if tipo == 'Linha 3':
            aposta1 = 'Linha 1'
            aposta2 = 'Linha 2'

        mensagem2 = self.bot.send_message(ID_GRUPO,
                                     " \U00002705\U00002705          SINAL           \U00002705\U00002705 \n\U00002705\U00002705   CONFIRMADO!   \U00002705\U00002705\n\n\n "
                                     "\U0001F4B0 Repetição da {TIPO} \U0001F4B0\n\n"
                                     " \U0001F3B0  {ROLETA}  \U0001F3B0\n\n\n"
                                     "   {NUMEROS}\n\n\n\U00002705  \U00002705  \U00002705  \U00002705  \U00002705  \U00002705  \U00002705  \U00002705 \n"
                                     "APOSTAR {APOSTA1} E {APOSTA2}! \n\U00002705  \U00002705  \U00002705  \U00002705  \U00002705  \U00002705  \U00002705  \U00002705 \n         COBRIR O ZERO!"
                                     "".format(TIPO=tipo, ROLETA=nome_roleta,
                                               NUMEROS=',  '.join(map(str, numeros)),
                                               APOSTA1=aposta1, APOSTA2=aposta2))
        return mensagem2.id

    def mandar_msg_green(self, tipo, nome_roleta, numeros):
        mensagem3 = self.bot.send_message(ID_GRUPO,
                                     "\U00002705\U00002705  RESULTADO  \U00002705\U00002705\n\n "
                                     "\U0001F4B0 Repetição na {TIPO} \U0001F4B0\n\n"
                                     " \U0001F3B0  {ROLETA}  \U0001F3B0\n\n"
                                     "   {NUMEROS}\n\n"
                                     "  \U00002705\U00002705   GREEN!!   \U00002705\U00002705"
                                     "".format(TIPO=tipo, ROLETA=nome_roleta,
                                               NUMEROS=',  '.join(map(str, numeros))))
        return mensagem3.id

    def mandar_msg_red(self, tipo, nome_roleta, numeros):
        mensagem4 = self.bot.send_message(ID_GRUPO,
                                     "\U0001F534\U0001F534  RESULTADO  \U0001F534\U0001F534\n\n "
                                     "\U0001F4B0 Repetição {TIPO} \U0001F4B0\n\n"
                                     " \U0001F3B0  {ROLETA}  \U0001F3B0\n\n"
                                     "   {NUMEROS}\n\n"
                                     "   \U0001F534\U0001F534    RED    \U0001F534\U0001F534"
                                     "".format(TIPO=tipo, ROLETA=nome_roleta,
                                               NUMEROS=',  '.join(map(str, numeros))))
        return mensagem4.id

    def apagar_msg(self, id_msg):
        self.bot.delete_message(ID_GRUPO, id_msg)
