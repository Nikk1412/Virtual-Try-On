import streamlit as st
import streamlit.components.v1 as components

# Set wide layout
st.set_page_config(page_title="Virtual Try-On", layout="wide")

# College and project details
COLLEGE_NAME = "Tatyasaheb Kore Institute of Engineering and Technology, Warananagar"
DEPARTMENT = "Department of Computer Science & Engineering"
GUIDE_NAME = "Prof. A. G. Patil (Assistant Professor, SWSVS)"
STUDENT_INFO = [
    {"name": "Nikhil Uday Mohite", "roll_no": "31"},
    {"name": "Sanket Sunil Chougule", "roll_no": "65"},
    {"name": "Pratik Sopan Gulig", "roll_no": "68"},
]

# --- HEADER SECTION ---
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    st.image("TKIET logo.png", width=100)  # Replace with actual logo
    st.title("👗 Virtual Try-On System")
    st.subheader("AI-Powered Clothing Try-On Experience")

with col3:
    st.image("name-png-logo-nik-creation-nikhil-creations.png", width=150)

st.markdown(f"**📚 {COLLEGE_NAME}**  \n🎓 *{DEPARTMENT}*  \n👨‍🏫 *Under the Guidance of {GUIDE_NAME}*")

# Display Student Details
st.markdown("### 👨‍💻 **Project Team**")
for student in STUDENT_INFO:
    st.write(f"✅ **{student['name']}** (Roll No: {student['roll_no']})")

st.divider()  # Add a visual separator

# --- PROJECT DESCRIPTION ---
st.markdown("## ✨ **What is Virtual Try-On?**")
st.write("""
Imagine trying on clothes without ever leaving your home! Our AI-powered Virtual Try-On System lets users experience a **realistic outfit trial**, helping them make better shopping decisions.
""")

st.markdown("### 🌟 **Why Use Virtual Try-On?**")
st.markdown("""
- 🚀 **Seamless Shopping Experience** – Try before you buy!
- 🤖 **AI-Powered Fit Detection** – Ensures accurate outfit alignment.
- 💡 **Personalized Recommendations** – Helps choose the perfect outfit.
- 📉 **Reduces Return Rates** – Enhances customer satisfaction.
""")

st.divider()

# --- MODEL SELECTION ---
st.markdown("## 🔥 **Choose Your Virtual Try-On Model**")
selected_option = st.radio("Pick a Try-On Model:", ["OOTDiffusion", "IDM-VTON", "OutfitAnyone"])

# --- MODEL SECTIONS ---
def show_ootdiffusion():
    st.subheader("👕 **OOTDiffusion - AI-Powered Virtual Try-On**")
    st.write("""
    - Offers **precise outfit alignment** without warping, ensuring natural fit and fabric details.
    - Supports **Upper Body & Full Body Try-On**.
    """)
    
    with st.expander("💡 **How to Use?**"):
        st.markdown("""
        1️⃣ Upload an image of the **model & garment**.  
        2️⃣ Select **Upper Body / Full Body** try-on mode.  
        3️⃣ Hit **"Run"** and get the results instantly!
        """)
    
    iframe_src = "https://levihsu-ootdiffusion.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

def show_idm_vton():
    st.subheader("🧥 **IDM-VTON - Advanced Virtual Try-On**")
    st.write("""
    - Adapts to various body types & clothing styles.
    - Uses **Auto-Masking & AI Fit Detection** for realistic try-on.
    """)

    with st.expander("💡 **How to Use?**"):
        st.markdown("""
        1️⃣ Upload a **model image & garment image**.  
        2️⃣ Enable **Auto-Mask** for better accuracy.  
        3️⃣ Write **Garment Description** (optional).  
        4️⃣ Click **"Try-On"** to see the results!
        """)

    iframe_src = "https://yisol-idm-vton.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

def show_outfitanyone():
    st.subheader("👗 **OutfitAnyone - AI Fashion for Everyone**")
    st.write("""
    - Works for **all body shapes & poses**.
    - Ensures a **natural & well-fitted clothing experience**.
    """)

    with st.expander("💡 **How to Use?**"):
        st.markdown("""
        1️⃣ Choose a **Top/Lower Garment** model.  
        2️⃣ Upload an **image** (or pick from samples).  
        3️⃣ Click **"Run"** to see your virtual outfit!
        """)

    iframe_src = "https://humanaigc-outfitanyone.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600"></iframe>', unsafe_allow_html=True)

# Show the selected model
if selected_option == "OOTDiffusion":
    show_ootdiffusion()
elif selected_option == "IDM-VTON":
    show_idm_vton()
elif selected_option == "OutfitAnyone":
    show_outfitanyone()

st.divider()

# --- FOOTER SECTION ---
st.markdown("""
---
👨‍🏫 **Project Guide:** *Prof. A. G. Patil*  
🎓 **Academic Year:** 2024-25  
📍 *Tatyasaheb Kore Institute of Engineering and Technology, Warananagar*  
""")
