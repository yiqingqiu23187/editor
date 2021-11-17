class MyIO(object):

    @classmethod
    def read_line(self, file_path):
        with open(file_path) as f:
            return [line.strip('\n') for line in f.readlines() if line.strip('\n')]