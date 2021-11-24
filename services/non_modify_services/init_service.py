from services.base_service import BaseService
from common.constant.category import Category


class InitService(BaseService):
    def get_code(self):
        return '-t'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        data = data.split('\"')
        if len(data) < 2:
            raise Exception('参数格式错误,参考：A \"last word\"')
        self.file.content = data[1]
