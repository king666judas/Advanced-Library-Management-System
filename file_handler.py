import os
import json

LIBRARY_FILE = os.path.join(os.path.dirname(__file__), "library.json")
LEND_FILE = os.path.join(os.path.dirname(__file__), "lend_info.json")

# Function to load library from JSON file
def load_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Function to save library to JSON file
def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# # Function to load library after updating information
# def load_lend_info():
#     if os.path.exists(LEND_FILE):
#         with open(LEND_FILE, 'r') as file:
#             return json.load(file)
#     return []

# # Function to save library after updating information  
# def save_lend_info(lend_info):
#     with open(LEND_FILE, 'w') as file:
#         json.dump(lend_info, file, indent=4)