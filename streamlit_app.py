import streamlit as st
import joblib
import re

# Load the trained model and vectorizer
vectorizer, model = joblib.load("malicious_url_model.pkl")

# URL Cleaning Function
def clean_url(url):
    url = re.sub(r'https?://', '', url)
    url = re.sub(r'www\.', '', url)
    return url

# Predict Function
def predict_url(url):
    cleaned = clean_url(url)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return "🔴 Malicious" if prediction == 1 else "🟢 Safe"

# Streamlit UI
st.set_page_config(page_title="Malicious URL Detector", page_icon="🔒")

st.title("🔐 Malicious URL Detection App")
st.markdown("Check if a URL is **safe or malicious** using Machine Learning")

url_input = st.text_input("Enter a URL:", placeholder="e.g., http://freemoney.ru")

if st.button("Check URL"):
    if url_input.strip() != "":
        result = predict_url(url_input)
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter a valid URL.")
