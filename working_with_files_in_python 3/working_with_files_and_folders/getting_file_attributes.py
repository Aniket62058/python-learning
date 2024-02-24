import os
from datetime import datetime


def get_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d %b %y')


def get_file_attrs(fld):
    with os.scandir(fld) as d:
        for f in d:
            if f.is_file():
                inf = f.stat()
                print(f"Modified {get_date(inf.st_mtime)} {f.name}")


get_file_attrs('../../Fundamentals')
