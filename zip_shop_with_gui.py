import os
import zipfile
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from gui.design import Ui_MainWindow
from zip_shop import zip_dir, humanize_bytes, exclude_configs, exclude_folders, exclude_files, \
    archive_name


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path = f'.{os.sep}'
        # Exclude OpenCart config files
        self.exclude_configs: tuple[str, str] or [] = []

    def browseFolderPathSlot(self):
        pass

    def returnedPressedSlot(self):
        pass

    def excludeConfigSlot(self):
        self.exclude_configs = exclude_configs

    def compressToZipSlot(self):
        """
        Create zip file from current directory
        :return: None
        """
        try:
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_fl:
                print('Start compressing shop folder to zip archive...')
                zip_dir(self.path, zip_fl, exclude_folders, exclude_files, self.exclude_configs)
                zip_fl.close()
                print(
                    f'End compressing shop folder to zip archive, ',
                    f'file size {humanize_bytes(os.stat(archive_name).st_size, 2)}',
                    sep=''
                )
        except zipfile.BadZipFile as err:
            print(f'Compressing is failed: {err}')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
