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
    if not os.path.exists(inpath):
        cloneRepo(repodir, repoout)
    basename = os.path.basename(inpath)
    os.chdir(repoout)
    commits = getCommits(inpath)
    for framescount, commit in enumerate(commits):
        checkout(commit)
        files = getFilesFromPath(inpath)
        ImgUtils.reduceAndSave2Png(os.path.join(outpath, "{name}{num:0>3}.png".format(name=basename, num=framescount)), *files)
    #ImgUtils.renderVideo(outpath, "{name}".format(name=basename)+"{:0>3}.png", cheoutcount, os.path.join(outpath, basename+".avi"))
    ImgUtils.renderVideo(outpath, "{name}".format(name=basename)+"%03d.png", os.path.join(outpath, basename+".avi"))
    return outpath


if __name__ == "__main__":
    a = doIt("https://github.com/nikolaypavlov/MLPNeuralNet.git", r"c:\tests",r"c:\tests\MLPNeuralNet", r"c:\tests")











if __name__ == "__main__":
    print "Done"
