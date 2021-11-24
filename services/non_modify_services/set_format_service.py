from services.base_service import BaseService
from common.constant.category import Category
from common.constant.file import FormatType

class SetFormatService(BaseService):
    def get_code(self):
        return 'content'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        if data.split()[1] == 'txt':
            self.file.language = FormatType.txt
        elif data.split()[1] == 'xml':
            self.file.language = FormatType.xml
