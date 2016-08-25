from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant, QAbstractItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from fs_data_structure import ExtensionsDataStructure, FoldersDataStructure

ROOT_PATH = "/home/batman/dev"


class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super(FileSystemModel, self).__init__()

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        my_data = super(FileSystemModel, self).data(index, role)
        return my_data

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        my_data_header = super(FileSystemModel, self).headerData(section, orientation, role)
        return my_data_header


class ExtensionDataModel(QAbstractTableModel):
    def __init__(self):
        super(QAbstractTableModel, self).__init__()
        self.columns = ['Extension', 'Files', 'Size', 'Full Name',
                        # 'Icon',
                        'Color', 'Percentage']
        self.data_structure = ExtensionsDataStructure(ROOT_PATH).sorted_structure()

    def columnCount(self, parent=QModelIndex(), *args, **kwargs):
        return len(self.columns)

    def rowCount(self, parent=QModelIndex(), *args, **kwargs):
        return len(self.data_structure)

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.columns[section]
            elif orientation == Qt.Vertical:
                return section + 1
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft
        return super(QAbstractTableModel, self).headerData(section, orientation, role)

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        if (role == Qt.DisplayRole and index.column() != 4) or (role == Qt.BackgroundColorRole and index.column() == 4):
            return self.data_structure[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft
        return QVariant()


class TreeDataModel(QAbstractItemModel):
    def __init__(self):
        super(QAbstractItemModel, self).__init__()
        self.columns = []
        self.data_structure = FoldersDataStructure(ROOT_PATH).sorted_structure()

    def columnCount(self, parent=QModelIndex(), *args, **kwargs):
        pass

    def rowCount(self, parent=QModelIndex(), *args, **kwargs):
        pass

    def headerData(self, section, orientation=Qt.Horizontal, role=Qt.DisplayRole):
        pass

    def data(self, index=QModelIndex(), role=Qt.DisplayRole):
        pass
