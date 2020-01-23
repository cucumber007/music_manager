import sys
import os

def filename_equal(name1, name2):
    return name1.lower() == name2.lower()


def filename(path):
    return path.split("\\")[-1]


def intersect_dirs(folder1_path, folder2_path):
    files1 = []
    files2 = []

    for path, dirs, files in os.walk(folder1_path):
        for file in files:
            files1.append(path+"\\"+file)

    for path, dirs, files in os.walk(folder2_path):
        for file in files:
            files2.append(path+"\\"+file)

    intersected = []

    for path1 in files1:
        filename1 = filename(path1)
        filtered = list(filter(lambda x: filename_equal(filename(x), filename1), files2))
        if len(filtered) > 0:
            intersected.append(Intersection(path1, filtered[0]))

    return intersected


if __name__ == "__main__":
    intersect_dirs(sys.argv[1], sys.argv[2])


class Intersection:

    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
        self.name = path1.split("\\")[-1]

    def str_relative(self, root1, root2):
        return "{}\t\t{}\t\t{}".format(
            self.name,
            self.path1.replace(root1, ""),
            self.path2.replace(root2, "")
        )

    def __str__(self) -> str:
        return "{}\t{}\t{}".format(
            self.name,
            self.path1,
            self.path2
        )

