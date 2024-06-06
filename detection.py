from deepface import DeepFace
import os
import logging

# Define paths
img2_path = #variable path 
db_path = #variable path, figure out how to get access to azure database

# Specify the model to use and the threshold
model_name = 'ArcFace'
distance_metric = 'cosine'
threshold = 0.6  # Adjust this value to experiment with different thresholds

results2 = DeepFace.find(img_path=img2_path, db_path=db_path, model_name=model_name)

# Check if results2 is a list and iterate through the DataFrames
if isinstance(results2, list):
    match_found = False
    for idx, df in enumerate(results2):
        # Extract and print the folder names
        df['folder_name'] = df['identity'].apply(lambda x: x.split('/')[-2])
        folder_names = df['folder_name'].unique()
        if len(folder_names) > 0:
            match_found = True
            for folder_name in folder_names:
                print(folder_name)
    if not match_found:
        print("no matches found")
else:
    # Extract and print the folder names
    results2['folder_name'] = results2['identity'].apply(lambda x: x.split('/')[-2])
    folder_names = results2['folder_name'].unique()
    if len(folder_names) > 0:
        for folder_name in folder_names:
            print(folder_name)
    else:
        print("no matches found")