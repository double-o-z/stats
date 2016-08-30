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
        self.depth = 0
        self.d = {}
        self.create_data()
        # self.create_data_dfs()
        # self.create_data_bfs()
        self.aggregate_data()
        self.format_data()

    def sorted_structure(self):
        return self.d

    def create_data(self):
        for cur_dir, sub_dirs, files in os.walk(self.path, topdown=False):
            if os.path.islink(cur_dir):
                continue
            data = self.d.get(cur_dir, {})
            if not data:
                len_files = len([f for f in files if not os.path.islink(os.path.join(cur_dir, f))])
                len_sub_dirs = len([d for d in sub_dirs if not os.path.islink(os.path.join(cur_dir, d))])
                data = {'Size': 0, 'Files': len_files, 'Folders': len_sub_dirs}
                for sub_dir in sub_dirs:
                    dir_path = os.path.join(cur_dir, sub_dir)
                    if os.path.islink(dir_path):
                        continue
                    data['Size'] += self.d[dir_path]['Size']
                    data['Files'] += self.d[dir_path]['Files']
                    data['Folders'] += self.d[dir_path]['Folders']
                for file in files:
                    file_path = os.path.join(cur_dir, file)
                    if os.path.islink(file_path):
                        continue
                    size = get_size(file_path)
                    self.d[file_path] = {'Size': size}
                    data['Size'] += size
                self.d[cur_dir] = data

    def create_data_dfs(self, path=None):
        if not path:
            path = self.path
        data = self.d.get(path, {})
        if not data:
            data = {'Size': 0, 'Files': 0, 'Folders': 0}
            for item in os.listdir(path):
                full_path = os.path.join(path, item)

                if os.path.islink(full_path):
                    continue
                elif os.path.isfile(full_path):
                    size = get_size(full_path)
                    self.d[full_path] = {'Size': size}
                    data['Files'] += 1
                    data['Size'] += size
                elif os.path.isdir(full_path):
                    self.create_data_dfs(full_path)
                    data['Folders'] += 1
                    data['Size'] += self.d[full_path]['Size']
                    data['Files'] += self.d[full_path]['Files']
                    data['Folders'] += self.d[full_path]['Folders']

            self.d[path] = data

    def create_data_bfs(self, path=None, breadth_first_dirs=None):
        data_structure = self.d
        if not path:
            path = self.path
        if not breadth_first_dirs:
            breadth_first_dirs = []

        data = self.d.get(path, {})
        if data:
            return
        data = {'Size': 0, 'Files': 0, 'Folders': 0}
        sub_dirs = []
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.islink(full_path):
                continue
            elif os.path.isfile(full_path):
                size = get_size(full_path)
                self.d[full_path] = {'Size': size}
                data['Files'] += 1
                data['Size'] += size
            elif os.path.isdir(full_path):
                sub_dirs.append(full_path)

        bfd_copy = list(breadth_first_dirs)
        if breadth_first_dirs:
            for bfd in breadth_first_dirs:
                bfd_copy.remove(bfd)
                self.create_data_bfs(bfd, bfd_copy)

        sbd_copy = list(sub_dirs)
        for sub_dir in sub_dirs:
            sbd_copy.remove(sub_dir)
            self.create_data_bfs(sub_dir, sbd_copy)
            data['Folders'] += 1
            data['Size'] += self.d[sub_dir]['Size']
            data['Files'] += self.d[sub_dir]['Files']
            data['Folders'] += self.d[sub_dir]['Folders']

        self.d[path] = data

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
