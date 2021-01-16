import os
import zipfile

current_folder_name = os.path.basename(os.getcwd())
archive_name = f'{current_folder_name}.zip'
exclude_folders = (f'.{os.sep}.idea', f'.{os.sep}.git', f'.{os.sep}.vscode')
exclude_files = (archive_name, os.path.basename(__file__))
exclude_configs = (f'.{os.sep}config.php', f'.{os.sep}admin{os.sep}config.php')


def zip_dir(path, zip_handler, exclude_fold, exclude_fl):
    path_len = len(path)
    for root, _, files in os.walk(path):
        check_folder = False
        for folder in exclude_fold:
            if folder in root:
                check_folder = True
        if check_folder:
            continue
        for file in files:
            if file in exclude_fl:
                continue
            file_path = os.path.join(root, file)
            check_configs = False
            for config_file in exclude_configs:
                if file_path == config_file:
                    check_configs = True
            if check_configs:
                continue
            zip_handler.write(file_path, file_path[path_len:])


with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_fl:
    zip_dir(f'.{os.sep}', zip_fl, exclude_folders, exclude_files)
    zip_fl.close()
