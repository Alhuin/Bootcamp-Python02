from pathlib import Path


class CsvReader(object):
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        self.file = None
        self.header = None
        if isinstance(filename, str) and Path(filename).is_file():
            self.file = open(filename, "r")
            data = self.file.read().split('\n')
            if header:
                self.header = data.pop(0).split(sep)
            self.lines = [
                line.split(sep)
                for i, line in enumerate(data)
                if line != "" and skip_top <= i < len(data) - skip_bottom - 1
            ]
            if header and self.lines != [] \
                    and len(self.header) != len(self.lines[0]):
                self.file = None
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
        return self.lines

    def getheader(self):
        return self.header


def main():
    with CsvReader("bad.csv", header=True, skip_bottom=6, skip_top=46) as file:
        if file is None:
            print("File is corrupted")
        else:
            data = file.getdata()
            print(data)
            header = file.getheader()
            print(header)


if __name__ == "__main__":
    main()
