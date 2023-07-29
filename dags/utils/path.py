import os

def path(path):
    print(os.path.basename(__file__))
    print(os.path.dirname(__file__))
    return os.path.join(os.getcwd(), path)