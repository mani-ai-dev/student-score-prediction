import getpass
ngrok_key = getpass.getpass("Enter ngrok key:")
Enter ngrok key:··········

!pip install streamlit pyngrok

%%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dataset
data = {
    "Hours": [1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0],
    "Scores": [35,40,45,50,55,60,62,65,70,75,78,80,85,88,90,95]
}
df = pd.DataFrame(data)

# Train linear regression
X = df[["Hours"]]
y = df["Scores"]
linear_model = LinearRegression()
linear_model.fit(X, y)

# Train polynomial regression (degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Predictions for metrics
y_linear_pred = linear_model.predict(X)
y_poly_pred = poly_model.predict(X_poly)

# Streamlit UI
st.title("📘 Student Score Predictor")
st.write("Predict exam scores based on study hours using Linear or Polynomial Regression.")

# User input
hours = st.slider("Select study hours:", 1.0, 10.0, 5.0)
model_choice = st.radio("Choose regression model:", ["Linear", "Polynomial"])

# Prediction
if model_choice == "Linear":
    predicted_score = linear_model.predict([[hours]])[0]
else:
    predicted_score = poly_model.predict(poly.transform([[hours]]))[0]

st.write(f"Predicted Exam Score for {hours} hours: **{predicted_score:.2f}**")

# Metrics Dashboard
st.subheader("📊 Model Performance Metrics")
metrics = {
    "Linear Regression": {
        "R²": r2_score(y, y_linear_pred),
        "MAE": mean_absolute_error(y, y_linear_pred),
        "RMSE": np.sqrt(mean_squared_error(y, y_linear_pred))
    },
    "Polynomial Regression": {
        "R²": r2_score(y, y_poly_pred),
        "MAE": mean_absolute_error(y, y_poly_pred),
        "RMSE": np.sqrt(mean_squared_error(y, y_poly_pred))
    }
}
st.write(pd.DataFrame(metrics).T)

# Visualization
fig, ax = plt.subplots()
ax.scatter(X, y, color="blue", label="Actual Data")

X_range = np.linspace(1, 10, 100).reshape(-1, 1)
ax.plot(X_range, linear_model.predict(X_range), color="red", label="Linear Fit")
ax.plot(X_range, poly_model.predict(poly.transform(X_range)), color="green", label="Polynomial Fit")

ax.set_xlabel("Study Hours")
ax.set_ylabel("Exam Scores")
ax.set_title("Regression Comparison")
ax.legend()
st.pyplot(fig)

Overwriting app.py

from pyngrok import ngrok

port = 8501

ngrok.set_auth_token(ngrok_key)
ngrok.connect(port).public_url

https://channing-semicommunicative-cristopher.ngrok-free.dev

!rm -rf logs.txt && streamlit run app.py &>/content/logs.txt

WARNING:pyngrok.process.ngrok:t=2026-04-17T09:38:08+0000 lvl=warn msg="Stopping forwarder" name=http-8501-ec10ab8b-93a7-41b5-9825-fe6b6ef3784a acceptErr="failed to accept connection: Listener closed"
