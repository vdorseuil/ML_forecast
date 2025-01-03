import os
import zipfile

def unzip_all_files_in_folder(folder_path):
    # Iterate through all files in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is a zip file
        if filename.endswith('.zip'):
            file_path = os.path.join(folder_path, filename)
            # Unzip the file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents into the same directory
                zip_ref.extractall(folder_path)
            print(f"Unzipped: {filename}")

# Example usage
folder_path = './'
unzip_all_files_in_folder(folder_path)