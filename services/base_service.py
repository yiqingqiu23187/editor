from domain.file import File

class BaseService(object):
    file = File()

    def __init__(self):
        pass

    def get_code(self):
        pass

    def get_category(self):
        pass

    def process(self, data):
        # type: (str) -> None
        pass

    def undo(self):
        pass

    def redo(self):
        pass