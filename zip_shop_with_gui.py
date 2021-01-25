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
        """
        Called when the user presses the Browse button
        :return: None
        """
        self.debugPrint('Browse button pressed')

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
        self.debugPrint('RETURN key pressed in LineEdit widget')

    def excludeConfigSlot(self):
        """
        Set excluded config files
        :return: None
        """
        self.exclude_configs = exclude_configs

    def compressToZipSlot(self):
        """Create zip file from current directory
        :return: None
        """
        try:
            with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zip_fl:
                self.debugPrint('Start compressing shop folder to zip archive...')
                zip_dir(self.path, zip_fl, exclude_folders, exclude_files, self.exclude_configs)
                zip_fl.close()
                self.debugPrint('End compressing shop folder to zip archive, ')
                self.debugPrint(f'file size {humanize_bytes(os.stat(archive_name).st_size, 2)}')
        except zipfile.BadZipFile as err:
            self.debugPrint(f'Compressing is failed: {err}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
