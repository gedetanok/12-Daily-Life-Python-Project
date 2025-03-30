# This all-in-one automation script transforms how you 
# organize and manage your files in just minutes! Simply provide 
# the path to the folder you want to clean up, and the script will 
# work its magic.

# File Extension Sorting
# Duplicate File Removal
# Date-Based Organization

import os
import shutil
import hashlib
from datetime import datetime

def get_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    with open(file_path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def organize_by_date_and_extension(folder_path):
    """Organize files by date, then by extension, and handle duplicates."""
    # Create a "Duplicates" folder at the root directory
    duplicates_folder = os.path.join(folder_path, '_Duplicates')
    os.makedirs(duplicates_folder, exist_ok=True)

    # Dictionary to store file hashes for duplicate detection
    file_hashes = {}

    # Iterate over all files in the directory
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_path in all_files:
        # Get the modification date of the file
        modification_time = os.path.getmtime(file_path)
        modification_date = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d')

        # Create a folder for the modification date if it doesn't exist
        date_folder = os.path.join(folder_path, modification_date)
        os.makedirs(date_folder, exist_ok=True)

        # Calculate the file hash
        file_hash = get_file_hash(file_path)

        # Check for duplicates
        if file_hash in file_hashes:
            # File is a duplicate, move to "Duplicates" folder
            shutil.move(file_path, os.path.join(duplicates_folder, os.path.basename(file_path)))
            print(f"Moved duplicate file {os.path.basename(file_path)} to Duplicates folder.")
        else:
            # Store the file hash to prevent future duplicates
            file_hashes[file_hash] = file_path

            # Move the file to the date folder
            new_path = os.path.join(date_folder, os.path.basename(file_path))
            shutil.move(file_path, new_path)

            # Organize files within the date folder by extension
            _, extension = os.path.splitext(new_path)
            extension = extension.lower()
            extension_folder = os.path.join(date_folder, extension[1:])  # Remove the dot from extension
            os.makedirs(extension_folder, exist_ok=True)

            # Move the file to its extension-specific folder
            shutil.move(new_path, os.path.join(extension_folder, os.path.basename(new_path)))
            print(f"Moved {os.path.basename(new_path)} to {extension_folder}.")

    print("Files organized by date, extension, and duplicates handled successfully!")

if __name__ == "__main__":
    # Specify the directory to organize
    folder_path = input("Enter the path to the folder to organize: ")
    organize_by_date_and_extension(folder_path)
    