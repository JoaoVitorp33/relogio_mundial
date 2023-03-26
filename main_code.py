# Instalar pytz: pip install pytz

from datetime import datetime
from pytz import country_timezones
import pytz

from paises import *

# Obtendo zonas de fuso horario

time_zones = pytz.all_timezones

# Obtendo zonas com abreviação do país

timezone_country = {}

for i in country_timezones:
    timezones = country_timezones[i]
    for y in timezones:
        timezone_country[y] = i
        
# Lista das zonas (fuso horario)

zona = []

for i in timezone_country.keys():
    zona.append(i)
    
# Convertendo a zona selecionada no formato de timezone

zona_selecionada = pytz.timezone(zona[2])
country_time = datetime.now(zona_selecionada)

# Obtendo o nome do país da zona selecionada

simbolo_do_pais = [timezone_country[zona[2]]]

for i in paises.keys():
    simbolo_do_pais.append(i.lower())

# Pegando o local da imagem

imagem = "png250px/{}.{}".format(simbolo_do_pais[0],'png').lower()

# Obtendo a chave do pais em letra maiusculas

key = simbolo_do_pais[0].upper()

# Obtendo o nome do pais

nome_do_pais = paises[key]

print(f"A data da {zona_selecionada} é {country_time.strftime('%d-%m-%y')} e o país é {nome_do_pais} e lá são {country_time.strftime('%H:%M:%S')}")

  
