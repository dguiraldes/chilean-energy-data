from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

auth_key = os.environ.get("auth_key")


params={'auth_key':auth_key,'anio':2021,'mes':1}

url='https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/sic/tecnologia.json'

response = requests.get(url,params)

print(response.json())
