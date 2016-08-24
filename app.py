import sys
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import (QApplication, QColumnView, QSplitter, QTreeView, QListView, QTableView,
                             QHBoxLayout, QWidget, QStyleFactory)

from data_models import FileSystemModel, ExtensionDataModel


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()

    def initUI(self):
        h_box = QHBoxLayout(self)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter2 = QSplitter(Qt.Vertical)

        file_system_model = FileSystemModel()
        file_system_model.setRootPath(QDir.rootPath())
        file_system_model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)

        tree_view = QTreeView()
        splitter1.addWidget(tree_view)
        tree_view.setModel(file_system_model)
        tree_view.setRootIndex(file_system_model.index(QDir.homePath()))

        table_view = QTableView()
        splitter1.addWidget(table_view)
        extensions_data_model = ExtensionDataModel()
        table_view.setModel(extensions_data_model)

        list_view = QListView()
        splitter2.addWidget(splitter1)
        splitter2.addWidget(list_view)
        list_view.setModel(file_system_model)
        list_view.setRootIndex(file_system_model.index(QDir.homePath()))

        # splitter1.setSizes([100, 200])
        h_box.addWidget(splitter2)
        self.setLayout(h_box)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.showMaximized()
        self.setWindowTitle('WinDirStat')
        self.show()


def main():
    app = QApplication(sys.argv)
    mw = MainWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
