import requests
import json
from tkinter import *

def show_data(country_code):
    url_confirmed='https://covid19api.herokuapp.com/confirmed'
    response_confirmed=requests.get(url_confirmed)


    if response_confirmed.status_code==200:
        response_json=json.loads(response_confirmed.text) 
        locations_confirmed=response_json['locations']
    

    for steps in locations_confirmed: 
        if steps['country_code'] == country_code.upper(): 
            confirmed = steps['latest']
         else:
            deaths_tk["text"]="Enter a valid country code"

    confirmed_tk["text"]="Confirmed: "+str(confirmed)


    url_deaths='https://covid19api.herokuapp.com/deaths'
    response_deaths=requests.get(url_deaths)

    if response_deaths.status_code==200:
        response_json=json.loads(response_deaths.text)
        locations_deaths=response_json['locations']
    
    for steps in locations_deaths: 
        if steps['country_code'] == country_code.upper(): 
            deaths = steps['latest']
            break

    deaths_tk["text"]="Deaths: "+str(deaths)

    url_recovered='https://covid19api.herokuapp.com/recovered'
    response_recovered=requests.get(url_recovered)

    if response_recovered.status_code==200:
        response_json=json.loads(response_recovered.text)
        locations_recovered=response_json['locations']


    for steps in locations_recovered: 
        if steps['country_code'] == country_code.upper(): 
            recovered = steps['latest']
            break

    recovered_tk["text"]="Recovered: "+str(recovered)

#ventana

ventana=Tk()
ventana.geometry("400x400")

main_title=Label(text="COVID-19 en el mundo", font=("Arial", 20,"normal"), justify="center")
main_title.pack(padx=10,pady=10)
main_title=Label(text="Fuente: John Hopkins University Center", font=("Arial", 12,"normal"), justify="center")
main_title.pack(padx=10,pady=10)

enter_countryCode=Entry(ventana, font=("Calibri",25,"normal"), justify="center")
enter_countryCode.pack(padx=10,pady=10)

obtain_data=Button(ventana,text="Enter",font=("Arial", 15,"normal"), justify="center",command=lambda:show_data(enter_countryCode.get()))
obtain_data.pack()

confirmed_tk=Label(ventana,fg="blue", font=("Calibri",25,"normal"), justify="center")
confirmed_tk.pack(padx=10,pady=10)

deaths_tk=Label(ventana, fg="red",font=("Calibri",25,"normal"), justify="center")
deaths_tk.pack(padx=10,pady=10)

recovered_tk=Label(ventana,fg="green", font=("Calibri",25,"normal"), justify="center")
recovered_tk.pack(padx=10,pady=10)

ventana.mainloop()
