import requests
import json
#import pandas 
import pandas as pd

print("\nConfirmed")
url_confirmed='https://covid19api.herokuapp.com/confirmed'
response_confirmed=requests.get(url_confirmed)

#De la página de donde se obtienen casos confirmados, se pide como formato json las locaciones de todos los confirmados
if response_confirmed.status_code==200:
    response_json=json.loads(response_confirmed.text) #y aqui los datos se hacen diccionario
    locations_confirmed=response_json['locations']
  #  print(locations)

for steps in locations_confirmed: #se busca en el diccionario 
    if steps['country_code'] == 'MX': 
        mexico_confirmed = steps
        break

del mexico_confirmed['coordinates']
del mexico_confirmed['country']
del mexico_confirmed['country_code']
del mexico_confirmed['province']
del mexico_confirmed['latest']

print(mexico_confirmed) #se imprime la busqueda del diccionario

mexico_confirmed_df=pd.DataFrame(mexico_confirmed)
mexico_confirmed_df.to_csv(r'C:\Users\Abigail\Documents\Proyectos\COVID\mexico_confirmed.csv',index=True)

print("\n\n\nDeaths")

url_deaths='https://covid19api.herokuapp.com/deaths'
response_deaths=requests.get(url_deaths)

if response_deaths.status_code==200:
    response_json=json.loads(response_deaths.text)
    locations_deaths=response_json['locations']
  
for steps in locations_deaths: 
    if steps['country_code'] == 'MX': 
        mexico_deaths = steps
        break

del mexico_deaths['coordinates']
del mexico_deaths['country']
del mexico_deaths['country_code']
del mexico_deaths['province']
del mexico_deaths['latest']
print(mexico_deaths)
mexico_deaths_df=pd.DataFrame(mexico_deaths)
mexico_deaths_df.to_csv(r'C:\Users\Abigail\Documents\Proyectos\COVID\mexico_deaths.csv',index=True)

print("\n\n\nRecovered")

url_recovered='https://covid19api.herokuapp.com/recovered'
response_recovered=requests.get(url_recovered)

if response_recovered.status_code==200:
    response_json=json.loads(response_recovered.text)
    locations_recovered=response_json['locations']


for steps in locations_recovered: 
    if steps['country_code'] == 'MX': 
        mexico_recovered = steps
        break

del mexico_recovered['coordinates']
del mexico_recovered['country']
del mexico_recovered['country_code']
del mexico_recovered['province']
del mexico_recovered['latest']
print(mexico_recovered)

mexico_recovered_df=pd.DataFrame(mexico_recovered)
mexico_recovered_df.to_csv(r'C:\Users\Abigail\Documents\Proyectos\COVID\mexico_recovered.csv',index=True)
    
