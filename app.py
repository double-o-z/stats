import sys
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import (QApplication, QColumnView, QSplitter, QTreeView, QListView, QTableView,
                             QHBoxLayout, QWidget, QStyleFactory)

from data_models import FileSystemModel, ExtensionDataModel, TreeDataModel, ROOT_PATH


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()

    def initUI(self):
        # Initializing Models
        file_system_model = FileSystemModel()
        file_system_model.setRootPath(ROOT_PATH)
        file_system_model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)
        extensions_data_model = ExtensionDataModel()
        tree_model = TreeDataModel()
        tree_model.setRootPath(ROOT_PATH)
        tree_model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)

        # Initializing Views
        tree_view = QTreeView()
        list_view = QListView()
        table_view = QTableView()

        # Binding views to models
        # Top Left View
        tree_view.setModel(tree_model)
        tree_view.setRootIndex(tree_model.index(ROOT_PATH))
        # Top Right View
        table_view.setModel(extensions_data_model)
        # Bottom View
        list_view.setModel(file_system_model)
        list_view.setRootIndex(file_system_model.index(ROOT_PATH))

        # Layout
        h_box = QHBoxLayout(self)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter2 = QSplitter(Qt.Vertical)
        splitter1.addWidget(tree_view)
        # splitter1.addWidget(table_view)
        splitter2.addWidget(splitter1)
        # splitter2.addWidget(list_view)
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
