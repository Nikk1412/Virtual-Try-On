# 🔥 Virtual Try-On System

## ✨ Introduction
Welcome to the **Virtual Try-On System**, an AI-powered application designed to revolutionize the online shopping experience. This project enables users to virtually try on clothing items, ensuring a perfect fit before making a purchase. It leverages advanced deep learning models to generate highly realistic outfit trials.

## 🚀 Features
- **Seamless Virtual Try-On** – Try on clothes without leaving your home!
- **AI-Powered Fit Detection** – Ensures accurate outfit alignment.
- **Interactive UI** – Designed with a sleek and modern interface using Streamlit.
- **Multiple Model Support** – Choose from **OOTDiffusion, IDM-VTON, OutfitAnyone**.
- **User-Friendly Controls** – Easy navigation and intuitive UI elements.

## 🎨 Tech Stack
- **Frontend:** Streamlit (Modern & Responsive UI)
- **Backend:** Python, Deep Learning Models
- **Frameworks:** Hugging Face Spaces, PyTorch, TensorFlow

## 👥 Team Members
- **Nikhil Uday Mohite** (Roll No. 31)
- **Sanket Sunil Chougule** (Roll No. 65)
- **Pratik Sopan Gulig** (Roll No. 68)

### 🎓 Under the Guidance of
**Prof. A. G. Patil**  
Assistant Professor, SWSVS,  
Tatyasaheb Kore Institute of Engineering and Technology,  
Warananagar (An Autonomous Institute)

## 🛠️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/virtual-tryon.git
   cd virtual-tryon
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 🖼️ Virtual Try-On Architecture

Below is the architecture diagram showcasing how OOTDiffusion, IDM-VTON, and OutfitAnyone process image data to generate virtual try-on results.

![Architecture Diagram](Image1.png)

### 🏗️ How It Works (Simple Explanation)
1. **Input Image:** The user uploads a photo of themselves and a clothing image.
2. **Preprocessing:** The system aligns the person’s body shape with the outfit.
3. **Model Processing:**
   - **OOTDiffusion**: Uses diffusion models for ultra-realistic clothing synthesis.
   - **IDM-VTON**: Focuses on high-accuracy garment warping.
   - **OutfitAnyone**: Ensures compatibility for different body types.
4. **Output Image:** The system generates a realistic try-on image where the clothing fits naturally on the user’s body.

### 📌 Example:
Imagine you want to try on a **blue jacket**:
- You upload your **photo** and an image of the **blue jacket**.
- The system processes the images and adjusts the jacket to fit your **body shape**.
- You receive a final image where you **see yourself wearing the blue jacket**.

## 📸 Screenshots
<img src="demo_screenshot.png" width="600" alt="Virtual Try-On Screenshot">

## 🤝 Contributing
We welcome contributions! Feel free to submit issues and pull requests to improve this project.

## 📜 License
This project is licensed under the **MIT License**.

## 📢 Acknowledgements
- Hugging Face for hosting ML models.
- Our mentor **Prof. A. G. Patil** for valuable guidance.
- The amazing open-source community!

---
✨ **Experience the future of fashion with Virtual Try-On!** ✨
