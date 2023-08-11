from django.shortcuts import render
import requests
# Create your views here.


def index(request):

    city = request.GET.get('city', 'Dhaka')
    # city = 'Dhaka'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b3cf60da29b0fc20f5344be4a432cf55'
    data = requests.get(url).json()
    # print(data)

    payload = {'city': data['name'],
               'weather': data['weather'][0]['main'],
               'icon': data['weather'][0]['icon'],
               'kelvin_temprature': data['main']['temp'],
               'celcius_temprature': data['main']['temp'] - 273,
               'pressure': data['main']['pressure'],
               'humidity': data['main']['humidity'],
               'description': data['weather'][0]['description'],
               'wind': data['wind']['speed'],
               'cloud': data['clouds']['all'],
               'maxtemp': data['main']['temp_max'] - 273,
               'lowtemp': data['main']['temp_min'] - 273,
               }
    context = {'data': payload}
    print(context)
    return render(request, 'index.html', context)
