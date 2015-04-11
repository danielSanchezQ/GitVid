__author__ = 'Daniel Sanchez Quiros'


import os.path as osp
import os



def getFilesFromPath(path, *args):
    if osp.exists(path):
        os.chdir(path)
        ret = []
        content = os.listdir(path)
        ret.extend(map(lambda x: osp.join(path,x),filter(lambda x: osp.isfile(x), content)))
        content = map(lambda x: osp.join(path,x),filter(lambda x: osp.isdir(x), content))
        if content:
            for e in map(getFilesFromPath, content):
                ret.extend(e)
        return filter(lambda x: osp.basename(x) not in args, ret)
    else:
        raise ValueError("Path does not exists!")

def getFromPathAndExtension(path, extension):
    if osp.exists(path):
        return filter(lambda x: osp.splitext(x)[1] == extension,os.listdir(path))
    else:
        raise ValueError("Path does not exists!")



if __name__ == "__main__":
    from pprint import pprint
    flst = getFilesFromPath(r"C:/tests/spheres")
    pprint(flst)
    print all(map (osp.isfile,flst))
    print getFromPathAndExtension("c:/tests", ".png")









