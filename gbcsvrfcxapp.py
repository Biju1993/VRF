from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os
import streamlit as st
from streamlit.components.v1 import iframe
import psychrolib
import requests
import pandas as pd



st.image("data:image/jpeg;base64,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")
st.title("VRF COMMISSIONING REPORT GENERATOR")

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("new.html")

form = st.form("template_form")

v1 = form.text_input("ENTER PROJECT NAME")
v2= form.date_input("DATE OF INSPECTION")

def get_location():
    try:
        # Make a request to ipinfo.io to get the location information based on the user's IP address
        response = requests.get('http://ipinfo.io')
        data = response.json()

        # Parse the location data
        ip = data.get('ip')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        location = f"IP: {ip}, City: {city}, Region: {region}, Country: {country}"
        # return location
        return city

    except Exception as e:
        return f"Error: {e}"

CURRENT_LOCATION=get_location()

SITE_LOCATION_OF_THE_UNIT=st.selectbox(" SITE_LOCATION_OF_THE_UNIT",[CURRENT_LOCATION,'pune','bangalore','mumbai', 'chennai'],)
v3 = form.text_input("LOCATION OF IDU")
v4 = form.text_input("ODU CAPACITY")
v5 = form.text_input("CIRCUIT NAME")
v6 = form.text_input("LOCATION ODUDRG Sr.NO")
v7 = form.text_input("LOCATION ODU")
v8 = form.text_input("ODU Sr.No")

form.subheader("IDU COOLING CAPACITY MEASUREMENT")
v9=st.number_input("ENTER MEASURED AIR FLOW RATE IN CFM")
v11= form.slider("ENTER RETURN AIR DBT IN DEG C", min_value=10, max_value=50, value=None, step=0.5)
v13= form.slider("ENTER RETURN AIR WBT IN DEG C", min_value=10, max_value=50, value=None, step=0.5)
v12= form.slider("ENTER SUPPLY AIR DBT IN DEG C", min_value=10, max_value=50, value=None, step=0.5)
v14= form.slider("ENTER SUPPLY AIR WBT IN DEG C", min_value=10, max_value=50, value=None, step=0.5)

v18=st.number_input("ENTER MEASURED VOLTAGE")
v20=st.number_input("ENTER MEASURED CURRENT")

v19=v18
v21=v20


# OpenWeatherMap API endpoint and API key
weather_api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "8af1a752ec6e57631f899729ded7eba5"  # Replace this with your actual OpenWeatherMap API key

params = {'q':  SITE_LOCATION_OF_THE_UNIT,
            'appid': api_key,
            'units': 'metric'  }
response = requests.get(weather_api_endpoint, params=params)
if response.status_code == 200:
    weather_data = response.json()
    main = weather_data['main']
    weather = weather_data['weather'][0]['description']
    temperature = main['temp']
    atm= main['pressure']
    humidity = main['humidity']
    lon=(weather_data['coord']['lon'])
    lat=(weather_data['coord']['lat'])
    win=(weather_data['wind']['speed'])
    city=(weather_data['name'])
else:
    print("Error fetching weather data.")

atmpressure=atm*100
psychrolib.SetUnitSystem(psychrolib.SI)
indbt=v11
inwbt=v13
outdbt=v12
outwbt=v14

inair=psychrolib.CalcPsychrometricsFromTWetBulb(indbt, inwbt, atmpressure)
outair=psychrolib.CalcPsychrometricsFromTWetBulb(outdbt, outwbt, atmpressure)

inh=inair[4]/1000*0.429923
outh=outair[4]/1000*0.429923
dh=inh-outh
# print(inh,outh)
cfm=v9
# print(f"AHU'S MEASURED AIR FLOW RATE IS {cfm} CFM")
tr=4.5*cfm*dh/12000

v15=inh
v16=outh
v17=dh
v23=tr
v22=v23*3.517
v24=v23*12000


submit = form.form_submit_button("GENERATE REPORT")

if submit:
    html = template.render(V1=v1,
V2=v2,
V3=v3,
V4=v4,
V5=v5,
V6=v6,
V7=v7,
V8=v8,
V9=v9,
V11=v11,
V12=v12,
V13=v13,
V14=v14,
V15=v15,
V16=v16,
V17=v17,
V18=v18,
V19=v19,
V20=v20,
V21=v21,
V22=v22,
V23=v23,
V24=v24
)
    with open("new.html", "w") as f:
        f.write(html)
    f.close()
    st.download_button("⬇️ Download Report",data=html,file_name=v3+".html") 
