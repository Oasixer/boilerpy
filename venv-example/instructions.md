# First time
python3 -m venv venv

## gitignore
just add venv dir to gitignore

# Activate
## Linux
source venv/bin/activate

## Windows
venv/Scripts/activate

# Deactivate
deactivate

# Update requirements to txt file
pip freeze > requirements.txt

# Load requirements from txt file
pip install -r requirements.txt

