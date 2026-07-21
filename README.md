# Machine Learning Day 3 - Logistic Regression Projects

## 📖 Overview

This repository contains two **Supervised Machine Learning** classification projects built using **Logistic Regression** with **Python** and **Scikit-learn**.

These projects demonstrate how Logistic Regression can be applied to solve real-world classification problems in healthcare and email security.

---

# 🩺 Project 1: Diabetes Prediction Using Logistic Regression

## 🎯 Objective

Develop a Machine Learning model to predict whether a patient is diabetic based on medical attributes.

## 📊 Dataset

- **File:** `diabetes.csv`
- **Target Variable:** `Outcome`
  - `0` → Not Diabetic
  - `1` → Diabetic

## 📝 Features Used

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

## ⚙️ Workflow

- Load the dataset
- Data preprocessing
- Split data into training and testing sets
- Train Logistic Regression model
- Evaluate model accuracy
- Predict diabetes status for a new patient
- Display prediction as **Diabetic** or **Not Diabetic**

## 📈 Evaluation

- Accuracy Score

## 💻 Sample Output

```text
Model Accuracy: 74.68%

Patient Details
Pregnancies: 2
Glucose: 120
Blood Pressure: 70
Skin Thickness: 20
Insulin: 80
BMI: 25.5
Diabetes Pedigree Function: 0.4
Age: 35

Prediction: Not Diabetic
```

---

# 📧 Project 2: Email Spam Detection Using Logistic Regression

## 🎯 Objective

Build a Machine Learning model to classify emails as **Spam** or **Not Spam** using Natural Language Processing (NLP).

## 📊 Dataset

- **File:** `completeSpamAssassin.csv`

## ⚙️ Workflow

- Load dataset
- Remove unnecessary columns
- Handle missing values
- Convert email text into numerical features using **CountVectorizer**
- Split dataset into training and testing sets
- Train Logistic Regression model
- Evaluate model performance
- Predict whether a new email is Spam or Not Spam

## 📈 Evaluation

- Accuracy Score
- Classification Report
- Confusion Matrix

## 💻 Sample Output

```text
Accuracy: 98.45%

Prediction: Spam
```

---

# 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- CountVectorizer

---

# 📚 Machine Learning Concepts

- Supervised Learning
- Classification
- Logistic Regression
- Train-Test Split
- Model Training
- Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report
- Natural Language Processing (NLP)
- Text Vectorization

---

# ⭐ Features

- Clean and well-structured Python code
- Data preprocessing
- Logistic Regression implementation
- Model accuracy evaluation
- Custom prediction examples
- User-friendly prediction output
- Real-world Machine Learning classification projects

---

# 🚀 Future Improvements

- Feature Scaling using StandardScaler
- Hyperparameter Tuning
- Model Deployment using Streamlit or Flask
- Save trained models using Pickle
- Add graphical user interface (GUI)
- Improve prediction performance with advanced algorithms

---

# 📁 Repository Structure

```text
Machine-Learning-Day-3-Projects/
│
├── Diabetes_Prediction.py
├── diabetes.csv
├── Email_Spam_Detection.py
├── completeSpamAssassin.csv
├── requirements.txt
├── README.md
└── images/
    ├── project_cover.png
    ├── diabetes_output.png
    └── spam_output.png
```

---

# ▶️ How to Run

1. Clone this repository.

```bash
git clone https://github.com/iqrakhan07/Machine-Learning-Day-3-Projects.git
```

2. Install the required libraries.

```bash
pip install -r requirements.txt
```

3. Run any project.

```bash
python Diabetes_Prediction.py
```

or

```bash
python Email_Spam_Detection.py
```

---

# 👩‍💻 Author

**Iqra Khan**

- Computer Engineering Student
- Machine Learning Intern at Visual Labs

---

## ⭐ If you found these projects useful, consider giving this repository a star!
