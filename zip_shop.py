import os
import zipfile

current_folder_name = os.path.basename(os.getcwd())
archive_name = f'{current_folder_name}.zip'
# Exclude IDE working folders and Git folder
exclude_folders = (f'.{os.sep}.idea', f'.{os.sep}.vscode', f'.{os.sep}.git')
# Exclude generated zip archive from himself, current python script and other unwanted files
exclude_files = (archive_name, os.path.basename(__file__), '.gitignore')
# Exclude OpenCart config files
exclude_configs = (f'.{os.sep}config.php', f'.{os.sep}admin{os.sep}config.php')


# Check if folder present in excluded folder
def check_folder(exclude_folder, main_folder):
    for folder in exclude_folder:
        if folder in main_folder:
            return True
    return False


# Check if file present in excluded config files
def check_configs(file_full_path, exclude_configs_tuple):
    for config_file in exclude_configs_tuple:
        if file_full_path == config_file:
            return True
    return False


# Generate zip archive of current OpenCart shop directory( with excluded configs )
def zip_dir(path, zip_handler, exclude_fold, exclude_fl, exclude_conf):
    path_len = len(path)
    for root, _, files in os.walk(path):
        if check_folder(exclude_fold, root):
            continue
        for file in files:
            if file in exclude_fl:
                continue
            file_path = os.path.join(root, file)
            if check_configs(file_path, exclude_conf):
                continue
            zip_handler.write(file_path, file_path[path_len:])


# Create zip file from current directory
with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_fl:
    zip_dir(f'.{os.sep}', zip_fl, exclude_folders, exclude_files, exclude_configs)
    zip_fl.close()
