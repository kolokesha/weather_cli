import requests

weather_parameters = {
    '0': '',
    'T': '',
    'M': ''
}


def weather(city):
    url = 'http://wttr.in'
    new_url = url + '/' + city
    response = requests.get(new_url, params=weather_parameters)
    return response.text


if __name__ == '__main__':
    print('City?')
    print(weather(input()))
