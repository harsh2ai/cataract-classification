# Cataract Classification System

This repository implements a deep learning-based cataract classification system using FastAPI and Streamlit. The system utilizes a custom neural network built on top of CLIP for image feature extraction and a custom classifier to predict cataract and non-cataract images.

## Directory Structure
```
cataract-classification/
    │
    ├── augmentatioin.ipynb          # Notebook for image augmentation techniques
    ├── EDA.ipynb                    # Exploratory Data Analysis notebook
    ├── LICENSE                      # License information
    ├── Readme.md                    # This README file
    ├── requirements.txt             # Python dependencies
    ├── main.py                      # FastAPI app for inference
    └── frontend.py                  # Streamlit app for frontend 
```

## How to Use

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/cataract-classification.git
cd cataract-classification
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI App

```bash
uvicorn main:app --reload
```

### 4. Run the Streamlit Frontend

In a new terminal window, navigate to the project directory and run:

```bash
streamlit run frontend.py
```

This will start the Streamlit app, allowing you to interact with the cataract classification system through a web interface.


### 5. Making Predictions

Once both the FastAPI backend and Streamlit frontend are running, you can make predictions as follows:

1. Open your web browser and navigate to the Streamlit app (usually at `http://localhost:8501`).
2. You'll see an interface with an option to upload an image.
3. Click on "Upload an Image" and select a fundus image (supported formats: jpg, jpeg, png).
4. Once uploaded, the image will be displayed on the page.
5. The system will automatically send the image to the FastAPI backend for prediction.
6. After a brief moment, you'll see the prediction result, including:
   - The predicted class (Cataract or Non-Cataract)
   - The confidence level of the prediction (as a percentage)

If you encounter any errors during prediction, make sure both the FastAPI and Streamlit apps are running correctly and try uploading the image again.


## API Reference

The FastAPI backend automatically generates API documentation. You can access these interactive API docs using the following URLs:

### Swagger UI

For an interactive API documentation interface, visit: `http://localhost:8000/docs`

### ReDoc

For a more detailed documentation, visit: `http://localhost:8000/redoc`





