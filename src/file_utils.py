import os


def concatenate_files(path, excluded_files=None):
    if not os.path.isdir(path):
        raise ValueError("Path is not a directory")
    return excluded_files_to_str(path, excluded_files)


def excluded_files_to_str(files, excluded_files):
    filtered_files = filter_files(files, excluded_files)
    return files_to_str(filtered_files)


def filter_files(path, excluded_files):
    all_items = os.listdir(path)
    files_in_directory = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    if not excluded_files:
        return files_in_directory
    return [f for f in files_in_directory if f not in excluded_files]


def files_to_str(files):
    return '\n'.join(file_to_str(file) for file in files)


def file_to_str(file_path):
    str = file_path + "\n"
    with open(file_path, 'r') as file:
        str += file.read()
    return str
