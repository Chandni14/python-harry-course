import os

# Specify the directory path
directory_path = '/'

# Check if the directory exists
if os.path.isdir(directory_path):
    print("\nContents of the directory:")
    
    for item in os.listdir(directory_path):
        print(item)
else:
    print("Invalid directory path.")