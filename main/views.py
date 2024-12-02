import requests
import json
from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    if request.method == 'POST':
        API_key="357174777309cce6ac6cc0d771a72562"
        try:
            city_name= request.POST['city']

            url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

            re=requests.get(url)
            list_of_data=re.json()
            data = {
                    "city_name":str(list_of_data['name']),
                    "country_code": str(list_of_data['sys']['country']),
                    "coordinate": str(list_of_data['coord']['lon']) + ', '
                    + str(list_of_data['coord']['lat']),

                    "temp": str(list_of_data['main']['temp']) + ' °C',
                    "pressure": str(list_of_data['main']['pressure']),
                    "humidity": str(list_of_data['main']['humidity']),
                    'main': str(list_of_data['weather'][0]['main']),
                    'description': str(list_of_data['weather'][0]['description']),
                    'icon': list_of_data['weather'][0]['icon'],
                }
        except Exception:
            return render(request,"main/not.html")

    else:
        data = {}

    return render(request, "main/index.html", data)
