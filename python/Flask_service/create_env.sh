# Create environemnt
python -m venv env

# Activate virtual environment
source env/bin/activate

# Install requirements
pip install -r requirements.txt

# Save requirements
pip freeze > requirements.txt