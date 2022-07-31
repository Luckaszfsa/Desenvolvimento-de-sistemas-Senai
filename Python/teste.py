import requests

link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(link)

print(requisicao.json())