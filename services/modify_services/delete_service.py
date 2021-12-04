from services.base_service import BaseService
from common.constant.category import Category

class DeleteService(BaseService):
    def get_code(self):
        return 'D'

    def get_category(self):
        return Category.modify

    def process(self, data):  # type: (str) -> None
        data = data.split()
        if len(data) < 2:
            raise Exception('参数格式错误，参考：D 5')
        self.delete_len = int(data[1])
        self.data = self.file.content[len(self.file.content) - self.delete_len:]
        self.file.content = self.file.content[0:len(self.file.content) - self.delete_len]
        print(self.file.content)

    def undo(self):
        self.file.content += self.data

    def redo(self):
        self.process('D ' + str(self.delete_len))
