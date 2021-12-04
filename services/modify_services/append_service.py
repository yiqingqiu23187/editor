from services.base_service import BaseService
from common.constant.category import Category


class AppendService(BaseService):

    def get_code(self):
        return 'A'

    def get_category(self):
        return Category.modify

    def process(self, data):
        # A "last word"
        data = data.split('\"')
        if len(data) < 2:
            raise Exception('参数格式错误,参考：A \"last word\"')
        self.data = data[1]
        self.file.content += self.data
        print(self.file.content)

    def undo(self):
        self.file.content = self.file.content.removesuffix(self.data)

    def redo(self):
        self.process(''.join(['A ', '\"', self.data, '\"']))
