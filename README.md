#  House Price Prediction using Linear Regression

## Description
This project uses **Linear Regression** to predict house prices based on features like number of rooms, population status, and other factors. It demonstrates a basic machine learning workflow including data preprocessing, model training, and evaluation.

---

## Project Overview
- Applied **Supervised Learning (Linear Regression)**
- Split data into training and testing sets
- Evaluated model using MAE and R² Score
- Visualized actual vs predicted prices

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  

---

## Dataset
- Boston Housing Dataset  
- Features used:
  - rm (number of rooms)
  - lstat (lower status population %)
  - ptratio (student-teacher ratio)

---

##  How to Run

```bash
pip install pandas numpy matplotlib scikit-learn
python house_price.py

 ## Output
🔹 Dataset Preview
crim    zn   indus  ...   b   lstat   medv
0.00632 18.0 2.31  ... 396.90 4.98   24.0
0.02731 0.0  7.07  ... 396.90 9.14   21.6
...
🔹 Model Evaluation
MAE: 3.33
R² Score: 0.63
🔹 Predicted Price
21.77
