from services.base_service import BaseService
from services.non_modify_services.undo_service import UndoService
from common.constant.category import Category
from handler.router import Router


class MacroService(BaseService):
    def get_code(self):
        return 'm'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        data = data.split()
        if len(data) != 3 or int(data[1]) > len(UndoService.undo_list):
            raise Exception('格式错误，参考：m 5 m10')
        router = Router()
        code, num, name = data
        name = '$' + name
        if name in router.CODE_SERVICE_MAP:
            raise Exception('已定义过该宏命令')

        class MacroGenService(BaseService):
            code_operator_map = {}
            def __init__(self):
                super(MacroGenService, self).__init__()

            def get_code(self):
                return name

            def get_category(self):
                return Category.modify

            def process(self, data):  # type: (str) -> None
                self.data = data
                for operator in MacroGenService.code_operator_map[data]:
                    operator.redo()

            def undo(self):
                for operator in MacroGenService.code_operator_map[self.data][::-1]:
                    operator.undo()

            def redo(self):
                for operator in MacroGenService.code_operator_map[self.data]:
                    operator.redo()

        MacroGenService.code_operator_map[name] = UndoService.undo_list[len(UndoService.undo_list) - int(num):]
        router.CODE_SERVICE_MAP[name] = MacroGenService
