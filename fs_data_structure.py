import os
import magic
import random
# from gi.repository import Gtk
import gi
from PyQt5.QtGui import QColor, QPixmap

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import collections
import operator
import math
import random

DataStructure = [[], 0, 0]


# Data Structure Methods
def extension_table_data(path):
    global DataStructure
    d = DataStructure
    create_data(path)
    aggregate_data()
    sort_data()
    format_data()
    return DataStructure[3]


def create_data(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            ext = file_ext(full_path)
            size = file_size(full_path)

            row = find_key(DataStructure[0], ext)
            data = DataStructure[0][row] if row != -1 else []

            DataStructure[1] += 1  # Files Count
            DataStructure[2] += size  # Size
            if data:
                data[1] += 1  # Files
                data[2] += size  # Size
            else:
                data = [ext, 1, size, ext_full_name(full_path), icon_name(ext), rand_color()]
                DataStructure[0].append(data)  # Files Dict


def aggregate_data():
    for i, row in enumerate(DataStructure[0]):
        s = DataStructure[0][i][2] / DataStructure[2] * 100.0
        DataStructure[0][i].append("{0:.2f}%".format(s))


def sort_data():
    copy = list(DataStructure[0])
    copy.sort(key=operator.itemgetter(2), reverse=True)
    DataStructure.append(copy)


def format_data():
    for i, row in enumerate(DataStructure[3]):
        formatted_data = convert_size(DataStructure[3][i][2])
        DataStructure[3][i][2] = formatted_data


# Fetching Methods
def file_ext(path):
    return os.path.splitext(path)[-1][1:].strip().lower()


def ext_full_name(path):
    return magic.from_file(path).split(", ")[0].title()


def icon_name(path, size=32):
    icon_theme = Gtk.IconTheme.get_default()
    icon_info = icon_theme.lookup_icon(path, size, 0)
    if icon_info:
        pix = QPixmap(icon_info.get_filename())
        return pix
    return ""


def rand_color():
    levels = range(0, 256, 32)
    return QColor(random.choice(levels), random.choice(levels), random.choice(levels))


def file_size(path):
    return os.path.getsize(path)


# Helper Methods
def find_key(l, elem):
    for row, i in enumerate(l):
        if i[0] == elem:
            return row
    return -1


def convert_size(size):
    if size == 0:
        return '0B'
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return '%s%s' % (s, size_name[i])


if __name__ == "__main__":
    extension_table_data("/home/batman/dev")
