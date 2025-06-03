import os

def list_folders(path):
    folders = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

# Example usage:
directory_path = "./" # Replace with your directory path
folder_list = list_folders(directory_path)
print(folder_list)