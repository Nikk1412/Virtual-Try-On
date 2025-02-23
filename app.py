import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Virtual Try-On", layout="wide")

# Sidebar - Team Information
st.sidebar.title("Meet the Team")
st.sidebar.write("### Project by:")
st.sidebar.write("- **Nikhil Uday Mohite (31)**")
st.sidebar.write("- **Sanket Sunil Chougule (65)**")
st.sidebar.write("- **Pratik Sopan Gulig (68)**")
st.sidebar.write("### Under the Guidance of:")
st.sidebar.write("- **Prof. A. G. Patil**")
st.sidebar.write("- Assistant Professor, TKIET Warananagar")

# Main Page Layout
col1, col2 = st.columns([3, 1])
with col1:
    st.title("👗 Virtual Try-On App")
    st.markdown("""
    **Imagine trying on clothes without ever leaving your home!**
    - 🔥 Convenience: Try on clothes anywhere, anytime.
    - 📉 Reduced Returns: See a realistic fit before buying.
    - 🛍️ Increased Sales: More confidence in purchases.
    - 🎯 Personalization: AI-powered recommendations.
    """)

# Model Selection Tabs
st.subheader("Select a Model")
tabs = st.tabs(["OOTDiffusion", "IDM-VTON", "OutfitAnyone"])

# OOTDiffusion Model
tabs[0].title("OOTDiffusion - AI Try-On")
tabs[0].markdown("""
- Ensures precise outfit alignment without warping.
- Offers natural fit with realistic fabric details.
""")
iframe_src1 = "https://levihsu-ootdiffusion.hf.space"
tabs[0].markdown(f'<iframe src="{iframe_src1}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

# IDM-VTON Model
tabs[1].title("IDM-VTON - Advanced Try-On")
tabs[1].markdown("""
- Allows virtual try-on regardless of body type.
- AI-based automated masking for better accuracy.
""")
iframe_src2 = "https://yisol-idm-vton.hf.space"
tabs[1].markdown(f'<iframe src="{iframe_src2}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

# OutfitAnyone Model
tabs[2].title("OutfitAnyone - Smart Try-On")
tabs[2].markdown("""
- Adapts to various body shapes and poses.
- Delivers well-fitted clothing representations.
""")
iframe_src3 = "https://humanaigc-outfitanyone.hf.space"
tabs[2].markdown(f'<iframe src="{iframe_src3}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

st.success("✅ Enjoy Virtual Try-On & Explore Fashion Like Never Before!")
