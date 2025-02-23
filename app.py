import streamlit as st
import requests
from PIL import Image
import io

# Set page title and favicon
st.set_page_config(page_title="Virtual Try-On", page_icon="👕", layout="wide")

# Load College Logo
college_logo = "TKIET logo.png"
st.sidebar.image(college_logo, use_column_width=True)

# Header Section
st.markdown(
    """
    <h1 style='text-align: center; color: #ff5733;'>🔥 Virtual Try-On System 🔥</h1>
    <p style='text-align: center; color: #555;'>Experience AI-powered outfit trials with a sleek modern UI!</p>
    """, unsafe_allow_html=True
)

# Upload Image Section
st.markdown("## Upload Your Photo")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"], help="Upload a front-facing image for the best results.")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded Image", use_column_width=True)
    
    # Select Clothing Model
    model_option = st.selectbox("Select a Virtual Try-On Model:", ["OOTDiffusion", "IDM-VTON", "OutfitAnyone"], index=0)
    st.write(f"You selected: **{model_option}**")
    
    # Process Image Button
    if st.button("Try On Now!", key="process"):
        st.success("Processing your virtual try-on request... 🕒")
        # Placeholder for ML API request
        st.image(image, caption="[Generated Try-On Preview]", use_column_width=True)

# Footer Section
st.markdown(
    """
    ---
    <div style='text-align: center;'>
        <p>Developed by <b>Team Virtual Try-On</b></p>
        <p><i>Under the guidance of Prof. A. G. Patil</i></p>
    </div>
    """, unsafe_allow_html=True
)
