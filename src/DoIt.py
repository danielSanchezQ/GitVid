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

def doIt(repodir, repoout, inpath, outpath):
    cloneRepo(repodir,repoout)
    os.chdir(repoout)
    basename = os.path.basename(inpath)
    cheoutcount = countRevisions()
    framescount = cheoutcount
    while framescount > 0:
        files = getFilesFromPath(inpath)
        ImgUtils.reduceAndSave2Png(os.path.join(outpath, "{name}{num:0>3}.png".format(name=basename, num=framescount)), *files)
        framescount += 1
    ImgUtils.renderVideo(outpath, "{name}{num:0>3}.png".format(name=basename), cheoutcount, os.path.join(outpath, basename+".avi"))
    return outpath


if __name__ == "__main__":
    a = test1("https://github.com/django/django.git", r"c:/tests",r"c:/tests/django", r"c:/tests")











if __name__ == "__main__":
    print "Done"
