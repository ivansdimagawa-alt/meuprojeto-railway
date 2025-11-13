import requests

API_KEY = "AXTEv8EZioZEzGJ4khWCUjR9Mv88zE7U"   # Coloque sua chave da FMP aqui
ISIN = "US0378331005"       # Apple exemplo

url = f"https://financialmodelingprep.com/api/v3/profile/{ISIN}?apikey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    print("Dados recebidos:")
    print(response.json())
else:
    print("Erro:")
    print(response.text)
