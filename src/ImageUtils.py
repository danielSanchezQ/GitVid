__author__ = 'Daniel Sanchez Quiros'

import hashlib
import cv2
import numpy as np
import math
import os.path as op
from itertools import repeat
import png

class ImgUtils:

    hexmin, hexmax = 0, int("ffffffff", 16)
    rgbmin, rgbmax = 0, 255

    def __init__(self, file):
        self.file = file

    @staticmethod
    def hexlify(data):
        return hashlib.md5(data).hexdigest()
    @staticmethod
    def hexlifylines(fname):
        return [ImgUtils.hexlify(x) for x in open(fname).readlines()[:100]]

    @staticmethod
    def split8bits(data):
        return [data[a:b] for a, b in [(0,8), (8,16), (16,24), (24, 32)]] if len(data) == 32 else None

    @staticmethod
    def parsenum(data):
        return int(data, 16)

    @classmethod
    def reduceAlpha(cls, r, g, b, a):
        return map(lambda x: int(math.floor(x*a/float(cls.rgbmax))), [r, g, b])

    @classmethod
    def normalize(cls, data):
        return math.floor(((data/float(cls.hexmax))+cls.hexmin)*cls.rgbmax)+cls.rgbmin

    @staticmethod
    def repeatLst(elem, size):
        ret = []
        data = [x for x in repeat(elem, size)]
        for e in data:
            ret.extend(e)
        return ret

    @staticmethod
    def toNumPyArray(lst):
        return np.asarray(lst, dtype=np.uint8)

    @staticmethod
    def npArrayReplicated(lst):
        return ImgUtils.toNumPyArray(ImgUtils.replicatedDataLst(lst))

    @staticmethod
    def toImage(array):
        return cv2.imdecode(array, 0)

    @staticmethod
    def replicatedDataLst(lst, size=10):
        return map(lambda x: ImgUtils.repeatLst(x, size), lst)

    @staticmethod
    def calcData(filename):
        f = lambda x : int(ImgUtils.normalize(ImgUtils.parsenum(x)))
        return map(lambda x: ImgUtils.reduceAlpha(*x), map(lambda x: map(f,x), map(ImgUtils.split8bits ,ImgUtils.hexlifylines(filename))))

    @staticmethod
    def refill(lst, sizeY, sizeX=10):
        lst.extend([0,0,0]*sizeX for x in xrange(sizeY))
        return lst

    @staticmethod
    def calcBunchFiles(replicatedSize=10, *args):
        replicated = map(lambda x: ImgUtils.replicatedDataLst(ImgUtils.calcData(x), replicatedSize), args)
        return map(lambda x: ImgUtils.refill(x, max(map(lambda y: len(y), replicated))- len(x), replicatedSize), replicated)


    def doIt(self):
        return self.toImage(self.npArrayReplicated(self.calcData(self.file)))

    def doAndSave(self ,outdir=None):
        filename, _ = op.splitext(op.basename(self.file))
        extension = '.jpg'
        if outdir:
            outdir = op.join(outdir, filename+extension)
        else:
            outdir = op.basename(filename+extension)
        cv2.imwrite(outdir, self.doIt())

    @staticmethod
    def data2Png(data, outdir):
        with open(outdir, 'wb') as f:
            #data = ImgUtils.replicatedDataLst(data,100)
            if data:
                w = png.Writer(len(data[0])/3, len(data), greyscale=False)
                w.write(f, data)
        return outdir

    @staticmethod
    def reduceAndSave2Png(outdir, *args):
        ImgUtils.data2Png(reduce(lambda x, y: [a+b for a,b in zip(x, y)] , ImgUtils.calcBunchFiles(1, *args)), outdir)

    def toPNG(self, outdir=None):
        filename, _ = op.splitext(op.basename(self.file))
        extension = '.png'
        if outdir:
            outdir = op.join(outdir, filename+extension)
        else:
            outdir = op.basename(filename+extension)
        with open(outdir, 'wb') as f:
            data = self.replicatedDataLst(self.calcData(),100)
            if data:
                w = png.Writer(len(data[0])/3, len(data), greyscale=False)
                w.write(f, data)
        return outdir if data else None


if __name__ == "__main__":
    from pprint import pprint
    import png
    import PathUtils

    ImgUtils.reduceAndSave2Png(r"C:\tests\test_django.png", *PathUtils.getFilesFromPath(r"C:\tests\django"))





