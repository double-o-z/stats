import os
import magic
import random
# from gi.repository import Gtk
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import collections


def file_ext(path):
    return os.path.splitext(path)[-1][1:].strip().lower()


def ext_full_name(path):
    return magic.from_file(path).split(", ")[0].title()


def icon_name(path, size=32):
    icon_theme = Gtk.IconTheme.get_default()
    icon_info = icon_theme.lookup_icon(path, size, 0)
    if icon_info:
        return icon_info.get_filename()
    return ""


def rand_color():
    r = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(), r(), r())


def file_size(path):
    return os.path.getsize(path)


def create_data_structure(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            key = file_ext(full_path)
            size = file_size(full_path)
            data = DataStructure['files'].get(key, {})
            if data:
                data['files'] += 1
                data['size'] += size
                DataStructure['total_size'] += size
                DataStructure['total_files'] += 1
            else:
                data['files'] = 1
                data['size'] = size
                data['icon'] = icon_name(key)
                data['full_name'] = ext_full_name(full_path)
                data['color_value'] = rand_color()
                DataStructure['files'][key] = data
                DataStructure['total_ext_types'] += 1
                DataStructure['total_files'] += 1
                DataStructure['total_size'] += size
    add_percentage_data()
    create_ordered_list()
    return DataStructure


def add_percentage_data():
    for key in DataStructure['files']:
        s = DataStructure['files'][key]['size'] / DataStructure['total_size'] * 100.0
        DataStructure['files'][key]['percentage'] = "{0:.2f}%".format(s)


def create_ordered_list():
    DataStructure['sorted'] = sorted(DataStructure['files'].items(), key=lambda x: x[1]['size'], reverse=True)

DataStructure = {
    'total_size': 0,
    'total_files': 0,
    'total_ext_types': 0,
    'files': {}
}


if __name__ == "__main__":
    DataStructure['files'] = {'': {'files': 195, 'color_value': '#143D99', 'full_name': 'Elf 64-Bit Lsb Executable', 'icon': '', 'size': 13035608, 'percentage': '4.42%'}, 'zip': {'files': 2, 'color_value': '#7D6BDB', 'full_name': 'Zip Archive Data', 'icon': '/usr/share/icons/Humanity/mimes/32/zip.svg', 'size': 1810, 'percentage': '0.00%'}, 'cpp': {'files': 4, 'color_value': '#EFDE42', 'full_name': 'C++ Source', 'icon': '', 'size': 4358, 'percentage': '0.00%'}, '2-fs_data_structure': {'files': 2, 'color_value': '#F83FF1', 'full_name': 'Ascii Text', 'icon': '', 'size': 204, 'percentage': '0.00%'}, 'h': {'files': 7, 'color_value': '#46DD27', 'full_name': 'Ascii Text', 'icon': '', 'size': 1109, 'percentage': '0.00%'}, '56': {'files': 3, 'color_value': '#DC793A', 'full_name': 'Elf 64-Bit Lsb Shared Object', 'icon': '', 'size': 30492116, 'percentage': '10.34%'}, 'dat': {'files': 1, 'color_value': '#37F5D8', 'full_name': 'Lif File', 'icon': '', 'size': 10207936, 'percentage': '3.46%'}, 'md': {'files': 1, 'color_value': '#CE13BF', 'full_name': 'Ascii Text', 'icon': '', 'size': 88, 'percentage': '0.00%'}, 'txt': {'files': 31, 'color_value': '#ECF167', 'full_name': 'Ascii Text', 'icon': '/usr/share/icons/Humanity/mimes/32/txt.svg', 'size': 14294, 'percentage': '0.00%'}, 'whl': {'files': 20, 'color_value': '#ED6EF9', 'full_name': 'Zip Archive Data', 'icon': '', 'size': 1182487, 'percentage': '0.40%'}, 'pem': {'files': 3, 'color_value': '#A4975B', 'full_name': 'Utf-8 Unicode Text', 'icon': '', 'size': 1034136, 'percentage': '0.35%'}, 'fish': {'files': 1, 'color_value': '#5538A5', 'full_name': 'Ascii Text', 'icon': '', 'size': 2221, 'percentage': '0.00%'}, 'conf': {'files': 1, 'color_value': '#79CE44', 'full_name': 'Ascii Text', 'icon': '', 'size': 20, 'percentage': '0.00%'}, 'c': {'files': 18, 'color_value': '#74CA6F', 'full_name': 'C Source', 'icon': '', 'size': 15070, 'percentage': '0.01%'}, 'sample': {'files': 9, 'color_value': '#CC4409', 'full_name': 'Posix Shell Script', 'icon': '', 'size': 14724, 'percentage': '0.00%'}, 'so': {'files': 125, 'color_value': '#E4A769', 'full_name': 'Elf 64-Bit Lsb Shared Object', 'icon': '', 'size': 45830072, 'percentage': '15.55%'}, 'csh': {'files': 1, 'color_value': '#49FBEC', 'full_name': 'Ascii Text', 'icon': '', 'size': 1023, 'percentage': '0.00%'}, 'pyc': {'files': 942, 'color_value': '#4B7276', 'full_name': 'Data', 'icon': '', 'size': 9959584, 'percentage': '3.38%'}, 'metainfo': {'files': 2, 'color_value': '#F7093B', 'full_name': 'Ascii Text', 'icon': '', 'size': 12935, 'percentage': '0.00%'}, 'qml': {'files': 333, 'color_value': '#260CA3', 'full_name': 'Ascii Text', 'icon': '', 'size': 1917495, 'percentage': '0.65%'}, 'tmpl': {'files': 4, 'color_value': '#0979CD', 'full_name': 'Ascii Text', 'icon': '', 'size': 678, 'percentage': '0.00%'}, 'py': {'files': 957, 'color_value': '#FACEDD', 'full_name': 'Python Script', 'icon': '', 'size': 10021872, 'percentage': '3.40%'}, 'rst': {'files': 11, 'color_value': '#978DEF', 'full_name': 'Ascii Text', 'icon': '', 'size': 81055, 'percentage': '0.03%'}, 'qmltypes': {'files': 32, 'color_value': '#6723CF', 'full_name': 'Ascii Text', 'icon': '', 'size': 1009614, 'percentage': '0.34%'}, 'xml': {'files': 29, 'color_value': '#382E4F', 'full_name': 'Xml 1.0 Document', 'icon': '', 'size': 152333, 'percentage': '0.05%'}, 'iml': {'files': 7, 'color_value': '#BE0AA6', 'full_name': 'Xml 1.0 Document', 'icon': '', 'size': 7588, 'percentage': '0.00%'}, 'pak': {'files': 57, 'color_value': '#1FBA87', 'full_name': 'Data', 'icon': '', 'size': 23230117, 'percentage': '7.88%'}, 'exe': {'files': 20, 'color_value': '#B8F9E9', 'full_name': 'Pe32+ Executable (Gui) X86-64', 'icon': '', 'size': 1557504, 'percentage': '0.53%'}, 'js': {'files': 4, 'color_value': '#279F78', 'full_name': 'Ascii Text', 'icon': '', 'size': 13629, 'percentage': '0.00%'}, '7': {'files': 3, 'color_value': '#51F6C2', 'full_name': 'A /Home/Batman/Dev/Stats/Bin/Python2 Script', 'icon': '', 'size': 3546578, 'percentage': '1.20%'}, '5': {'files': 35, 'color_value': '#993895', 'full_name': 'Symbolic Link To Python3', 'icon': '', 'size': 135869466, 'percentage': '46.09%'}, 'qm': {'files': 118, 'color_value': '#107B0F', 'full_name': 'Qt Translation File', 'icon': '', 'size': 5411902, 'percentage': '1.84%'}, 'cfg': {'files': 4, 'color_value': '#587317', 'full_name': 'Ascii Text', 'icon': '', 'size': 5690, 'percentage': '0.00%'}, 'png': {'files': 137, 'color_value': '#26265B', 'full_name': 'Png Image Data', 'icon': '', 'size': 128158, 'percentage': '0.04%'}, 'json': {'files': 14, 'color_value': '#3AFF73', 'full_name': 'Ascii Text', 'icon': '', 'size': 41706, 'percentage': '0.01%'}}
    create_data_structure("/home/batman/dev")
