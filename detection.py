from deepface import DeepFace
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Define paths
img2_path = "/Users/leopold/customer_detection/img2.jpg"
db_path = "/Users/leopold/customer_detection/database"

# Specify the model to use and the threshold
model_name = 'ArcFace'
distance_metric = 'cosine'
threshold = 0.6  # Adjust this value to experiment with different thresholds

# Perform the search for img2
logging.debug(f"Searching for {img2_path} in {db_path} using model {model_name}")

try:
    results2 = DeepFace.find(img_path=img2_path, db_path=db_path, model_name=model_name)
    
    # Check if results2 is a list and iterate through the DataFrames
    if isinstance(results2, list):
        for idx, df in enumerate(results2):
            # Extract and print the folder names
            df['folder_name'] = df['identity'].apply(lambda x: x.split('/')[-2])
            folder_names = df['folder_name'].unique()
            for folder_name in folder_names:
                print(folder_name)
    else:
        # Extract and print the folder names
        results2['folder_name'] = results2['identity'].apply(lambda x: x.split('/')[-2])
        folder_names = results2['folder_name'].unique()
        for folder_name in folder_names:
            print(folder_name)

except Exception as e:
    logging.error(f"An error occurred during the search: {e}")
