import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import log_loss, confusion_matrix

# Cargar el conjunto de datos Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar las características para mejorar el rendimiento del MLP
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar un MLP
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000, alpha=0.001,
                    solver='adam', verbose=10, tol=0.0001, random_state=1,
                    learning_rate_init=.01)

mlp.fit(X_train_scaled, y_train)

# Calcular la pérdida de entrenamiento usando la loss_curve_
train_loss = mlp.loss_curve_

# Calcular la pérdida de prueba (sólo después de todo el entrenamiento para simplificar)
y_test_pred_prob = mlp.predict_proba(X_test_scaled)
test_loss_value = log_loss(y_test, y_test_pred_prob)

# Graficar pérdida de entrenamiento y línea horizontal para pérdida de prueba
plt.plot(train_loss, label='Training loss')
plt.axhline(test_loss_value, color='red', linestyle='--', label='Test loss after training')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Matriz de confusión
y_test_pred = mlp.predict(X_test_scaled)
cm = confusion_matrix(y_test, y_test_pred)

# Imprimir matriz de confusión
print("Matriz de Confusión:")
print(cm)

# Visualizar matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap="YlGnBu", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()
