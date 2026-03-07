
# 🌿 PlantCare AI – Plant Disease Classification using Transfer Learning


## Introduction
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%3E%3D2.17.0-orange.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.2-lightgrey.svg)


PlantCare AI is a deep learning-based project designed to automatically detect and classify plant diseases from leaf images. Plant diseases significantly affect crop productivity, and early detection is essential for preventing large-scale agricultural losses. Traditional disease identification methods rely on manual inspection by experts, which can be time-consuming and sometimes inaccurate.

This project uses transfer learning with the MobileNetV2 Convolutional Neural Network (CNN) to build an efficient and accurate plant disease classification model. The model is trained on the New Plant Diseases Dataset, which contains 87,000+ labeled plant leaf images across 38 different classes, including healthy and diseased leaves from crops such as Apple, Corn, Grape, Potato, and Tomato.

## 🚀 Key Features
Real-time Image Classification: Upload leaf images and get instant diagnostic results.

Persistent Image Display: The UI "remembers" your uploaded image on the result page using unique filename logic.

Dual View Optimization: Fully responsive layout for both Desktop (camera-enabled) and Mobile (home-focused) use.

Confidence Scoring: Provides an AI confidence percentage for every diagnosis.

## 🚀 Dataset

Source: New Plant Diseases Dataset (Kaggle) via SkillWallet.

Scale: 87,000+ augmented RGB images.

Diversity: 38 classes covering 14 different plant species (Apple, Tomato, Corn, etc.).

Format: JPEG images originally 256×256 pixels.

## Model Architecture

Base Model: MobileNetV2 (using Transfer Learning).

Input Shape: 224×224×3 (RGB).

Optimizer: Adam with categorical cross-entropy loss.

Accuracy: Achieved ~93.6% validation accuracy.

## ⚙️ System Architecture
![PlantCare AI System](Plantcare%20Website/static/Photos/system.png)

## 📱 Screenshots & Demo
### Desktop View

### Home Page: Introduction and navigation to the diagnostic tool.
![PlantCare AI Home](Plantcare%20Website/static/Photos/PlantCareAI_Home.jpeg)

### Upload Page: Features a file selector and camera integration for live leaf captures.
![PlantCare AI Upload](Plantcare%20Website/static/Photos/PlantCareAI_Upload.jpeg)

### Result Page: Displays the processed image (224x224), the AI confidence score, and recommended actions required for the specific plant/disease diagnosis.
![PlantCare AI Result](Plantcare%20Website/static/Photos/PlantCareAI_Result.jpeg)

### Mobile View
### Home Page: A streamlined, responsive version of the site for on-the-go farming diagnostics.

