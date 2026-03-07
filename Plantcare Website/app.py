print("Starting up... Loading TensorFlow (this might take a minute!)...")
import os
import json
import numpy as np
from PIL import Image
from flask import Flask, request, render_template, redirect, url_for
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'avif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MODEL_PATH = 'model/plant_disease_recog_model_pwp.keras'
JSON_PATH = 'model/class_indices.json'

try:
    model = load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

try:
    with open(JSON_PATH, 'r') as f:
        class_indices = json.load(f)
    class_names = {int(v): k for k, v in class_indices.items()}
    print("Class indices loaded.")
except Exception as e:
    print(f"Error loading class indices: {e}")
    class_names = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_image(image_path):
    img = Image.open(image_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize((224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    img_array = img_array / 255.0 
    return img_array

def parse_prediction(class_name):
    parts = class_name.split("___")
    plant_type = parts[0].replace("_", " ")
    condition = parts[1].replace("_", " ") if len(parts) > 1 else "Unknown"
    return plant_type, condition

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
       
        if model is None:
            return "CRITICAL ERROR: The AI model failed to load in the background."

       
        if 'file' not in request.files:
            return "ERROR: The server received the request, but the file was missing."
        
        file = request.files['file']
        
       
        if file.filename == '':
            return "ERROR: You clicked Analyze but didn't select an image."

   
        if not allowed_file(file.filename):
            return f"ERROR: Invalid file type. You uploaded '{file.filename}'. Allowed types are: {ALLOWED_EXTENSIONS}"

       
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            processed_img = process_image(filepath)
            predictions = model.predict(processed_img)
            
            confidence = float(np.max(predictions[0])) * 100
            
            if confidence < 65.0:
                return render_template(
                    "result.html",
                    plant_type="Unrecognized Image",
                    condition="Not a Plant / Invalid Photo",
                    confidence=f"{confidence:.2f}% (Too Low)",
                    is_healthy=False,
                    image_filename=filename
                )

            predicted_class_index = np.argmax(predictions[0])
            predicted_class_name = class_names[predicted_class_index]
            
            plant_type, condition = parse_prediction(predicted_class_name)
            is_healthy = 'healthy' in condition.lower()

            return render_template(
                "result.html",
                plant_type=plant_type,
                condition=condition,
                confidence=f"{confidence:.2f}%",
                confidence_width=f"{confidence:.2f}%",
                is_healthy=is_healthy,
                image_filename=filename
            )
        except Exception as e:
            return f"ERROR DURING AI PREDICTION: {str(e)}"
            
    
    return redirect(url_for('upload'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

