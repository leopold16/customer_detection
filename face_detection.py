import os
from deepface import DeepFace
import logging

def detect_face(image_path):
    try:
        local_db_path = "./local_db"  # Path to your local image database

        model_name = 'ArcFace'
        distance_metric = 'cosine'
        threshold = 0.6

        results = DeepFace.find(img_path=image_path, db_path=local_db_path, model_name=model_name, distance_metric=distance_metric)

        if isinstance(results, list):
            match_found = False
            for df in results:
                df['folder_name'] = df['identity'].apply(lambda x: x.split('/')[-2])
                folder_names = df['folder_name'].unique()
                if len(folder_names) > 0:
                    match_found = True
                    return folder_names[0]  # Return the first match
            if not match_found:
                return "no matches found"
        else:
            results['folder_name'] = results['identity'].apply(lambda x: x.split('/')[-2])
            folder_names = results['folder_name'].unique()
            if len(folder_names) > 0:
                return folder_names[0]  # Return the first match
            else:
                return "no matches found"
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return "error"

    return "no matches found"
