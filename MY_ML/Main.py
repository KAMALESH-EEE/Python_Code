import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('CGPA.csv')

# Prepare data
X = df[['CGPA']].values
y = df['Gender'].values

# Polynomial Regression
degree = 10
polynomial_features = PolynomialFeatures(degree=degree)
X_poly = polynomial_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)

# Evaluation
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Visualization
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, y_pred, color='red', label='Polynomial fit')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.title('Polynomial Regression')
plt.legend()

new_data = np.array([[9.156], [7.987], [9.174]]) 

new_data_poly = polynomial_features.transform(new_data)

new_predictions = model.predict(new_data_poly)
b='Boy'
g='Girl'

for i, value in enumerate(new_data):
    print(f"Prediction for {value[0]}: {b if new_predictions[i].__round__()==1 else g}")

plt.show()