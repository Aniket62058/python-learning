import fnmatch
import os


# This is more generic way of searching file name

def match(fld_path, search):
    for fn in os.listdir(fld_path):
        if fnmatch.fnmatch(fn, search):
            print(fn)


match('../../Fundamentals', '*_*')
