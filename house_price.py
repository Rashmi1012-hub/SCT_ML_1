# HOUSE PRICE PREDICTION USING LINEAR REGRESSION
# =========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ✅ Load working dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

print("Dataset Preview:")
print(df.head())

# ✅ Select features and target
X = df[['rm', 'lstat', 'ptratio']]   # input features
y = df['medv']                       # house price

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Evaluation
print("\n--- Model Evaluation ---")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ✅ Predict new house price
new_house = pd.DataFrame([[6, 12, 18]],  # example values
                         columns=['rm', 'lstat', 'ptratio'])

predicted_price = model.predict(new_house)
print("\nPredicted Price:", predicted_price[0])

# ✅ Visualization (Graph)
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot(y_test, y_test)  # perfect prediction line
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()# HOUSE PRICE PREDICTION USING LINEAR REGRESSION
# =========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ✅ Load working dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

print("Dataset Preview:")
print(df.head())

# ✅ Select features and target
X = df[['rm', 'lstat', 'ptratio']]   # input features
y = df['medv']                       # house price

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Evaluation
print("\n--- Model Evaluation ---")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ✅ Predict new house price
new_house = pd.DataFrame([[6, 12, 18]],  # example values
                         columns=['rm', 'lstat', 'ptratio'])

predicted_price = model.predict(new_house)
print("\nPredicted Price:", predicted_price[0])

# ✅ Visualization (Graph)
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot(y_test, y_test)  # perfect prediction line
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()# HOUSE PRICE PREDICTION USING LINEAR REGRESSION
# =========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ✅ Load working dataset
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

print("Dataset Preview:")
print(df.head())

# ✅ Select features and target
X = df[['rm', 'lstat', 'ptratio']]   # input features
y = df['medv']                       # house price

# ✅ Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ✅ Train model
model = LinearRegression()
model.fit(X_train, y_train)

# ✅ Predictions
y_pred = model.predict(X_test)

# ✅ Evaluation
print("\n--- Model Evaluation ---")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ✅ Predict new house price
new_house = pd.DataFrame([[6, 12, 18]],  # example values
                         columns=['rm', 'lstat', 'ptratio'])

predicted_price = model.predict(new_house)
print("\nPredicted Price:", predicted_price[0])

# ✅ Visualization (Graph)
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot(y_test, y_test)  # perfect prediction line
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()