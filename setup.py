import os
import platform

SETUP_ART = r'''
      _______
     |  __   |
     | |__)  |
     |  ___/ |
     |_|     | 

   Project Setup
'''

def generate_unix_script():
    script = f'''#!/bin/bash

# Create and activate the Conda environment
conda create --name project_env python=3.8 -y
source ~/anaconda3/etc/profile.d/conda.sh || source ~/miniconda3/etc/profile.d/conda.sh
conda activate project_env

# Install requirements
pip install -r requirements.txt

# Install CLIP
pip install git+https://github.com/openai/CLIP.git

echo "Project environment setup complete!"

# Display ASCII art
cat << EOT
{SETUP_ART}
EOT

echo "To run FastAPI server, use:"
echo "    uvicorn main:app --reload"
echo "To run Streamlit frontend, use:"
echo "    streamlit run frontend.py"
'''
    with open('setup_project.sh', 'w') as f:
        f.write(script)
    os.chmod('setup_project.sh', 0o755)
    print("Generated setup_project.sh")
    print("Run './setup_project.sh' to set up the environment")

def generate_windows_script():
    script = f'''@echo off

REM Create and activate the Conda environment
call conda create --name project_env python=3.8 -y
call conda activate project_env

REM Install requirements
pip install -r requirements.txt

REM Install CLIP
pip install git+https://github.com/openai/CLIP.git

echo Project environment setup complete!

REM Display ASCII art
echo.
echo {SETUP_ART.replace('"', '^"')}
echo.

echo To run FastAPI server, use:
echo     uvicorn main:app --reload
echo To run Streamlit frontend, use:
echo     streamlit run frontend.py
pause
'''
    with open('setup_project.bat', 'w') as f:
        f.write(script)
    print("Generated setup_project.bat")
    print("Run 'setup_project.bat' to set up the environment")

if __name__ == "__main__":
    system = platform.system()
    if system == "Windows":
        generate_windows_script()
    elif system in ["Linux", "Darwin"]:
        generate_unix_script()
    else:
        print(f"Unsupported operating system: {system}")
