__author__ = 'Daniel Sanchez Quiros'

import os
from cStringIO import StringIO
import subprocess

def redirect_output(f):
    def ret(*args):
        old_stout = os.sys.stdout
        myStdout = StringIO()
        os.sys.stdout = myStdout
        error = f(*args)
        stringret = myStdout.getvalue()
        myStdout.close()
        os.sys.stdout = old_stout
        return stringret, error
    return ret

def getVersion():
    return subprocess.check_output("git --version").strip("\n")

def cloneRepo(dir, path = None, username = None, passwd = None):
    if path:
        os.chdir(path)
    return subprocess.check_output("git clone {dir}".format(dir=dir))


def getCommits(path= None):
    if path:
        os.chdir(path)
    ret = [x for x in subprocess.check_output("git log --pretty=%H").split("\n")]
    #ret.reverse()
    return ret[:-1]

def checkout(checkout_code, path = None):
    if path:
        os.chdir(path)
    subprocess.check_output("git checkout master")
    subprocess.check_output("git checkout {}".format(checkout_code))

#def getcheckout(revision):
#    subprocess.check_output("git checkout ")

def countRevisions(path=None):
    if path:
        os.chdir(path)
    return int(subprocess.check_output("git rev-list HEAD --count").strip("\n"))

if __name__ == "__main__":
    from pprint import pprint
    #p = "https://github.com/fourthbit/spheres.git"
    #os.chdir("c:/tests")
    #cloneRepo(p)
    #os.chdir("c:/tests/spheres")
    print countRevisions(r"C:\tests\MLPNeuralNet")
    pprint(getCommits(r"C:\tests\MLPNeuralNet"))