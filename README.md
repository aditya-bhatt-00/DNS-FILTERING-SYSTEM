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

---

## ⚙️ Data Preprocessing

- Combined all four CSVs into a single DataFrame
- Dropped irrelevant columns
- Applied Label Encoding on target variable
- **Train-Test Split**: 80% Training | 20% Testing

---

## 🧠 Model Experimentation Journey

| Model                | Description                                   | Accuracy   |
|---------------------|-----------------------------------------------|------------|
| Random Forest        | Baseline model                                | 15% (0.15) |
| XGBoost              | Boosted tree classifier                       | **93% (0.93)** |
| MLP + SMOTE          | Applied SMOTE oversampling                    | 15% (0.15) |
| Stacking Classifier  | Ensemble of top-performing models             | **93% (0.93)** |

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
