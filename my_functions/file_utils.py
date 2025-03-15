import os

def get_files(root_folder: str, file_list: list, filter: str=None):
    """
    This function walks through folders and its subfolders and fetches files.
    params:
        root_folder (str): The start folder
        file_list (list): An empty list for storing files
        filter (str)(optional): Use a filter for collecting files
    """

    assert os.path.isdir(root_folder), "root_folder must be a directory."
    assert isinstance(file_list, list), "file_list must be a list."

    # collect all files and folders in root_folder
    folder_content = os.listdir(root_folder)

    # create a container for subfolders
    subfolders = []

    for i in folder_content:
        full_path = os.path.join(root_folder, i)
        if os.path.isfile(full_path):
            file_list.append(full_path)
        else:
            subfolders.append(full_path)
    
    # if we found subfolders start recursion
    for folder in subfolders:
        get_files(folder, file_list, filter)

if __name__ == "__main__":
    file_list = []
    get_files(r"D:\Work\PythonSuli\kezdo-250301\alapok_2", file_list)
    pass