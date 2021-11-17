from services.undo_service import UndoService
from services.list_service import ListService
from common.utils.exception import exception_wrapper
from common.constant.category import Category
from handler.router import Router


class Executor(object):
    def __init__(self):
        self.router = Router()

    @exception_wrapper()
    def execute(self, string):
        # type: (str) -> None
        params = string.split()
        target_service = self.router.find_route(params[0])()
        target_service.process(string)

        if target_service.get_category() == Category.modify:
            UndoService.add(target_service)
            ListService.add(string)