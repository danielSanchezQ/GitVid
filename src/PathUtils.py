__author__ = 'Daniel Sanchez Quiros'


import os.path as osp
import os

def getFilesFromPath(path):
    if osp.exists(path):
        os.chdir(path)
        ret = []
        content = os.listdir(path)
        ret.extend(map(lambda x: osp.join(path,x),filter(lambda x: osp.isfile(x), content)))
        content = map(lambda x: osp.join(path,x),filter(lambda x: osp.isdir(x), content))
        if content:
            for e in map(getFilesFromPath, content):
                ret.extend(e)
        return ret
    else:
        raise ValueError("Path does not exists!")




if __name__ == "__main__":
    print all(map (osp.isfile,getFilesFromPath("C:/Users/Netwave/Documents/Visual Studio 2013")))









