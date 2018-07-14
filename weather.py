import requests


k = '4e5024e5f10a558109305cd63350bd37'


def get_city_number(city_name):
    r = requests.get(
        'http://restapi.amap.com/v3/config/district?key={}&keywords={}&subdistrict={}'.format(k, city_name, 0))
    if r.json()['count'] == '0':
        adcode = '330109'
    else:
        adcode = r.json()['districts'][0]['adcode']
    return adcode


def get_weather(city_name, key=k):
    if not city_name:
        city_name = '萧山'

    city_num = get_city_number(city_name)
    if city_name == '澳门':
        city_num = '820000'
    r = requests.get(
        'http://restapi.amap.com/v3/weather/weatherInfo?key={}&city={}&extensions={}'.format(key, city_num, 'all'))
    fore = r.json()['forecasts'][0]
    city = fore['city']
    time = fore['reporttime'].split(' ')[0]
    for i in fore['casts']:
        if i['date'] == time:
            dayweather = i['dayweather']
            nightweather = i['nightweather']
            daytemp = i['daytemp']
            nighttemp = i['nighttemp']
            return '{} \n白天:{}  温度{}\n晚上:{}  温度{}'.format(city, dayweather, daytemp, nightweather, nighttemp)


if __name__ == '__main__':
    print(get_city_number(''))
    print(get_weather('狗屎'))
