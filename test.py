import requests
city_name="New Delhi"
API_key="357174777309cce6ac6cc0d771a72562"

url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

re=requests.get(url)

if re.status_code==200:
    print("yes")
    list_of_data=re.json()
    print(list_of_data)
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
    print("---"*30)
    print(data)