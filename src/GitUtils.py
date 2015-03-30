__author__ = 'Netwave'

import os
from cStringIO import StringIO
import subprocess

def redirectoutput(f):
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

def revert():
    subprocess.check_output("git revert")

#def getcheckout(revision):
#    subprocess.check_output("git checkout ")

def countRevisions(path=None):
    if path:
        os.chdir(path)
    return int(subprocess.check_output("git rev-list HEAD --count").strip("\n"))

if __name__ == "__main__":
    p = "https://github.com/fourthbit/spheres.git"
    os.chdir("c:/tests")
    cloneRepo(p)
    os.chdir("c:/tests/spheres")
    print countRevisions()








