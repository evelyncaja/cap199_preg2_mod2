import pandas as pd
import requests
import zipfile
import io
import os

# URL del dataset
url = "https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/master/Cancer_Pulmon.zip"

# Descargar el archivo ZIP
response = requests.get(url)
response.raise_for_status()

# Descomprimir el ZIP
with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
    zip_ref.extractall("data")

# Buscar el archivo CSV
csv_file = None
for file in os.listdir("data"):
    if file.endswith(".csv"):
        csv_file = os.path.join("data", file)
        break

if csv_file is None:
    raise FileNotFoundError("No se encontró ningún archivo CSV en el ZIP")

# Cargar el dataset en memoria
df = pd.read_csv(csv_file)

# Verificación
print(df.head())
