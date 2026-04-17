# 🎓 Student Score Prediction using Machine Learning

## 📌 Problem Statement
Predict student exam scores based on study hours using regression techniques.

---

## 📊 Dataset
Synthetic dataset created using Python:
- Feature: Study Hours
- Target: Exam Scores

---

## ⚙️ Approach

### 🔹 Data Analysis
- Visualized relationship using scatter plot
- Observed strong positive correlation

### 🔹 Model Building
- Linear Regression
- Polynomial Regression (degree = 2)

### 🔹 Evaluation Metrics
- R² Score
- MAE
- RMSE

---

## 📈 Results
- Linear regression provided good baseline accuracy
- Polynomial regression improved prediction performance
- Clear relationship between study time and performance

---

## 🌐 Deployment
- Built interactive web app using Streamlit
- Enabled real-time predictions

---

## 📷 Output

### Scatter Plot
![Graph](images/graph.png)

### Streamlit App
![App](images/app.png)

---

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app/app.py
