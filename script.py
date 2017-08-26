import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dateutil
import urllib.request
import requests

def obtenerFabricante(macAddress):

    validador = "^(([0-9A-Fa-f]{2}:){5})([0-9A-Fa-f]{2})$"

    peticion = requests.get("http://www.macvendorlookup.com/oui.php?mac={}".format(macAddress), verify=False)
    print(peticion.text + str(peticion.status_code))
    if peticion.status_code != 200 or not(peticion.text):
        return None
    infoJson = peticion.json()
    # print()
    fabricante = infoJson[0]["company"]
    return fabricante




# infoMacAddress = obtenerFabricante("74:AA:FE:A5:7E:90")
# print(infoMacAddress)
# In[55]:
validacionMAC = "^(([0-9A-Fa-f]{2}:){5})([0-9A-Fa-f]{2})$"


dateparse = lambda x: pd.datetime.strptime(x,'%Y-%m-%d %h:%m:%s')
data = pd.read_csv('./tmp/rp_conexion.csv',sep=';',index_col=False, parse_dates={'datetime':['fecha','hora']}, usecols=["codigo","pauta_id","sitio_id","mac_usr","fecha","hora","ip_local","ip_usr","so","navegador","url_ref","tiempo_espera"])

data["filtroMAC"] = data['mac_usr'].str.contains(validacionMAC)
# data = data[filter]

# print(data)

data = data[data["filtroMAC"] == True]

# print(nuevoData)

del data["filtroMAC"]

# data = data[:10000]

# print(len(data))

try:

    data["fabricante-dispositivo"] = data["mac_usr"].apply(obtenerFabricante)

except:

    data.to_csv("dispositivos_fabricantes_excepcion.csv")

finally:

    data.to_csv("dispositivos_fabricantes.csv")

# data.to_csv("dispositivos_fabricantes.csv")

# print(data)

# dispositivos = data.groupby("so").size()
#
# print(dispositivos)