# Delete Duplicate Images (on Linux)

### How It Works:
1. **Hash Function**: The script reads the content of each file and calculates its MD5 hash.
2. **Walking Through the Directory**: It recursively scans through the specified directory and its subdirectories for image files.
3. **Check for Duplicates**: For each image, it checks if the hash has already been encountered. If so, the script deletes the duplicate file.
4. **File Extensions**: The script checks for common image file extensions like .png, .jpg, .jpeg, .gif, bmp, tiff, webp. (You can add more extension types)

### How To Run:
1. In your terminal run: ```python3 imgDelete.py```
2. You will be asked to input your directory full path e.g. ```/home/user/Pictures/my-folder```
