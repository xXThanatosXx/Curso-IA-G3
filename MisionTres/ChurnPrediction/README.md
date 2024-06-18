
# Predicción de Abandono de Clientes

Este proyecto tiene como objetivo predecir si un cliente va a abandonar el servicio en un futuro cercano utilizando datos de un archivo Excel.


## Estructura del Proyecto

```
ChurnPrediction/
│
├── main.py
├── data_processing.py
├── model.py
├── evaluation.py
├── config.py
└── churn_data.xlsx
```

## Archivos del Proyecto

- `main.py`: Archivo principal que coordina la carga de datos, el preprocesamiento, la construcción y evaluación del modelo.
- `data_processing.py`: Maneja la carga y preprocesamiento de datos.
- `model.py`: Contiene la lógica para construir y entrenar el modelo de machine learning.
- `evaluation.py`: Maneja la evaluación del modelo.
- `config.py`: Contiene configuraciones y constantes utilizadas en el proyecto.
- `churn_data.xlsx`: Archivo Excel con datos ficticios de clientes.

## Librerías Necesarias

Para ejecutar este proyecto, necesitarás instalar las siguientes librerías:

```bash
pip install pandas numpy scikit-learn imbalanced-learn openpyxl
```

## Descripción del Flujo del Proyecto

1. **Carga de Datos**: Se carga el archivo `churn_data.xlsx` utilizando `pandas`.
2. **Preprocesamiento de Datos**: 
   - Se separa la variable objetivo (`Churn`) de las características.
   - Se convierten las variables categóricas en variables dummy.
   - Se dividen los datos en conjuntos de entrenamiento y prueba.
   - Se estandarizan las características.
3. **Sobremuestreo de la Clase Minoritaria**: Utilizando SMOTE para equilibrar las clases.
4. **Entrenamiento del Modelo**: Utilizando RandomForest y Gradient Boosting con búsqueda de hiperparámetros.
5. **Evaluación del Modelo**: Se evalúa el modelo utilizando los datos de prueba y validación cruzada.

## Resultados Obtenidos

### Reporte de Clasificación
```
              precision    recall  f1-score   support

           0       1.00      0.50      0.67         2
           1       0.50      1.00      0.67         1

    accuracy                           0.67         3
   macro avg       0.75      0.75      0.67         3
weighted avg       0.83      0.67      0.67         3
```

### AUC-ROC
```
AUC-ROC: 1.00
```

### Validación Cruzada
```
Cross-Validation Accuracy scores: [0.66666667 0.66666667 0.33333333]
Mean Accuracy: 0.56 ± 0.16
```

## Interpretación de los Resultados

1. **Reporte de Clasificación**:
   - **Clase 0 (No Churn)**:
     - **Precisión**: 1.00 - El modelo identifica todos los no abandonos correctamente.
     - **Recall**: 0.50 - El modelo detecta correctamente solo la mitad de los no abandonos reales.
     - **F1-Score**: 0.67 - Promedio armónico de precisión y recall.
   - **Clase 1 (Churn)**:
     - **Precisión**: 0.50 - La mitad de las predicciones de abandono son correctas.
     - **Recall**: 1.00 - El modelo detecta correctamente todos los abandonos reales.
     - **F1-Score**: 0.67 - Promedio armónico de precisión y recall.

2. **AUC-ROC**: 
   - Un valor de 1.00 indica que el modelo es capaz de distinguir perfectamente entre las clases en el conjunto de prueba. Esto puede ser un indicativo de overfitting, especialmente con conjuntos de datos pequeños.

3. **Validación Cruzada**:
   - Las puntuaciones de accuracy varían, indicando una posible inestabilidad en el modelo.
   - **Mean Accuracy**: 0.56 - El rendimiento promedio es relativamente bajo.
   - **Standard Deviation**: 0.16 - Hay variación en las puntuaciones de accuracy, lo que sugiere que el modelo podría estar generalizando mal.


## Instrucciones para Ejecutar el Proyecto

1. **Colocar el Archivo de Datos**: Asegúrate de tener el archivo `churn_data.xlsx` en la raíz del proyecto.
2. **Instalar Dependencias**: Asegúrate de tener todas las dependencias instaladas ejecutando `pip install`.
3. **Ejecutar el Script Principal**: Ejecuta `main.py` para asegurarte de que todo funciona correctamente.

```bash
python main.py
```

