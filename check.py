import os
dataset_path = '/Users/leopold/customer_detection/database'
for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.endswith(('png', 'jpg', 'jpeg')):
            print(f"Loading image: {os.path.join(root, file)}")
