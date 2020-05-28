from pathlib import Path


class CsvReader(object):
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.file = None
        if Path(filename).is_file():
            self.header = header
            self.file = open(filename, "r")
            data = self.file.read().split('\n')
            self.lines = [
                line.split(sep)
                for i, line in enumerate(data)
                if skip_top <= i < len(data) - skip_bottom - 1
            ]
            if not all(len(line) == len(self.lines[0]) for line in self.lines):
                self.file = None

    def __enter__(self):
        if self.file is None:
            return None
        return self

    def __exit__(self, type, value, traceback):
        if self.file is not None:
            self.file.close()

    def getdata(self):
        return self.lines[1:] if self.header else self.lines

    def getheader(self):
        return self.lines[0] if self.header else None


def main():
    with CsvReader('bad.csv', header=True) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)


if __name__ == "__main__":
    main()
