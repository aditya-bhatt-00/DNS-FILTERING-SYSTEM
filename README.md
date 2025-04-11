# DNS-FILTERING-SYSTEM
We made that possible—thanks to powerful ML models, real-time visualizations, and a clean UI. Trained on CIC-BELL-DNS-2021, our tool goes beyond theory and lands straight into action. 93% accuracy, zero guesswork.

# DNS Malware Detection using Ensemble Learning

A smart cybersecurity solution to detect **malicious network traffic** using **ML-powered classification** on the CIC-BELL-DNS-2021 dataset. Our model analyzes DNS records to classify traffic into **Benign, Malware, Phishing, or Spam**, and presents real-time predictions with an interactive UI and dynamic visualizations.

---

## 🚀 Motivation

With cyber threats becoming increasingly sophisticated, DNS remains a vulnerable vector for attackers. We aim to create an intelligent, accurate, and user-friendly detection system to flag and analyze potential DNS-based threats—turning raw logs into powerful cybersecurity insights.

---

## 📁 Dataset

**Source**: CIC-BELL-DNS-2021  
- Format: CSV  
- Files: `benign.csv`, `malware.csv`, `phishing.csv`, `spam.csv`

These were merged into a unified dataset with labeled entries for ML processing.
![image](https://github.com/user-attachments/assets/86c55a27-5ebb-4bf2-b881-9a2a94843939)


---

## ⚙️ Data Preprocessing

- Combined all four CSVs into a single DataFrame
- Dropped irrelevant columns
- Applied Label Encoding on target variable
- **Train-Test Split**: 80% Training | 20% Testing
- ![image](https://github.com/user-attachments/assets/05c37874-8005-4163-ad68-c29af75d1b8b)

---

## 🧠 Model Experimentation Journey

| Model                | Description                                   | Accuracy   |
|---------------------|-----------------------------------------------|------------|
| Random Forest        | Baseline model                                | 15% (0.15) |
| XGBoost              | Boosted tree classifier                       | **93% (0.93)** |
| MLP + SMOTE          | Applied SMOTE oversampling                    | 15% (0.15) |
| Stacking Classifier  | Ensemble of top-performing models             | **93% (0.93)** |

![image](https://github.com/user-attachments/assets/a58e4f51-b7cd-4b93-a11e-e9534cc768c8)
![image](https://github.com/user-attachments/assets/c98e69c7-3c42-4f22-80ae-c85dbde7905f)
![image](https://github.com/user-attachments/assets/61c92caf-e869-495e-a99d-5289d49a9edf)
![image](https://github.com/user-attachments/assets/09a897a0-2599-4c2e-9199-7830861918c7)
![image](https://github.com/user-attachments/assets/beecdd0b-e428-42dd-a611-c1b6ac2ba7c0)
![image](https://github.com/user-attachments/assets/1dedbc88-cac7-4307-8ac6-7f28e0d6fb73)
![image](https://github.com/user-attachments/assets/6e455531-948d-4a16-9f75-3a628c89cd69)

After experimenting with several models and balancing techniques, **XGBoost** and **Stacking** emerged as top performers.

---

## 🖥️ User Interface (Frontend)

- Built a clean and interactive UI
- Accepts file uploads (CSV, PDF, etc.)
- Provides analysis and classification
- Outputs include:
  - Threat category (Malware, Phishing, etc.)
  - Real-time visualizations (Pie Chart, Bar Graphs, etc.)

---

## 📊 Visual Insights

We’ve integrated powerful visualization tools to:
- Show category-wise distribution
- Represent prediction probabilities
- Detect anomalies instantly

---

## 🧩 Tech Stack

- Python (Pandas, Scikit-learn, XGBoost, SMOTE)
- Streamlit (for UI)
- Matplotlib / Seaborn (Visualizations)
- GitHub (Version control & deployment)
