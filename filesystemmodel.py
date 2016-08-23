from PyQt5.QtWidgets import QFileSystemModel


class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super(FileSystemModel, self).__init__()
