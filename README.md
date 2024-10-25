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
This project includes generate_setup_scripts.py, a Python script to automatically generate platform-specific setup scripts for Windows and Linux/macOS. It also automates the process of downloading and unzipping model files from Google Drive

```bash
git clone https://github.com/your-repo/cataract-classification.git
cd cataract-classification
```

### 2. Generate the Setup Script

```bash
python setup.py
```

This will generate a setup script for your operating system.
 - For Windows, it will generate `setup_project.bat`
 - For Linux and MacOS, it will generate `setup_project.sh`


In case above script is not working, you can manually install the dependencies using `requirements.txt` file.

### 3. Run the Generated Setup Script

Run the appropriate setup script for your operating system.

On Windows:

```bash
setup_project.bat
```

On Linux and MacOS:
```bash
setup_project.sh
```

### 4. Run the FastAPI App

```bash
uvicorn main:app --reload
```


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


### Explanation of Changes:
1. **Downloading and Unzipping Model Files**:
   - The generated setup script now includes the use of `gdown` to download model files from a Google Drive link.
   - The zip file is automatically extracted to the `./models` directory.

2. **Google Drive Link**:
   - Replace `"https://drive.google.com/drive/folders/1A71FHeX18Ag9tD-Z3yiDDuz6fGkMjGxm?usp=sharing"` with the actual link to the Google Drive folder containing the model files.

### How the Automation Works:
- **Linux/macOS**: The script uses `gdown` to download the zip file from Google Drive and then unzips it into the `./models` directory.
- **Windows**: The script uses `gdown` and `powershell` to download and unzip the file into the same directory.




