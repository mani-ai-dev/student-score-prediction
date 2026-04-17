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
![Graph](https://github.com/mani-ai-dev/student-score-prediction/blob/7638647474c4ed4b7f9298a42c28279a7419c50f/images/Screenshot%202026-04-17%20145841.png)

### Streamlit App
![App](https://github.com/mani-ai-dev/student-score-prediction/blob/289239d4072c9e35617da8415e874daa26a73b70/images/Screenshot%202026-04-17%20145826.png)

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
