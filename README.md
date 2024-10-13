# Delete Duplicate Images (on Linux)

### How It Works:
1. **Hash Function**: The script reads the content of each file and calculates its MD5 hash.
2. **Walking Through the Directory**: It recursively scans through the specified directory and its subdirectories for image files.
3. **Check for Duplicates**: For each image, it checks if the hash has already been encountered. If so, the script deletes the duplicate file.
4. **File Extensions**: The script checks for common image file extensions like .png, .jpg, .jpeg, .gif, bmp, tiff, webp. (You can add more extension types)

### How To Run:
1. Change the directory path to your folder path
   - `directory = '/home/user/Documents/Folder/'  # Replace with your actual folder path`
2. In your terminal run: <code>python3 imgDelete.py</code>
