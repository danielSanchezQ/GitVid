__author__ = 'Daniel Sanchez Quiros'

from GitUtils import *
from PathUtils import *
from ImageUtils import *


def test1(repodir, repoout, inpath, outpath):
    cloneRepo(repodir,repoout)
    print "getting files"
    files = getFilesFromPath(inpath)
    print "building image"
    ImgUtils.reduceAndSave2Png(outpath, *files)
    return files


if __name__ == "__main__":
    a = test1("https://github.com/django/django.git", r"c:/tests",r"c:/tests/django", r"c:/tests")











if __name__ == "__main__":
    print "Done"
