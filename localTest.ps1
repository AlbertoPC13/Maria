# Scipt for testing the Flask app locally in a Windows environment
# Run this script in PowerShell

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
.\venv\Scripts\Activate

# Install the required packages
pip install -r requirements.txt

# Execute the Flask app
python .\app.py