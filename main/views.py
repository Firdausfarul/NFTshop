from django.shortcuts import render
from random import randint
from requests import get
# Create your views here.
def show_main(request):
    context = reqnft()
    return render(request, "main.html", context)

def reqnft():
    temp = randint(1, 124)
    res = get(f'https://raw.githubusercontent.com/Firdausfarul/Intft_stellar/main/img/test/{temp}.json')
    res = res.json()
    img_url = res['image']
    emoji = res['name']
    country = res['attributes'][0]['value']
    continent = res['attributes'][1]['value']
    return {
        'name': f"{emoji} | {country}",
        'amount': randint(1, 100),
        'description': f"A very beautiful country named {country} that located on {continent}",
        'img': img_url,
        'price': randint(4, 159)
    }