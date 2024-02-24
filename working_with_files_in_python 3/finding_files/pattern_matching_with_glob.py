from pathlib import Path


def glob_match(fld_path, search):
    p = Path(fld_path)
    for n in p.glob(search):
        print(n)


glob_match('../../Fundamentals/classes_and_objects', '*.p*')
