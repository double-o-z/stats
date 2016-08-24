from PyQt5.QtWidgets import QFileSystemModel
from PyQt5.QtCore import QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from fs_data_structure import extension_table_data


class FileSystemModel(QFileSystemModel):
    def __init__(self):
        super(FileSystemModel, self).__init__()


class ExtensionDataModel(QAbstractTableModel):
    def __init__(self):
        super(QAbstractTableModel, self).__init__()
        self.columns = ['Extension', 'Files', 'Size', 'Full Name', 'Icon', 'Color', 'Percentage']
        self.data_structure = extension_table_data("/home/batman/dev")

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
        if (role == Qt.DisplayRole and index.column() != 5) or (role == Qt.BackgroundColorRole and index.column() == 5):
            return self.data_structure[index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignLeft
        return QVariant()
