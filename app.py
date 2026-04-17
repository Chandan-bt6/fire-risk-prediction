import streamlit as st
import pandas as pd
import numpy as np
import joblib

import requests

st.set_page_config(page_title="Himalayan FireGuard", page_icon="🔥")

# ---------- Load model ----------
@st.cache_resource
def load_model():
    return joblib.load("fire_risk_model.pkl")

try:
    model = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"Model load error: {e}\nPlease train & save model as fire_risk_model.pkl")

st.title("🔥 Himalayan FireGuard — Forest Fire Risk Predictor")

st.markdown("Enter weather/vegetation values and get **risk = Low / Medium / High**.")

def predict_risk(_temp, _hum, _wind, _rain, _ndvi):
    X = pd.DataFrame([{
        "temp": _temp,
        "humidity": _hum,
        "wind": _wind,
        "rainfall": _rain,
        "ndvi": _ndvi
    }])
    return model.predict(X)[0]

def send_sms_simulated(risk):
    """Fake demo SMS (no cost)"""
    if risk == "High":
        print("🚨 SMS Sent: HIGH fire risk! Evacuate immediately!")
    else:
        print("✅ No SMS needed.")

"""actual sms(using api)"""

def send_sms_real(message, numbers):
    
    url = "https://www.fast2sms.com/dev/bulkV2"
    
    payload = {
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': numbers
    }
    headers = {
        'authorization': "Tw3NZfoYm6BzqkIdvhiayrD9LC1GjWKXHlegcFEu0xPM28bVO4Ru7hrQokEX9vDzg5ifsIU3xmcyWVKJ",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()


# ---------- Inputs ----------
col1, col2, col3 = st.columns(3)
with col1:
    temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=30.0, step=0.5)
    wind = st.number_input("Wind Speed", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
with col2:
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=40.0, step=1.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=2.0, step=0.5)
with col3:
    ndvi = st.number_input("NDVI (0–1)", min_value=0.0, max_value=1.0, value=0.45, step=0.01)

# ---------- Predict ----------
# ---------- Predict ----------
st.markdown("---")

st.info("Fill values and click Predict to see fire risk 🔥")  # 👈 ADD HERE

phone = st.text_input("Enter phone number (with country code: 91XXXXXXXXXX)")
btn = st.button("🔮 Predict Risk", use_container_width=True, type="primary")
if btn:
    if not model_loaded:
        st.warning("Model not loaded. Train & save as fire_risk_model.pkl first.")
    else:
        risk = predict_risk(temp, humidity, wind, rainfall, ndvi)

        emoji = {"Low":"🟢", "Medium":"🟡", "High":"🔴"}
        st.subheader(f"Risk: {emoji.get(risk,'❓')} **{risk}**")

        # Helpful context text
        if risk == "High":
            st.error("High risk detected. Trigger siren/LED + prepare alert message.")
            
            if phone:
                resp = send_sms_real("🔥 HIGH FIRE RISK!", phone)
                st.success("✅ SMS sent!")
                st.write(resp)   # Optional: Show API response
            else:
                st.warning("⚠️ Please enter a valid phone number")

        elif risk == "Medium":
            st.warning("Medium risk. Keep monitoring and prepare resources.")
        else:
            st.success("Low risk. Normal conditions.")

        # Show the exact input back to user
        with st.expander("See input details"):
            st.write({
                "temp": temp, "humidity": humidity, "wind": wind,
                "rainfall": rainfall, "ndvi": ndvi
            })


"""simulated sms demo"""
st.caption("Tip: Next step we’ll connect this to hardware (LED/siren) & SMS alert.")

def send_sms_simulated(risk):
   if risk == "High":
    st.error("High risk detected. 🚨 SMS Sent to authorities!")
   elif risk == "Medium":
        st.warning("Medium risk — monitor situation.")
   else:
        st.success("Low risk — normal conditions.")


