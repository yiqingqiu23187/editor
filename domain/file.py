from common.utils.singleton import singleton
from common.constant.file import LanguageType, FormatType


@singleton
class File(object):
    def __init__(self):
        self.content = ''
        self.language = LanguageType.eng
        self.format = FormatType.txt