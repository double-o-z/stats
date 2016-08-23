from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtCore import QAbstractListModel


class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super(FileSystemModel, self).__init__()


class ExtensionDataModel(QAbstractListModel):
    def __init__(self):
        super(QAbstractListModel, self).__init__()
        self.columns = ['File Type', 'Count', 'Size', 'Icon', 'Full Name', 'Color']
