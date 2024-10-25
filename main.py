from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
import torch
import torch.nn as nn
import clip
from torchvision import transforms
import uvicorn
from typing import Dict
import numpy as np

app = FastAPI()

# Model definition
class CataractClassifier(nn.Module):
    def __init__(self, clip_model):
        super().__init__()
        self.clip_model = clip_model
        self.classifier = nn.Sequential(
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 2)
        )
        
    def forward(self, x):
        with torch.no_grad():
            features = self.clip_model.encode_image(x)
            features = features.float()
        return self.classifier(features)

# Global variables
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = None
preprocess = None

@app.on_event("startup")
async def load_model():
    global model, preprocess
    print("Loading model...")
    
    # Load CLIP model
    clip_model, preprocess = clip.load("RN50", device=device)
    
    # Initialize model
    model = CataractClassifier(clip_model).to(device)
    
    # Load trained weights (using the quantized version for efficiency)
    model_path = r"E:\jivi-ai\results\run_20241025_160239\best_model.pth"  # Update path
    checkpoint = torch.load(model_path, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    print("Model loaded successfully!")

@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> Dict:
    # Read and preprocess image
    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    
    # Preprocess and predict
    image_tensor = preprocess(image).unsqueeze(0).to(device)
    
    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.softmax(outputs, dim=1)
        prediction = torch.argmax(outputs, dim=1)
        confidence = round(probabilities[0][prediction.item()].item() * 100, 2)
    
    return {
        "predicted_class": "Cataract" if prediction.item() == 1 else "Non-Cataract",
        "confidence": confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)