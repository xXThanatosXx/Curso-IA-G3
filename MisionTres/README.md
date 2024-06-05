<h1 align="center">Métricas</h1>

### Comparación Matriz de Confusión
```python
y_true = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
y_pred = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0]

# Calcular Verdaderos Negativos (TN)
TN = sum((y_true[i] == 0) and (y_pred[i] == 0) for i in range(len(y_true)))

# Calcular Falsos Positivos (FP)
FP = sum((y_true[i] == 0) and (y_pred[i] == 1) for i in range(len(y_true)))

# Calcular Falsos Negativos (FN)
FN = sum((y_true[i] == 1) and (y_pred[i] == 0) for i in range(len(y_true)))

# Calcular Verdaderos Positivos (TP)
TP = sum((y_true[i] == 1) and (y_pred[i] == 1) for i in range(len(y_true)))

print(f"Verdaderos Negativos (TN): {TN}")
print(f"Falsos Positivos (FP): {FP}")
print(f"Falsos Negativos (FN): {FN}")
print(f"Verdaderos Positivos (TP): {TP}")
```

## Ejemplo Matriz de Confusión

Supongamos que estamos trabajando en un problema de clasificación binaria donde estamos tratando de predecir si un correo electrónico es spam (1) o no spam (0). Hemos entrenado nuestro modelo y ahora queremos evaluarlo usando una matriz de confusión.

Paso 1: Recopilar Predicciones y Etiquetas Reales
Primero, recopilamos las predicciones de nuestro modelo y las etiquetas reales de un conjunto de prueba.

### Paso 1: Recopilar datos
```python
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Supongamos que tenemos las siguientes etiquetas reales y predicciones del modelo
y_true = [0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
y_pred = [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0]

# Crear la matriz de confusión
cm = confusion_matrix(y_true, y_pred)

# Visualizar la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No Spam', 'Spam'], yticklabels=['No Spam', 'Spam'])
plt.xlabel('Clase Predicha')
plt.ylabel('Clase Real')
plt.title('Matriz de Confusión')
plt.show()


```

### Paso 2: Interpretar la Matriz de Confusión
```python
# Generar un informe de clasificación
report = classification_report(y_true, y_pred, target_names=['No Spam', 'Spam'])
print(report)
```


