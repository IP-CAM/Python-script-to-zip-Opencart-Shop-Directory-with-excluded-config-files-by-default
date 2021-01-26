import os
import sys
import zipfile

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from gui.design import Ui_MainWindow
from zip_shop import zip_dir, humanize_bytes


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path: str = f'.{os.sep}'
        # Exclude IDE working folders and Git folder
        self.exclude_folders: tuple[str, ...] = (
            f'{os.sep}.idea', f'{os.sep}.vscode', f'{os.sep}.git', f'{os.sep}__pycache__')
        self.archive_name: str = f'{os.path.basename(os.getcwd())}.zip'
        # Exclude generated zip archive from himself, current python script and other unwanted files
        self.exclude_files: tuple[str, ...] = (
            self.archive_name, os.path.basename(__file__), '.gitignore')
        # Exclude OpenCart config files
        self.exclude_configs: tuple[str, str] or [] = []

    def browseFolderPathSlot(self):
        """
        Called when the user presses the Browse button
        :return: None
        """
        directory: str = QFileDialog.getExistingDirectory()
        if os.path.exists(directory) and os.path.isdir(directory):
            self.path = directory
            # Set text to input as directory path
            self.ui.lineEdit.setText(directory)
            self.archive_name = f'{os.path.basename(directory)}.zip'
            self.debugPrint(f'Set directory: {directory}')
        else:
            self.debugPrint('The directory is not exist!')

    def debugPrint(self, msg):
        """
        Print the message in the text edit at the bottom of the
        horizontal splitter.
        :return: None
        """
        self.ui.debugTextBrowser.append(msg)

    def returnedPressedSlot(self):
        """
        Called when the user enters a string in the line edit and
        presses the ENTER key.
        :return: None
        """
        directory: str = self.ui.lineEdit.text()
        if os.path.exists(directory) and os.path.isdir(directory):
            self.path = directory
            self.archive_name = f'{os.path.basename(directory)}.zip'
            self.debugPrint(f'Set directory: {directory}')
        else:
            self.debugPrint('The directory of your input is not exist!')

    def excludeConfigSlot(self):
        """
        Set excluded config files
        :return: None
        """
        if self.ui.checkBox.isChecked():
            if self.path == f'.{os.sep}':
                self.exclude_configs = (f'.{os.sep}config.php', f'.{os.sep}admin{os.sep}config.php')
            else:
                self.exclude_configs = (
                    f'{self.path}{os.sep}config.php', f'{self.path}{os.sep}admin{os.sep}config.php')
            self.debugPrint('Set exclude configs')
        else:
            self.exclude_configs = []
            self.debugPrint('Configs will not be excluded')

    def compressToZipSlot(self):
        """Creates zip file from chosen directory
        :return: None
        """
        self.debugPrint(f'Start compressing {self.path} folder to zip archive...')
        try:
            with zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_fl:
                zip_dir(self.path, zip_fl, self.exclude_folders, self.exclude_files,
                        self.exclude_configs,
                        zip_logger=self.debugPrint)
                zip_fl.close()
                self.debugPrint(f'file size {humanize_bytes(os.stat(self.archive_name).st_size, 2)}')
        except zipfile.BadZipFile as err:
            self.debugPrint(f'Compressing is failed: {err}')
        self.debugPrint(f'End compressing {self.path} folder to zip archive.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
