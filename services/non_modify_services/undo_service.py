from services.base_service import BaseService
from common.constant.category import Category
from services.non_modify_services.redo_service import RedoService

class UndoService(BaseService):
    undo_list = []
    if False:
        undo_list = [BaseService()]

    def get_code(self):
        return 'u'

    def get_category(self):
        return Category.non_modify

    def process(self, data):  # type: (str) -> None
        if not UndoService.undo_list:
            # print(self.file.content)
            return
        service = UndoService.undo_list.pop()
        service.undo()
        RedoService.add(service)


    @classmethod
    def add(self, service):
        UndoService.undo_list.append(service)
