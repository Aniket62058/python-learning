import zipfile


def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)


def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)


extract_file('./data/files.zip', 'data/f2.txt', './data/extracted/file')
extract_all('./data/files.zip', './data/extracted')
