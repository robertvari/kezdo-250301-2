from my_functions.file_utils import get_files

file_list = []
get_files(r"C:\Work\PythonSuli\kezdo-250301-2", file_list, filter=".py")

for i in file_list:
    print(i)