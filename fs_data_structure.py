import os
import operator

from helper_methods import *


class ExtensionsDataStructure:
    def __init__(self, path):
        self.path = path
        self.d = [[], 0, 0]
        self.create_data()
        self.aggregate_data()
        self.sort_data()
        self.format_data()

    def sorted_structure(self):
        return self.d[3]

    def create_data(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                full_path = os.path.join(root, file)
                ext = file_ext(full_path)
                size = get_size(full_path)

                row = find_key(self.d[0], ext)
                data = self.d[0][row] if row != -1 else []

                self.d[1] += 1  # Files Count
                self.d[2] += size  # Size
                if data:
                    data[1] += 1  # Files
                    data[2] += size  # Size
                else:
                    data = [ext, 1, size, ext_full_name(full_path),
                            # icon_name(ext),
                            rand_color()]
                    self.d[0].append(data)  # Files Dict

    def aggregate_data(self):
        for i, row in enumerate(self.d[0]):
            s = self.d[0][i][2] / self.d[2] * 100.0
            self.d[0][i].append("{0:.2f}%".format(s))

    def sort_data(self):
        copy = list(self.d[0])
        copy.sort(key=operator.itemgetter(2), reverse=True)
        self.d.append(copy)

    def format_data(self):
        for i, row in enumerate(self.d[3]):
            formatted_data = convert_size(self.d[3][i][2])
            self.d[3][i][2] = formatted_data


class FoldersDataStructure:
    def __init__(self, path):
        self.path = path
        self.d = {}
        self.create_data()
        self.aggregate_data()
        self.format_data()

    def sorted_structure(self):
        return self.d

    def create_data(self):
        a = self.d
        files_total = 0
        folders_total = 0
        size_total = 0
        last_dir = ""
        for cur_dir, sub_dirs, files in os.walk(self.path, topdown=False):
            size_count = 0
            files_count = len(files)
            folders_count = len(sub_dirs)
            for file in files:
                size = get_size(os.path.join(cur_dir, file))
                file_path = os.path.join(cur_dir, file)
                self.d[file_path] = {'Size': size}
                size_count += size

            data = self.d.get(cur_dir, False)
            if not data:
                data = {'Files': 0, 'Folders': 0, 'Size': 0}
                for sub_dir in sub_dirs:
                    key = os.path.join(cur_dir, sub_dir)
                    if os.path.islink(key):
                        continue
                    data['Size'] += self.d[key]['Size']
                    data['Files'] += self.d[key]['Files']
                    data['Folders'] += self.d[key]['Folders']

            data['Size'] += size_count
            data['Files'] += files_count
            data['Folders'] += folders_count

            self.d[cur_dir] = data

    def aggregate_data(self):
        for key, value in self.d.items():
            if key == self.path:
                self.d[key]['Percentage'] = "100.0%"
                continue
            parent = "/".join(key.split("/")[:-1])
            parent_size = self.d[parent]['Size'] * 1.0
            if parent_size > 0:
                self.d[key]['Percentage'] = "{0:.2f}%".format(self.d[key]['Size'] / parent_size * 100.0)
            else:
                self.d[key]['Percentage'] = "0.0%"

    def sort_data(self):
        pass

    def format_data(self):
        for key, value in self.d.items():
            self.d[key]['Size'] = convert_size(self.d[key]['Size'])
