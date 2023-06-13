import requests
from api_key import api_key


para_moeda = input('Para: ')
de_moeda = input('De: ')
valor = input('Valor: ')
url = 'https://api.apilayer.com/exchangenerates_data/convert?'


payload = {
    'to': para_moeda,
    'from': de_moeda,
    'amount': valor
}


headers = {
    'apikey': api_key
}


r = requests.request(
    'GET',
    url,
    headers=headers,
    params=payload
)

print (r.text)
