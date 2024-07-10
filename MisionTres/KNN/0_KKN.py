import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as dts 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Cargar el dataset Iris
iris = dts.load_iris()
X = iris.data
y = iris.target

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Estandarizar las características
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Entrenar el clasificador KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_std, y_train)

# Realizar predicciones
y_pred = knn.predict(X_test_std)

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
