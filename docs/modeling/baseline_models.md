# Reporte del Modelo de regresión logística

Este documento contiene los resultados del modelo de regresión logística.

## Descripción del modelo

El modelo de regresión logística es utilizado para predecir el resultado de una variable categórica en función de las variables independientes o predictoras. Es el primer modelo construido y se utilizara para establecer una línea base para el rendimiento de los modelos posteriores.

## Variables de entrada

Lista de las variables de entrada utilizadas en el modelo.
Time,
V1,
V2,
V3,
V4,
V5,
V6,
V7,
V8,
V9,
V10,
V11,
V12,
V13,
V14,
V15,
V16,
V17,
V18,
V19,
V20,
V21,
V22,
V23,
V24,
V25,
V26,
V27,
V28,
Amount

## Variable objetivo

Nombre de la variable objetivo utilizada en el modelo.
Class

## Evaluación del modelo

### Métricas de evaluación

Descripción de las métricas utilizadas para evaluar el rendimiento del modelo.

    Clasificación: accuracy, precision, recall, f1-score, AUC.
    Regresión: r2, error cuadrático medio, error absoluto medio.
    Agrupamiento: coeficiente de silueta, índice de Davies-Bouldin.


### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo de regresión logística, incluyendo las métricas de evaluación.

| | precision | recall | f1-score | support |
| --- | --- | --- | --- | --- |
|accuracy | |  | 1.00 | 7108 |
|macro avg | 1.00 | 1.00 | 1.00 | 7108 |
|weighted avg|1.00 | 1.00 | 1.00 | 7108 |

## Análisis de los resultados

Se presenta la matriz de confusión para mostrar resultados de las metricas

![imagen](https://github.com/dtnech/MDLSproyectoDTN/assets/65313279/dffa353f-2ac9-4594-a5fe-f42274ec6e44)

Descripción de los resultados del modelo de regresión logística.
Los resultados de las metricas evidencian que los test arrojan buenas salidas que conllevan a concluir favorablemente hacia la elección del modelo.

 | Modelo | accuracy score | Precision | Recall | f1_score |
 | --- | --- | --- | --- | --- |
 | ANN 	|  0.99789 |  0.995797 | 1.0 | 0.997894

La ventaja de este modelo es que produjo buenas metricas de evaluación y ajuste.
Es un modelo que no consume muchos recursos y por tanto es facil de estimar.
La desventaja es que no permite ajustar modelos lineales.

## Conclusiones

El modelo de regresión logistica produce resultados muy buenos ya que el accuracy score fue:0.9978897017445132, sin embargo tambien se ajusto un modelo que permita comparar los resulados.

## Referencias

https://www.iartificial.net/como-usar-regresion-logistica-en-python/

https://www.cienciadedatos.net/documentos/py17-regresion-logistica-python

https://www.aprendemachinelearning.com/regresion-logistica-con-python-paso-a-paso/

www.kaggle.com/
