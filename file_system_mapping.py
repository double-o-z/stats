# import sys
# import os
#
# fs = {
#         'name': "/",
#         'files': {},
#         'folders': {},
#         'files_count': 0,
#         'folders_count': 0,
#         'percentage': 0.0
#     }
#
# FILE = {
#         'percentage': 0.0
#     }
#
# FOLDER = {
#         'files': {},
#         'folders': {},
#         'files_count': 0,
#         'folders_count': 0,
#         'percentage': 0.0
#     }
#
# root = "/"
#
#
# def walk(fs, dir, meth):
#     """ walks a directory, and executes a callback on each file """
#     dir = os.path.abspath(dir)
#     for file in [file for file in os.listdir(dir) if file not in [".", ".."]]:
#         nfile = os.path.join(dir, file)
#         # meth(nfile)
#         if os.path.isdir(nfile):
#             walk(fs, nfile, meth)
#         fs = meth(fs, nfile)
#     return fs
#
#
# def meth(fs, nfile):
#     parts = nfile.split("/")[1:]
#     for path in parts:
#         return rec(fs, path, nfile)
#
#
# def rec(fs, path, nfile):
#     path_type, path_struct = ('files', FILE) if os.path.isfile(path) else ('folders', FOLDER)
#     e = fs[path_type].get(path, {})
#     if not e:
#         fs[path_type][path] = dict(path_struct)
#         fs[path_type][path]['name'] = path
#         fs[path_type][path]['size'] = os.stat(nfile)
#     else:
#         fs[path_type][path] = rec(fs[path_type][path], path, nfile)
#     return fs
#
# if __name__ == '__main__':
#     fs = walk(fs, root, meth)


import os
from functools import reduce


def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    # a = os.sep
    # b = rootdir.rfind(a)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


if __name__ == '__main__':
    fs = get_directory_structure("/..")
    a = 0
