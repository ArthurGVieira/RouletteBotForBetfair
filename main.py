from driver import Driver
from scraper import Scraper
from bot import Bot
import time

driver = Driver()
bot = Bot()
t = 0

while True:
    elementos = driver.pegar_elementos()
    df = Scraper(elementos).soup()
    time.sleep(1)
    t = t + 1
    if t > 300:
        driver.reset_driver()
        t = 0
    # A repetição dos números aconteceu e a função .soup() retornou uma lista: 0 - True, 1 - valor de i,
    # 2 - valor de k, 3 - nome da roleta, 4 - números, 5 - tipo da repetição
    if df is not None:
        lista_numeros = df[4]
        num = df[4]
        mensagem = bot.mandar_msg_sinal(df[5], df[3], num)
        i = 0
        while True:
            time.sleep(1)
            elementos = driver.pegar_elementos()
            analise = Scraper.analise(elementos, df[1], df[2], df[3], num)
            if analise == 3:
                bot.apagar_msg(mensagem)
                break
            # Buscando novos números
            if analise == 2:
                continue
            # Confirma o sinal e função analise() retorna uma lista: 0 - 0, 1 - lista de números atual
            if analise[0] == 0:
                if i == 0:
                    num = analise[1]
                    lista_numeros.append(num[len(num) - 1])
                    bot.apagar_msg(mensagem)
                    mensagem = bot.mandar_msg_confirmado(df[5], df[3], lista_numeros)
                    i = i + 1
                    continue
                # Realiza o gale
                if i == 1:
                    num = analise[1]
                    lista_numeros.append(num[len(num) - 1])
                    i = i + 1
                    continue
                # Deu red
                else:
                    num = analise[1]
                    lista_numeros.append(num[len(num) - 1])
                    bot.apagar_msg(mensagem)
                    mensagem = bot.mandar_msg_red(df[5], df[3], lista_numeros)
                    time.sleep(120)
                    break
            if analise[0] == 1:
                # Sinal falhou
                if i < 1:
                    bot.apagar_msg(mensagem)
                    break
                # Deu green
                else:
                    num = analise[1]
                    lista_numeros.append(num[len(num) - 1])
                    bot.apagar_msg(mensagem)
                    mensagem = bot.mandar_msg_green(df[5], df[3], lista_numeros)
                    break
