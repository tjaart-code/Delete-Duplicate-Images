#    Copyright (C) 2025 Tjaart de Kock

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses.

import os
import hashlib

# Function to compute hash of a file
def get_file_hash(file_path, chunk_size=4096):
    try:
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Function to find and delete duplicate images
def delete_duplicates(directory):
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' is not a valid directory.")
        return
    
    hashes = {}
    duplicates_found = []

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if the file is an image based on file extension
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
                file_path = os.path.join(root, filename)
                print(f"Processing: {file_path}")  # Debugging: see what is being processed

                # Get the file's hash
                file_hash = get_file_hash(file_path)
                if file_hash is None:
                    continue

                # If the hash exists, it's a duplicate
                if file_hash in hashes:
                    print(f"Duplicate found: {file_path}")
                    duplicates_found.append(file_path)
                else:
                    hashes[file_hash] = file_path

    # Show duplicates found and ask for confirmation
    if duplicates_found:
        print(f"\nFound {len(duplicates_found)} duplicate image(s):")
        for i, dup_file in enumerate(duplicates_found, 1):
            print(f"  {i}. {dup_file}")
        
        # Ask for user confirmation
        confirmation = input("\nAre you sure you want to delete these duplicates? (yes/no): ").strip().lower()
        if confirmation != "yes":
            print("Deletion cancelled.")
            return
        
        # Delete the duplicates
        deleted_count = 0
        for file_path in duplicates_found:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        
        print(f"\nSuccessfully deleted {deleted_count} duplicate image(s).")
    else:
        print("No duplicate images found.")

# Example usage
if __name__ == "__main__":
    # Prompt user for directory path
    while True:
        directory = input("Please enter the directory path: ").strip()
        if os.path.isdir(directory):
            delete_duplicates(directory)
            break
        else:
            print(f"Error: '{directory}' is not a valid directory. Please try again.")
