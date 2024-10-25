import streamlit as st
import requests
from PIL import Image
import io

# FastAPI endpoint
FASTAPI_URL = "http://localhost:8000/predict"  # Update if hosted on a server

st.title("Cataract Classification")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert image to bytes for FastAPI
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()
    
    # Send request to FastAPI
    with st.spinner("Predicting..."):
        response = requests.post(
            FASTAPI_URL,
            files={"file": img_bytes}
        )
    
    if response.status_code == 200:
        result = response.json()
        st.write("### Prediction")
        st.write(f"**Predicted Class**: {result['predicted_class']}")
        st.write(f"**Confidence**: {result['confidence']}%")
    else:
        st.error("Error in prediction. Please try again.")
