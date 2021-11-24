#
# @program: Editor
# @description: oop lab1
# @author: Huang Zihao
# @email: 18302010034@fudan.edu.cn
#
from handler.executor import Executor

executor = Executor()


def exe(string):
    executor.execute(string)


if __name__ == '__main__':
    # 2-拼写检查部分 TestCase01
    exe('A "Quel est votre point de vue"')
    exe('s')            # Quel est votre point de vue
    exe('a "What is your point of view, and, "')
    exe('s')            # What is your point of view, and, Quel est votre point de vue
    exe('content txt')
    exe('lang eng')
    exe('spell')        # Quel est votre point de vue
    exe('lang fra')
    exe('spell')        # What is your point of view and
    exe('m 2 twoStep')
    exe('$twoStep')
    exe('s')            # What is your point of view, and, What is your point of view, and, Quel est votre point de vueQuel est votre point de vue
    exe('spell')        # What is your point of view and What is your point of view and vueQuel
    exe('lang eng')
    exe('spell')        # Quel est votre point de vueQuel est votre de vue
    exe('u')
    exe('s')            # What is your point of view and Quel est votre de vue
    exe('d 3')
    exe('s')            # t is your point of view, and, Quel est votre de vue
    exe('spell')        # t Quel est votre point de vue
