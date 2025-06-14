# 🔐 Malicious URL Detection using Machine Learning

This project is a simple and effective Streamlit web app that detects whether a given URL is **malicious** or **safe** using a machine learning model trained on a real-world dataset.

---

## 🚀 Live Demo

[Click here to use the app]([https://your-streamlit-link.streamlit.app](https://malicious-url-app-ersjjlm8vdzuc4rtvbvtcb.streamlit.app/))  
(*Replace with your actual Streamlit Cloud URL after deployment*)

---

## 🧠 What This Project Does

- Accepts a URL input
- Cleans and preprocesses the URL
- Uses a trained machine learning model to classify the URL as:
  - ✅ Safe
  - ❌ Malicious
- Displays prediction result in real-time

---

## 📦 Files Included

- `streamlit_app.py` – Streamlit web app script
- `malicious_url_model.pkl` – Trained ML model (Logistic Regression or similar)
- `vectorizer.pkl` – Fitted TF-IDF vectorizer
- `requirements.txt` – Python packages for deployment

---

## 📊 Dataset Used

- Dataset: [`malicious_phish.csv`](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- Features: URL strings and their label (`good` or `bad`)
- Preprocessing includes lowercasing, removing protocols/domains, and vectorizing with TF-IDF

---

## 💻 How to Run Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/your-username/malicious-url-app.git
   cd malicious-url-app

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run streamlit_app.py

🌐 How to Deploy on Streamlit Cloud
Push all 4 files (streamlit_app.py, model.pkl, vectorizer.pkl, requirements.txt) to your GitHub repo

Go to https://streamlit.io/cloud

Sign in with GitHub, select the repo, and deploy it — that's it!

 Developed By
Abhinay Dasi
Cybersecurity & AI/ML Enthusiast
📧 abhinaydasi5983@gmail.com
