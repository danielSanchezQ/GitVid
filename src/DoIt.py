__author__ = 'Daniel Sanchez Quiros'

from GitUtils import *
from PathUtils import *
from ImageUtils import *


def test1(inpath, outpath):
    files = getFilesFromPath(inpath)
    imgs = []
    for file in files:
        img = ImgUtils(file)
        imgs.append(img.toPNG(outpath))
        del img
    return imgs


if __name__ == "__main__":
    a = test1(r"c:/tests/spheres", r"c:/tests")
    print len(a) == len(getFilesFromPath(r"c:/tests/spheres"))











if __name__ == "__main__":
    print "Done"
