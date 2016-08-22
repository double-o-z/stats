import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFileSystemModel, QDockWidget,
    QTreeView, QTableView, QListView
)
from PyQt5 import QtCore

# ROOT = QtCore.QDir.currentPath()
ROOT = QtCore.QDir.rootPath()


class MyDockWidget(QDockWidget):
    def __init__(self):
        super().__init__("File System")
        self.tree = QTreeView()
        self.model = MyFileSystemModel()
        self.create_dock()

    def create_dock(self):
        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)

        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.AllDirs)
        self.model.setRootPath(ROOT)

        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(ROOT))

        self.setWidget(self.tree)


class MyFileSystemModel(QFileSystemModel):
    def __init__(self):
        super().__init__()

    def headerData(self, section, orientation, role=None):
        if section == 4 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Percent"
        return super(MyFileSystemModel, self).headerData(section, orientation, role)

    def columnCount(self, parent=QtCore.QModelIndex(), **kwargs):
        return super(MyFileSystemModel, self).columnCount(parent)

    def data(self, index=QtCore.QModelIndex(), role=None):
        # Size Column
        if index.isValid() and index.column() == 1 and self.isDir(index):
            if role == QtCore.Qt.DisplayRole:
                return self.size(index)
            if role == QtCore.Qt.TextAlignmentRole:
                return QtCore.Qt.AlignRight
        # Disk Use Percentage Column
        if index.isValid() and index.column() == 4:
            if role == QtCore.Qt.DisplayRole:
                return self.percent(index)
            if role == QtCore.Qt.TextAlignmentRole:
                return QtCore.Qt.AlignLeft

        return super(MyFileSystemModel, self).data(index, role)

    def size(self, index):
        sibling = index.sibling(index.row()+1, 1)
        parent = sibling.parent()
        print("index: ", index.row(), index.column())
        print("sibling: ", sibling.row(), sibling.column())
        print("parent: ", parent.row(), parent.column())
        return super(MyFileSystemModel, self).size(index)

    def percent(self, index):
        return "100%"


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left_dock = MyDockWidget()
        self.init_ui()
        self.add_dock_widgets()

    def add_dock_widgets(self):
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.left_dock)

    def init_ui(self):
        self.setWindowTitle('WinDirStat')
        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    sys.exit(app.exec_())
