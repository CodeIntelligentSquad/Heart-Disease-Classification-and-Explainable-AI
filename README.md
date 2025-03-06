# ❤️ Heart Disease Classification & Explainable AI
 
![download](https://github.com/user-attachments/assets/29374782-9d21-470b-a05b-ce83653a9bb1)

## 📄 Project Overview

Heart disease is one of the leading causes of death worldwide. Early detection can save lives. This project builds a **machine learning model** to predict heart disease based on medical data (age, blood pressure, cholesterol, etc.), combined with **Explainable AI (XAI)** to show why the model made each prediction.

This system is designed for both **healthcare professionals** and **patients**, offering predictions along with transparent explanations using **SHAP (SHapley Additive ExPlanations)**.

---

## ✨ Key Features

✅ **Machine Learning Model**

- Voting Ensemble Classifier (SVM + XGBoost)
- Tuned for high accuracy (83.6%)
- Feature selection and hyperparameter optimization applied

✅ **Explainability with SHAP && LIME**

- Shows feature importance for each prediction
- Helps understand why the model predicted heart disease (or not)

✅ **User-Friendly Interface**

- Interactive **Streamlit** web application
- Secure login/signup system
- Simple medical form + prediction + explanation

✅ **Database Integration**

- Uses **MySQL** to store user accounts and optionally patient records
- Enables secure multi-user access and persistence

---

## 📊 Model Performance

| Metric        | Value |
| ------------- | ----- |
| **Accuracy**  | 83.6% |
| **Precision** | 78.0% |
| **Recall**    | 97.0% |
| **F1-Score**  | 86.5% |

![4](https://github.com/user-attachments/assets/7d2823f0-2b73-459b-9ac7-e1aa1c935686)

This ensures the model excels at **catching true heart disease cases** while keeping false positives reasonably low.

---

## 🧠 Training Performance (Using ANN)

This project explored Another models, including Artificial Neural Networks (ANN). Below is the **training vs validation accuracy** plot over 100 epochs when training the ANN:

![output](https://github.com/user-attachments/assets/60863bc7-f414-4511-9f77-687e8b949cbd)



The plot shows:
- **Blue Line:** Training Accuracy
- **Orange Line:** Validation Accuracy

This helps assess how well the model learned the data and whether it overfitted.

---

## 🛠️ Technologies Used

| Category           | Tools/Frameworks            |
| ------------------ | --------------------------- |
| Language           | Python 3.8+                 |
| Machine Learning   | Scikit-learn, XGBoost, SHAP |
| Data Handling      | Pandas, NumPy               |
| Visualization      | Matplotlib, Seaborn         |
| Web App            | Streamlit                   |
| Database           | MySQL                       |
| Model Persistence  | Joblib                      |
| Database Connector | mysql-connector-python      |

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-xai.git
cd heart-disease-xai
```

## 🧰 Usage

### 1️⃣ Sign Up / Login

Create an account or log in to access the prediction form.

### 2️⃣ Enter Medical Data

Fill in fields like:

- Age
- Cholesterol
- Chest pain type
- Blood pressure
- And other health indicators.

### 3️⃣ Get Prediction

The model will predict:

- Whether heart disease is likely.
- Probability of heart disease (confidence score).

### 4️⃣ Understand the Prediction

The app uses **SHAP (SHapley Additive Explanations)** to explain:

- Which features (age, cholesterol, etc.) had the greatest impact on the prediction.
- Helps doctors and patients understand **why** the prediction was made.

### 📊 Explainability Example

The SHAP summary plot shows which features impact predictions the most:

![output png3](https://github.com/user-attachments/assets/3685d193-5737-4f20-a4f5-e5ed4551884a)

![output2](https://github.com/user-attachments/assets/78c0db0f-5fee-4217-b2d4-4f74cc163fdd)

![output5](https://github.com/user-attachments/assets/7ac6f08c-2d2f-46c4-9be6-5abb61603447)

## Contributors

[Ahmed Ashraf, Abou-El-Ela](https://github.com/Ashraf1625)

[Abdelrahman Atef, Osheba](https://github.com/Abdelrahman1Osheba)

[Osama Fawzy, Adel](https://github.com/OsamaElswesy)

[Youssef Husseiny, Maaod](https://github.com/yuseiff)
