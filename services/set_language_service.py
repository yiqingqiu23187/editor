from services.base_service import BaseService
from common.constant.category import Category
from common.constant.file import LanguageType

class SetLanguageService(BaseService):
    def get_code(self):
        return 'lang'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        if data.split()[1] == 'eng':
            self.file.language = LanguageType.eng
        elif data.split()[1] == 'fra':
            self.file.language = LanguageType.fra
