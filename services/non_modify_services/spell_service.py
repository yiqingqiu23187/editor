import re
from services.base_service import BaseService
from common.constant.category import Category
from common.constant.file import FormatType, LanguageType
from common.utils.MyIO import MyIO


class SpellService(BaseService):
    def get_code(self):
        return 'spell'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        if self.file.format == FormatType.txt:
            words = re.compile('[a-zA-Z]+').findall(self.file.content)
        elif self.file.format == FormatType.xml:
            sentences = re.compile('>.*?<').findall(self.file.content)
            words = [word for sentence in sentences for word in re.compile('[a-zA-Z]+').findall(sentence)]
        else:
            raise Exception('文本格式错误')

        if self.file.language == LanguageType.eng:
            dictionary = MyIO.read_line('common/dictionary/eng.txt')
        elif self.file.language == LanguageType.fra:
            dictionary = MyIO.read_line('common/dictionary/fra.txt')
        else:
            raise Exception('文本语言错误')


        unmatch = []
        for word in words:
            if word not in dictionary:
                unmatch.append(word)

        print(unmatch)

