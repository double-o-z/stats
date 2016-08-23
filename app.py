import sys
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtWidgets import (QApplication, QColumnView, QSplitter, QTreeView, QListView, QTableView,
                             QHBoxLayout, QWidget, QStyleFactory)

from filesystemmodel import FileSystemModel


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()

    def initUI(self):
        h_box = QHBoxLayout(self)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter2 = QSplitter(Qt.Vertical)
        model = FileSystemModel()
        model.setRootPath(QDir.rootPath())
        model.setFilter(QDir.NoDotAndDotDot | QDir.AllEntries)
        for ViewType in (QTreeView, QListView, QTableView):
            view = ViewType()
            if ViewType != QTableView:
                splitter1.addWidget(view)
            else:
                splitter2.addWidget(splitter1)
                splitter2.addWidget(view)
            if ViewType == QListView:
                pass
            else:
                view.setModel(model)
                view.setRootIndex(model.index(QDir.homePath()))
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
