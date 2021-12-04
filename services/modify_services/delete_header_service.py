from services.base_service import BaseService
from common.constant.category import Category

class DeleteHeaderService(BaseService):
    def get_code(self):
        return 'd'

    def get_category(self):
        return Category.modify

    def process(self, data):  # type: (str) -> None
        data = data.split()
        if len(data) < 2:
            raise Exception('参数格式错误，参考：d 5')
        self.delete_len = int(data[1])
        self.data = self.file.content[0: self.delete_len]
        self.file.content = self.file.content[self.delete_len:]
        print(self.file.content)

    def undo(self):
        self.file.content = self.data + self.file.content

    def redo(self):
        self.process('d ' + str(self.delete_len))
