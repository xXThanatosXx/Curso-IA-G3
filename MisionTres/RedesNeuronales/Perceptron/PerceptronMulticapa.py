from sklearn  import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

# X = X[y != 2][:, [0, 1]]
# y = y[y != 2]
# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Estandarizar las características
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Entrenar el Perceptrón Multicapa
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=40, alpha=0.001, learning_rate_init=0.15, random_state=1,solver='adam',activation='relu')
mlp.fit(X_train_std, y_train)

# Realizar predicciones
y_pred = mlp.predict(X_test_std)

# Evaluar el rendimiento del modelo
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2f}')

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Graficar la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Graficar el error por época de entrenamiento
plt.figure(figsize=(8, 6))
plt.plot(range(1, len(mlp.loss_curve_) + 1), mlp.loss_curve_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss per Epoch')
plt.show()