![PlantCare AI Mobile View](Plantcare%20Website/static/Photos/PlantCareAI_MobileView.jpeg)

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PlantCare-AI.git
cd "Plantcare Website"
```
### 2. Environment Setup (Recommended: Python 3.11)
```bash
conda create -n plantcare python=3.11 -y
conda activate plantcare
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
python app.py
```
 Access the site at: http://127.0.0.1:5000

 Our Link :
```bash
https://sayan04-plantcare-web.hf.space/
```
 
 ## 📁 Project Structure

```
├── model/
│   ├── class_indices.json       # Maps AI output indices to disease names
│   └── plant_disease_recog.keras # Pre-trained Keras model
├── static/
│   ├── style.css                # Global styles, variables, and animations
│   ├── Photos/                  # UI assets and logos
│   └── uploads/                 # Temporary storage for analyzed images
├── templates/
│   ├── base.html                # Master layout, Nav, and Footer
│   ├── home.html                # Landing page
│   ├── about.html               # Technology and Mission details
│   ├── upload.html              # Drag-and-drop & Webcam interface
│   └── result.html              # Dynamic diagnosis and recommendation page
├── app.py                       # Flask application and routing logic
├── requirements.txt             # Python dependencies
└── .gitignore                   # Ignored files and cache
```

## 📊 Results
The *PlantCare AI* result page provides a comprehensive breakdown of the AI's analysis:

**Visual Confirmation**: Displays the uploaded leaf image directly on the results dashboard for immediate verification.

**Target Crop Identification:** Correctly identifies the plant species (e.g., Tomato).

**Disease Diagnosis:** Provides the specific detected condition (e.g., Early blight).

**AI Confidence Meter:** A visual progress bar showing the model's certainty (e.g., 91.66%).

**Actionable Insights:** Includes a Recommended Actions section to guide users on pruning, fungicide application, and proper watering techniques.

## 🛠 Technologies Used
### Core Artificial Intelligence
**TensorFlow 2.17.0:** The primary deep learning framework used to load and run the MobileNetV2 model.

**Keras:** Used for high-level neural network API implementation and handling the .keras model format.

**MobileNetV2:** A lightweight, efficient CNN architecture utilized via Transfer Learning for fast image classification.
### Backend Development
**Python 3.11:** The programming language powering the entire backend logic.

**Flask 3.0.2:** A micro-web framework used to create the server, handle routing, and manage user sessions.

### Data & Image Processing
**NumPy:** Used for high-performance multidimensional array processing, specifically for converting images into tensors for the model.

### Frontend & UI/UX
* **HTML5** : For the responsive styling of the web interface.

* **CSS3**: For the responsive styling of the web interface.

* **Vanilla JavaScript (Webcam API, DOM manipulation)**
* **FontAwesome (Icons)**

### ☁️ Development & Deployment Platform
**Google Colab:** Used for training the deep learning model with GPU support and handling large datasets efficiently.

**Hugging Face.com:** Used to deploy and host the Flask web application for online access.

###  Environment & Version Control
**Anaconda/Conda:** Used for environment management to ensure library version compatibility.

**Git & GitHub:** For version control and project documentation.

## Conclusion:
PlantCare AI successfully demonstrates the power of transfer learning in agriculture, providing a high-accuracy, real-time diagnostic tool. By utilizing the MobileNetV2 architecture, we created a system that is lightweight enough for web deployment while remaining robust enough to handle 38 different plant categories.

## Future Scope:
Offline Mode: Implementing PWA features for use in remote fields without internet.

Treatment Database: Adding automated care suggestions based on the specific disease detected.

IoT Integration: Connecting the model to field sensors for automated health monitoring.

## 🏆 Acknowledgements
**SkillWallet:** For the guided learning path and technical project support.

**Kaggle:** For providing the New Plant Diseases Dataset.

*Images:* 87,000+ RGB images.

*Classes:* 38 (Healthy and Diseased categories).

*Specifications:* Images originally 256×256 pixels, resized to 224×224 for MobileNetV2 compatibility.

## 👥 Authors / Contributors

This project is **jointly developed** by **SAYAN PAUL** and **SAYANDIP DEY**.  
We worked together on Machine Learning, Backend, Frontend, and Deployment aspects of the project.  

| Contributor | Role | GitHub | LinkedIn |
|-------------|------|--------|----------|
| **SAYAN PAUL** | ML, Frontend Development , Backend Integration & Deployment | [![GitHub](https://img.shields.io/badge/GitHub-OctoEcho-181717?logo=github&logoColor=white)](https://github.com/OctoEcho) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-SayanPaul-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sayan-paul-83a99a267/) |
| **SAYANDIP DEY** | ML Model Development & Training, Backend DEvelopment,  API Integration | [![GitHub](https://img.shields.io/badge/GitHub-Sayandipdey-181717?logo=github&logoColor=white)](https://github.com/Sayandipdey) | [![LinkedIn](https://img.shields.io/badge/LinkedIn-SayandipDey-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sayandip-dey-063693298/) |

Also team Members **SHANTANU MONDAL** & **RAJASHREE DUTTA**
