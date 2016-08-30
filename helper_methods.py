from PyQt5.QtGui import QColor, QPixmap

import os
import magic
import random
import math

# import gi
# gi.require_version("Gtk", "3.0")
# from gi.repository import Gtk


def file_ext(path):
    return os.path.splitext(path)[-1][1:].strip().lower()


def ext_full_name(path):
    return magic.from_file(path).split(", ")[0].title()

# def icon_name(path, size=32):
#     icon_theme = Gtk.IconTheme.get_default()
#     icon_info = icon_theme.lookup_icon(path, size, 0)
#     if icon_info:
#         pix = QPixmap(icon_info.get_filename())
#         return pix
#     return ""


def get_size(path):
    return os.path.getsize(path)


def rand_color():
    levels = range(0, 256, 32)
    return QColor(random.choice(levels), random.choice(levels), random.choice(levels))


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
