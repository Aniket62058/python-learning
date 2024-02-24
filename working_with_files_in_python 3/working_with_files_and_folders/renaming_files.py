import os
from pathlib import Path


def rename_file_1(src, dst):
    os.rename(src, dst)


def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)


# rename_file_2('__init__.py','init.txt')
rename_file_1('init.txt', '__init__.py')
