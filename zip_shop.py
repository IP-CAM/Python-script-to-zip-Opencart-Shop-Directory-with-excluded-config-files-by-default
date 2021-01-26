import os
import zipfile

current_folder_name: str = os.path.basename(os.getcwd())
archive_name: str = f'{current_folder_name}.zip'
# Exclude IDE working folders and Git folder
exclude_folders: tuple[str, ...] = (
    f'.{os.sep}.idea', f'.{os.sep}.vscode', f'.{os.sep}.git', f'.{os.sep}__pycache__')
# Exclude generated zip archive from himself, current python script and other unwanted files
exclude_files: tuple[str, ...] = (archive_name, os.path.basename(__file__), '.gitignore')
# Exclude OpenCart config files, set exclude_configs to [], if you don't want to exclude configs
exclude_configs: tuple[str, str] or [] = (
    f'.{os.sep}config.php', f'.{os.sep}admin{os.sep}config.php')


# Check if folder present in excluded folder
def check_folder(exclude_folder: exclude_folders, main_folder: str):
    for folder in exclude_folder:
        if folder in main_folder:
            return True
    return False


# Check if file present in excluded config files
def check_configs(file_full_path: str, exclude_configs_tuple: exclude_configs):
    for config_file in exclude_configs_tuple:
        if file_full_path == config_file:
            return True
    return False


# Generate zip archive of current OpenCart shop directory( with excluded configs )
def zip_dir(path: str, zip_handler, exclude_fold: exclude_folders, exclude_fl: exclude_files,
            exclude_conf: exclude_configs):
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
            try:
                # Add only root directory content, exclude the root directory folder
                zip_handler.write(file_path, file_path[path_len:])
            except OSError as zip_err:
                print(f'\tError is occurred, {zip_err}\n\tcontinue compression...')


def humanize_bytes(bytes_value: int, precision: int = 1):
    """Return a humanized string representation of a number of bytes.

    >>> humanize_bytes(1)
    '1 byte'
    >>> humanize_bytes(1024)
    '1.0 kB'
    >>> humanize_bytes(1024*123)
    '123.0 kB'
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    >>> humanize_bytes(1024*12342,2)
    '12.05 MB'
    >>> humanize_bytes(1024*1234,2)
    '1.21 MB'
    >>> humanize_bytes(1024*1234*1111,2)
    '1.31 GB'
    >>> humanize_bytes(1024*1234*1111,1)
    '1.3 GB'
    """
    abbrevs = (
        (1024 * 1024 * 1024, 'GB'),
        (1024 * 1024, 'MB'),
        (1024, 'kB'),
        (1, 'bytes')
    )
    if bytes_value == 1:
        return '1 byte'
    factor: int = 0
    suffix: str = ''
    for factor, suffix in abbrevs:
        if bytes_value >= factor:
            break
    return f'{round(bytes_value / factor, precision)} {suffix}'


# Create zip file from current directory
if __name__ == "__main__":
    try:
        with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_fl:
            print('Start compressing shop folder to zip archive...')
            zip_dir(f'.{os.sep}', zip_fl, exclude_folders, exclude_files, exclude_configs)
            zip_fl.close()
            print(
                f'End compressing shop folder to zip archive, ',
                f'file size {humanize_bytes(os.stat(archive_name).st_size, 2)}',
                sep=''
            )
    except zipfile.BadZipFile as err:
        print(f'Compressing is failed: {err}')
