# import streamlit as st
# import streamlit.components.v1 as components

# def run():
#     st.set_page_config(layout="wide")
#     iframe_src = "https://levihsu-ootdiffusion.hf.space"
#     st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

# if __name__ == "__main__":
#     run()

import streamlit as st
import streamlit.components.v1 as components

def show_option1_app():
    st.title("OOTDiffusion")
    st.write("""- It offers precise outfit alignment without warping, ensuring a natural fit and realistic fabric details.
             - It is divided into two parts: 
             1. Upper Body
             2. Lower Body/Full Body""")

    # Display the "help" button on the top right corner
    if st.button("Help", key="option1_help_button", help="Show usage instructions for Option 1 app"):
        # When the "help" button is clicked, show the usage instructions directly below the button
        desc=("""
        The app has two parts:
        1. **For Upper body Try on**
        - Upload an image of a model and the garment
            (you can also select from the examples given below)
        - Hit "--> Run <--"
        2. **For Lower body/Full body Try on**
        - Upload an image of a model and the garment
            (you can also select from the examples given below)
        - Select the garment category (upper-body/lower-body/dress)
        - Hit "--> Run <--"
        """)
        st.markdown(desc)

    # Add the code for the Option 1 app here
    iframe_src = "https://levihsu-ootdiffusion.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

def show_landing_page():
    col1, col2, col3 = st.columns([2, 2, 1])
    with col1:
        # st.image("Cover.jpeg", width=800)
        # Change the font and size of the title
        st.title("Virtual Try-On")

    with col3:
        st.image("BugendaiTech LOGO.png", width=200)

    description = """
    **Imagine trying on clothes without ever leaving your home! That's the magic of virtual try-on.**

    Benefits of AI Virtual Try-On Models:
    - Convenience: Users can try on clothes from anywhere, anytime, without the need to visit a physical store.
    - Reduced Returns: By providing a more accurate idea of fit and style, virtual try-on can lead to fewer returns due to sizing or style issues.
    - Increased Sales: The engaging and interactive experience can encourage customers to explore more products and potentially make more purchases.
    - Personalization: AI models can be used to recommend clothing items that are likely to flatter a user's specific body type and preferences.
    """

    st.markdown(description)

    selected_option = st.selectbox("Select a Model", ["Select an option", "OOTDiffusion", "IDM-VTON", "OutfitAnyone"])

    if selected_option == "OOTDiffusion":
        show_option1_app()
    elif selected_option == "IDM-VTON":
        show_option2_app()
    elif selected_option == "OutfitAnyone":
        show_option3_app()

def show_option2_app():
    st.title("IDM-VTON")
    st.write("- It is an advanced virtual Try On Model, it allows you to virtually try on any clothing item, regardless of your body type or the outfit’s style.")

    # Display the "help" button on the top right corner
    # if st.button("Help", key="option2_help_button", help="Show usage instructions for IDM-VTON"):
        # When the "help" button is clicked, show the usage instructions in a modal dialog
    with st.expander("Usage instructions for IDM-VTON"):
        st.write("""
                 - Upload an Image of a model and the Garment
                    (You can also select from the examples given below)
                 - Select **Use auto-generated mask**, for Easier Auto Masking
                 - Write down the Garment Description in the space below the **Garment Image**
                 - Hit "--> **Try-On** <--
                 - The Final Output will be shown Below""")

    # Add the code for the Option 2 app here
    iframe_src = "https://yisol-idm-vton.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

def show_option3_app():
    st.title("OutfitAnyone")
    st.write("- It adapts to various body shapes and poses, ensuring natural and well-fitted clothing representations.")

    with st.expander("Usage instructions for OutfitAnyone"):
        st.write("""
                 1. Select a Model from the options available.
                 2. Upload an Image of Top Garment/Lower Garment
                    (You can also select from the examples given below)
                 3. Hit --> **Run** <--
                 """)

    # Add the code for the Option 2 app here
    iframe_src = "https://humanaigc-outfitanyone.hf.space"
    st.markdown(f'<iframe src="{iframe_src}" width="100%" height="600" frameborder="0"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    show_landing_page()