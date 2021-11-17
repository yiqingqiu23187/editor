from services.base_service import BaseService
from common.constant.category import Category
import services.undo_service

class RedoService(BaseService):
    redo_list = []
    if False:
        redo_list = [BaseService()]

    def get_code(self):
        return 'r'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        service = RedoService.redo_list.pop()
        service.redo()
        services.undo_service.UndoService.add(service)

    @classmethod
    def add(self, service):
        RedoService.redo_list.append(service)
