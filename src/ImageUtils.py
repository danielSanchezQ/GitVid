__author__ = 'Daniel Sanchez Quiros'

import hashlib
import cv2
import numpy as np
import math


class ImgUtils:

    hexmin, hexmax = 0, int("ffffffff", 16)
    rgbmin, rgbmax = 0, 255

    def __init__(self, file):
        self.file = file

    def hexlify(self, data):
        return hashlib.md5(data).hexdigest()

    def hexlifylines(self):
        return [self.hexlify(x) for x in open(self.file).readlines()]

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

    def doIt(self):
        f = lambda x : int(self.normalize(self.parsenum(x)))
        return map(lambda x: self.reduceAlpha(*x), map(lambda x: map(f,x), map(self.split8bits ,self.hexlifylines())))





