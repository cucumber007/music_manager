import msvcrt
import sys
from intersect import intersect
from utils import my_print

root_path = sys.argv[1]
if root_path[-1] != "\\" or root_path[-1] != "\\":
    root_path = root_path + "/"

library_path = root_path + "Music library\\"
playlists_path = root_path + "Playlists\\"
res = intersect.intersect_dirs(library_path, playlists_path)


def print_intersected(res, limit=99999):
    print("Intersected: {}".format(len(res)))
    for inter in res[:limit]:
        print(inter.str_relative(library_path, playlists_path))




print_intersected(res, limit=15)
input = input("\nPress Enter to exit")
