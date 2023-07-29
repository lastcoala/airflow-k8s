import os

def path(path):
    curdir = os.path.dirname(__file__)
    temp = "/".join(curdir.split("/")[:-1])
    return os.path.join(temp, path)