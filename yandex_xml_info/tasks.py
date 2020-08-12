from starlette.background import BackgroundTask
from starlette.responses import JSONResponse

from main import TEXT


def string_separator():
    """Простой разделитель строк по точке"""
    for part in TEXT:
        yield part


async def get_yandex_xml():
    """Отпаравка запроса к Yandex.XML и запись результата разбора ответа в
    базу."""
    #TODO тут должны быть запросы к yandex xml не ясно до конца как это лучше
    # сделать. есть библиотека pyyaxml, но ее результат нужно разбирать. думаю
    # подойдет PyBX


async def start_tasks_for_yandex_xml(request):
    """Запускает таски для разбора текста"""
    data = string_separator()

    tasks = []

    for part_text in data:
        tasks.append(BackgroundTask(get_yandex_xml, text=part_text))

    content = {
        'tasks': tasks
    }

    message = {'status': 'Запущены запросы к Yandex.XML'}
    return JSONResponse(message, content=content)
