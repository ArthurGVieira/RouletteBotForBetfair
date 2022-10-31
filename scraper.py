from bs4 import BeautifulSoup
import re

quantidade_numeros = 6
atributo_nomes = {"class": "lobby-table__name-container"}
atributo_numeros = {"class": "roulette-history-item__value-textsiwxWvFlm3ohr_UMS23f"}
lista_ref = ['Dúzia 1', 'Dúzia 2', 'Dúzia 3', 'Linha 1', 'Linha 2', 'Linha 3']
lista_conf = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35], [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
                [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]]


class Scraper:

    def __init__(self, elementos):
        self.elementos = elementos
        self.lista_nomes = []
        self.lista_numeros = []

    def soup(self):
        lista_numeros_temp = []
        lista_true_false = []
        for i in range(len(self.elementos)):
            soup = BeautifulSoup(self.elementos[i], 'html.parser')
            nomes = soup.find_all("div", attrs=atributo_nomes)
            numeros = soup.find_all("div", attrs=atributo_numeros)

            # Append dos nomes
            nom = str(nomes)
            apenas_nomes = re.search(r'.*.*\>(.*)\<', nom)
            self.lista_nomes.append(apenas_nomes.group(1))

            # Append dos numeros
            q = quantidade_numeros - 1
            for k in range(quantidade_numeros):
                num = str(numeros[q])
                apenas_numeros = re.search(r'.*.*\>(.*)\<', num)
                lista_numeros_temp.append(apenas_numeros.group(1))
                q = q - 1

            # Análise para verificar se a sequência está se formando
            for k in range(6):
                for p in range(quantidade_numeros):
                    try:
                        if int(lista_numeros_temp[p]) in lista_conf[k]:
                            lista_true_false.append(True)
                        else:
                            lista_true_false.append(False)
                    except:
                        lista_true_false.append(False)
                if all(lista_true_false):
                    return True, i, k, self.lista_nomes[i], lista_numeros_temp, lista_ref[k]
                lista_true_false = []

            # Resetando as variáveis
            self.lista_numeros.append(tuple(lista_numeros_temp))
            lista_numeros_temp = []
            lista_true_false = []

    @classmethod
    def analise(cls, elementos, i, k, nome_roleta, numeros):
        try:
            soup = BeautifulSoup(elementos[i], 'html.parser')
        except IndexError:
            return 3
        nomes = soup.find_all("div", attrs=atributo_nomes)
        numeros2 = soup.find_all("div", attrs=atributo_numeros)

        nom = str(nomes)
        apenas_nomes = re.search(r'.*.*\>(.*)\<', nom)

        lista_numeros_temp = []
        q = quantidade_numeros - 1
        for j in range(quantidade_numeros):
            num = str(numeros2[q])
            apenas_numeros = re.search(r'.*.*\>(.*)\<', num)
            lista_numeros_temp.append(apenas_numeros.group(1))
            q = q - 1

        if apenas_nomes.group(1) == nome_roleta:
            if lista_numeros_temp == numeros:
                return 2
            else:
                if lista_numeros_temp[len(lista_numeros_temp) - 1] == '':
                    return 3
                if int(lista_numeros_temp[len(lista_numeros_temp) - 1]) in lista_conf[k]:
                    return 0, lista_numeros_temp
                else:
                    return 1, lista_numeros_temp
        else:
            return 3
