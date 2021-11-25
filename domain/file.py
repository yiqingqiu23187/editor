from common.utils.singleton import singleton_wrapper
from common.constant.file import LanguageType, FormatType


@singleton_wrapper
class File(object):
    def __init__(self):
        self.content = ''
        self.language = LanguageType.eng
        self.format = FormatType.txt