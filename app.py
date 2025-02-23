import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

def main():
    st.set_page_config(page_title="Virtual Try-On", layout="wide")
    
    # Sidebar for navigation
    st.sidebar.image("TKIET logo.png", width=200)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "OOTDiffusion", "IDM-VTON", "OutfitAnyone"])
    
    if page == "Home":
        show_home()
    elif page == "OOTDiffusion":
        show_option1_app()
    elif page == "IDM-VTON":
        show_option2_app()
    elif page == "OutfitAnyone":
        show_option3_app()

def show_home():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("👕 Virtual Try-On System")
        st.subheader("A Smart AI-Powered Outfit Try-On Experience")
        
        st.markdown(
            """
            **Imagine trying on clothes without ever leaving your home! That's the magic of Virtual Try-On.**
            
            **Benefits of AI Virtual Try-On Models:**
            - 🚀 **Convenience**: Try on clothes from anywhere, anytime.
            - 📉 **Reduced Returns**: Get accurate fit and style recommendations.
            - 📈 **Increased Sales**: Engage customers with an interactive experience.
            - 🤖 **Personalization**: AI models suggest outfits based on your body type.
            """, unsafe_allow_html=True)
    
    with col2:
      #  image = Image.open("TKIET logo.png")  # Replace with actual cover image
        st.image(image, use_column_width=True)
    
    # Group Details
    st.markdown("---")
    st.subheader("👨‍💻 Project Group Details")
    st.markdown(
        """
        **Team Members:**  
        - 🎓 **Nikhil Uday Mohite** (Roll No: 31)  
        - 🎓 **Sanket Sunil Chougule** (Roll No: 65)  
        - 🎓 **Pratik Sopan Gulig** (Roll No: 68)  
        
        **Degree:** Bachelor of Technology in Computer Science & Engineering  
        **Under the Guidance of:** Prof. A. G. Patil (Assistant Professor, SWSVS, TKIET, Warananagar)
        
        **Academic Year:** 2024-25
        """, unsafe_allow_html=True)
    
    st.markdown("---")

def show_option1_app():
    st.title("👗 OOTDiffusion - AI Outfit Try-On")
    st.write("""OOTDiffusion ensures precise outfit alignment without warping, ensuring a natural fit.
             - **It has two parts:**
             1. Upper Body
             2. Lower Body/Full Body""")
    
    with st.expander("ℹ️ How to Use OOTDiffusion"):
        st.markdown(
            """
            1. Upload an image of a model and the garment
            2. Select the garment category (upper-body/lower-body/dress)
            3. Click on **Run** to process the image
            4. View the result below!
            """, unsafe_allow_html=True)
    
    iframe_src = "https://levihsu-ootdiffusion.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

def show_option2_app():
    st.title("👕 IDM-VTON - Advanced Try-On")
    st.write("""An advanced AI Virtual Try-On system that allows anyone to visualize clothing effortlessly.
             
             - **Supports diverse body types and clothing styles**
             - **Realistic fitting adjustments**
             """)
    
    with st.expander("ℹ️ How to Use IDM-VTON"):
        st.markdown(
            """
            1. Upload an image of a model and the garment
            2. Enable **Auto Masking** for easy segmentation
            3. Enter garment description (optional)
            4. Click on **Try-On**
            """, unsafe_allow_html=True)
    
    iframe_src = "https://yisol-idm-vton.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

def show_option3_app():
    st.title("👗 OutfitAnyone - AI-Powered Fashion Fit")
    st.write("""OutfitAnyone is designed to adapt to different body shapes, ensuring a natural clothing fit.
             
             - **Handles diverse poses and angles**
             - **AI-assisted clothing adaptation for better visualization**
             """)
    
    with st.expander("ℹ️ How to Use OutfitAnyone"):
        st.markdown(
            """
            1. Select a Model from the available options.
            2. Upload an Image of Top Garment/Lower Garment
            3. Click **Run** to see the results
            """, unsafe_allow_html=True)
    
    iframe_src = "https://humanaigc-outfitanyone.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
