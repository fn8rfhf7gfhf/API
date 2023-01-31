
import requests


R = '\u001b[31m';
C = '\033[1;36m';
V = '\033[1;92m';
B = '\033[1;97m';
M = '\u001b[35m';

print(f'''
{C}Consumindo {B} API {V} da{R} Nasa{M} 
    by Samde0liveira

''')

url = "https://api.nasa.gov/planetary/apod?api_key=6mhKfETfzsKDfHnuJauVVoWwEyz65gPOVhLEnhml"
response = requests.get(url)
print(response.json())
