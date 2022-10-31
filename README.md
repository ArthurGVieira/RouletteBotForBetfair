# Roulette Bot For Betfair
A bot for web scraping and sending telegram group signals

## 1. Configure
> Go to driver.py, change login and password to any valid betfair account

> Go to bot.py, change CHAVE_API to your telegram bot API KEY and change ID_GRUPO to your telegram group ID where do you want the signals to be sent

## 2. How it works
> It realizes a web scraping for get the html from betfair roulettes

> Checks if there was a repetition of 6 numbers in the same dozen or line in any of the roulette wheels

> Then sends a signal to the telegram group notifying it

> If one more number of the same dozen or line comes out, the bot sends a confirmation for betting on the other 2 dozens or other 2 lines

## 3. Additional configuration
> If you want to change the number of numbers of the repetition, go to scraper.py and change the value of quantidade_numeros
