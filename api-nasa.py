
import requests
import re


R = '\u001b[31m';
C = '\033[1;36m';
V = '\033[1;92m';
B = '\033[1;97m';
M = '\u001b[35m';

print(f'''
{C}Consumindo {B} API {V} da{R} Nasa{M} 
    by Samde0liveira

''')

response = requests.get('https://api.nasa.gov/planetary/apod?api_key=6mhKfETfzsKDfHnuJauVVoWwEyz65gPOVhLEnhml')
data = response.json()
link_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

for key, value in data.items():
    if isinstance(value, str) and link_regex.search(value):
        print(value)


