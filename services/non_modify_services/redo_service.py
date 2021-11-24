from services.base_service import BaseService
from common.constant.category import Category
import services.non_modify_services.undo_service

class RedoService(BaseService):
    redo_list = []
    if False:
        redo_list = [BaseService()]

    def get_code(self):
        return 'r'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        if not self.redo_list:
            # print(self.file.content)
            return
        service = RedoService.redo_list.pop()
        service.redo()
        services.non_modify_services.undo_service.UndoService.add(service)

    @classmethod
    def add(self, service):
        RedoService.redo_list.append(service)
