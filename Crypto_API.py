# Our Team: Utsav, Rudra
import requests
import json
import wikipedia
import urllib.request
from PIL import Image

def top_cryptocurrencies():
    headers = {
        'X-CMC_PRO_API_KEY' : 'a55593bf-4aae-4ffa-83c8-db4d326abc7d',
        'Accepts': 'application/json'
    }

    n=int(input("Enter the value of n: "))
    parameters = {
        'start':'1',
        'limit':n,
        'convert':'INR'
    }

    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', params=parameters, headers=headers).json()
    for x in r['data']:
        print(x['name'],x['symbol'],x['quote']['INR']['price'])


def specific_currency_price():
    headers = {
        'X-CMC_PRO_API_KEY' : 'a55593bf-4aae-4ffa-83c8-db4d326abc7d',
        'Accepts': 'application/json'
    }

    parameters = {
        'start':'1',
        'limit':500,
        'convert':'INR'
    }

    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', params=parameters, headers=headers).json()

    crypto = input('Enter name of cryptocurrency : ')
    count=0
    for x in r['data']:
        if x['name'] == crypto:
            print(x['quote']['INR']['price'])
            count+=1
    if count == 0:
        print('This cryptocurrency is not present in the list')


def compare_currencies():
    headers = {
        'X-CMC_PRO_API_KEY' : 'a55593bf-4aae-4ffa-83c8-db4d326abc7d',
        'Accepts': 'application/json'
    }

    parameters = {
        'start':'1',
        'limit':500,
        'convert':'INR'
    }

    r = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest', params=parameters, headers=headers).json()

    c1 = input('Enter 1st cryptocurrency : ')
    c2 = input('Enter 2nd cryptocurrency : ')
    count=0
    for x in r['data']:
        if x['name'] == c1:
            symbol1 = x['symbol']
            price1 = x['quote']['INR']['price']
            count+=1
        elif x['name'] == c2:
            symbol2 = x['symbol']
            price2 = x['quote']['INR']['price']
            count+=1
    if count<2:
        print('Invalid cryptocurrencies')
    else:
        if price1>price2:
            compare = price1/price2
            print('1',symbol1,'=',compare,symbol2)
        else:
            compare = price2/price1
            print('1',symbol2,'=',compare,symbol1)

       
def cryptocurrency_info():
    value_input = input("Enter name of cryptocurrency: ")
    k = value_input.capitalize()

    try:
        temp = wikipedia.summary(k)
        print(temp)
    except:
        temp1 = k+" crypto"
        temp = wikipedia.summary(temp1)
        print(temp)

def cryptocurrency_image():
    value_input = input("Enter name of cryptocurrency: ")
    k = value_input.capitalize()
    url1 = f"https://imsea.herokuapp.com/api/1?q={k}"
    try:
        respons1 = requests.get(url1)
        data1 = json.loads(respons1.text)
        y = data1["results"][0]
        urllib.request.urlretrieve(f'{y}',"gfg.png") 
        img = Image.open("gfg.png")
        img.show()
    except:
        print("No image found, try again for another currency")


while True:
    print('''Hello User. This application uses API to extract information from Coin Market Gap and Wikipedia about cryptocurrencies.
A total of 5 endpoints have been created. Enter :
1 to Display the top "n" cryptocurrencies in the market
2 to Get the price of a specific cryptocurrency in Rupees(INR)
3 to Get the exchange rate of one cryptocurrency in terms of another
4 to Get some information/summary about a specific cryptocurrency
5 to Get  an image associated with a specific cryptocurrency
6 to Quit the application''')
    print()
    
    menu_control = int(input())
    if menu_control == 6:
        print()
        break
    else:
        if menu_control == 1:
            top_cryptocurrencies()
        elif menu_control == 2:
            specific_currency_price()
        elif menu_control == 3:
            compare_currencies()
        elif menu_control == 4:
            cryptocurrency_info()
        elif menu_control == 5:
            cryptocurrency_image()
        print()
