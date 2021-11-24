from services.base_service import BaseService
from common.constant.category import Category

class ShowService(BaseService):

    def get_code(self):
        return 's'

    def get_category(self):
        return Category.non_modify

    def process(self, data):
        print(self.file.content)

