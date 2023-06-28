# Definición de los datos

## Origen de los datos

- Los datos fueron extraídos de kaggle. No se utilizó ninguna herramienta, se descargó directamente desde la página de kaggle.

## Especificación de los scripts para la carga de datos

- Se utilizo un script para la carga de los datos, para esto se utilizaron paquetes como los siguientes:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

## Referencias a rutas o bases de datos origen y destino
- Los datos fueron extraídos de kaggle.
- df = pd.read_csv('/content/creditcard.csv', sep=';')
- https://drive.google.com/file/d/1Uy7hxc8I1pmRy5SVkuKoHK2xFPZ0bS0k/view?usp=sharing

### Rutas de origen de datos

- La ubicación de los archivos de origen de los datos es el drive de google.
- La estructura de los archivos utilizados es de tipo csv
- Se procedió a verificar si hay datos faltantes y se encontró que no, tampoco existen datos ilegibles o con problemas de codificación.
- Los datos de las diferentes variables están en un formato igual y por lo tanto no se evidencia mezcla de formatos.


### Base de datos de destino

- No se requiere base de datos de destino para los datos.
- [NA] Especificar la estructura de la base de datos de destino.
- El procedimiento de carga y transformación de los datos en la base de datos de destino no se requiere.
