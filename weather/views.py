from django.shortcuts import render
import json
import urllib.request


# Create your views here.
def index(request):
    if request.method  == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=e3eac307a35b3022f04a1ed7c2204e6c').read()
        json_data = json.loads(res)
        
        data = {
                'country_code' : str(json_data['sys']['country']),
                'coordinate' : str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
                'temp' : str(json_data['main']['temp']) + 'k',
                'pressure' : str(json_data['main']['pressure']),
                'humidity' : str(json_data['main']['humidity'])
                    }
        
        
        
    else:
        data = {}
        city = ''
        
    return render(request, 'index.html', {'data' : data, 'city':city })