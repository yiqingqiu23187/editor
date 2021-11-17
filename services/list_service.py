from services.base_service import BaseService
from common.constant.category import Category


class ListService(BaseService):
    operate_list = []
    if False:
        operate_list = ['D 5']

    def get_code(self):
        return 'l'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        data = data.split()
        if len(data) < 2:
            raise Exception('参数格式错误，参考：l 5')
        for i, operator in enumerate(ListService.operate_list[::-1]):
            if i + 1 == int(data[1]):
                break
            print((i + 1, operator))

    @classmethod
    def add(cls, operator):
        cls.operate_list.append(operator)
