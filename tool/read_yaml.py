import os
from config import BASE_URL
import yaml


def read_yaml(readfile):
    with open("../data/" + readfile, "r", encoding="utf-8")as f:
        return yaml.load(f)


# def read_yaml(readfile):
#     with open(BASE_URL + os.sep + "data" + os.sep + readfile, "r", encoding="utf-8")as f:
#
#         return yaml.load(f)


if __name__ == '__main__':
    # print(read_yaml("login.yaml"))
    # print("---" * 25)
    arr = []
    for data in read_yaml("login.yaml").values():
        arr.append(tuple(data.values()))
    print(arr)
