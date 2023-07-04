# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

El dataset esta compuesto por 31 columnas con 284.806 registros. 
30 variables son tipo float y 1 int64. Los datos de las diferentes variables están en un formato igual y por lo tanto no se evidencia mezcla de formatos.
El archivo en el cual están es de tipo csv.
El tamaño del conjunto de datos es de 67.4 MB.
Al verificar datos faltantes y se encontró que no hay, no existen datos ilegibles o con problemas de codificación.
Los resultados de las medidas de tendencia central y también un boxplot múltiple, permiten evidenciar la presencia de algunos datos atípicos, sin embargo, en general se observa un comportamiento normal en la mayor parte de las variables.

## Resumen de calidad de los datos

No hay datos faltantes y por tanto el porcentaje de datos faltantes es cero. Se evidenció la presencia de algunos datos extremos, pero no se encontraron errores ni duplicidad de registros.
No se requiere limpieza de la información ya que los datos no presentan información inconsistente, sin embargo si se requiere aumentar el número de muestras debido al desequilibrio que existe y para ello se realiza submuestreo y sobremuestreo.

## Variable objetivo

La variable objetivo se llama "Class" y representa las transacciones con tarjeta de crédito fraudulentas o no para una entidad financiera, es categorica, contiene los valores 0 y 1, 0 indica que son transacciones normales y 1 para aquella transacciones fraudulentas.
La variable contiene un desbalanceo en los datos, ya que en el grupo 0 esta el mayor porcentaje de las observaciones 284.315 que equivalen al 99.83%, mientras que en el 1 hay 492 que equivalen al 0.17%.


## Variables individuales

Con la matriz de correlaciones se puede evidenciar que no hay correlación alta entre la variable objetivo y las demás variables, tampoco es altamente significativa entre las demás variables.
A continuación se presenta el boxplot que permite analizar el comportamiento estadístico de la variable:

![imagen](https://github.com/dtnech/MDLSproyectoDTN/assets/65313279/3c4fdbb5-2d4c-4cef-8db4-eba5de6f8d39)

A continuación se pueden observavar los graficos de dispersión de las variables Amount y Time teniendo en cuenta el grupo de transacciones sin fraude y el grupo con fraude.

![imagen](https://github.com/dtnech/MDLSproyectoDTN/assets/65313279/240d3466-44bd-4b26-8326-e77325db6f6a)

![imagen](https://github.com/dtnech/MDLSproyectoDTN/assets/65313279/4fbae36e-0090-4363-b2f2-15c9a92c1b78)

Debido al desequilibrio que existe entre los grupos se realiza submuestreo y sobremuestreo, para lo anterior se procede a aumentar el número de muestras.

## Ranking de variables

A continuación se presenta el grafico de correlaciones entre variables:
![imagen](https://github.com/dtnech/MDLSproyectoDTN/assets/65313279/eea4c5ec-fbd1-4277-b0af-bae1afc78d95)

## Relación entre variables explicativas y variable objetivo

Como se menciono en el punto anterior, con la matriz de correlaciones se puede evidenciar que no hay correlación alta entre la variable objetivo y las demás variables.

La variable objetivo class es categórica y puede ser explicada por las demás variables, se procederá a ajustar un modelo de regresión logística y se utilizaran técnicas de machine learning usando las herramientas de TensorFlow.

La matriz de correlación y el diagrama de dispersión se presentó en literales anteriores y por tal razón no se presentan de nuevo.
