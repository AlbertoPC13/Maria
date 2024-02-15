# Scipt for testing the Flask app locally in a linux environment
# Run this script in bash

# Install python3-venv
sudo apt-get install python3-venv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Execute the application
python3 app.py
