from django.shortcuts import render
from decouple import config
import json
import requests
#from requests import Session, Request

apiKey = config('APITOKEN')

headers = {
            'authorization': apiKey

    }

def home(request):
    url ='https://min-api.cryptocompare.com/data/v2/news/?lang=EN'
    url2 = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP&tsyms=USD'

    price_r = requests.get(url2,headers)
    price = json.loads(price_r.content)

    response = requests.get(url,headers)
    api = json.loads(response.content)
    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):

    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()

        quoteUrl = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + quote + '&tsyms=USD'

        quoteResponse = requests.get(quoteUrl,headers)
        quoteApi = json.loads(quoteResponse.content)

        return render(request, 'prices.html',{'quote': quote,'quoteApi':quoteApi})

    else:
        return render(request, 'prices.html',{})
