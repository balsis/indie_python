
DEBUG = 10, 'DEBUG'
INFO = 20, 'INFO'
WARNING = 30, 'WARNING'
ERROR = 40, 'ERROR'
CRITICAL = 50, 'CRITICAL'


def log_event(timestamp: int, message: str, /, *, level=INFO, format_log="[%(time)] %(levelname) - %(message)"):
    if level[0] > 10:
        format_log = format_log.replace("%(time)", str(timestamp)).replace("%(levelname)", str(level[1])).replace("%(message)", str(message)).replace("%(levelno)", str(level[0]))
        return format_log
    else:
        return None

res1 = log_event(1764230394, 'Сервер приложения запущен')
res2 = log_event(1764230425, 'Медленный GET-запрос', level=WARNING)
res3 = log_event(1764230410, 'Ошибка подключения к БД', level=ERROR,
                 format_log="%(levelno), %(time): %(message)")

assert res1 == "[1764230394] INFO - Сервер приложения запущен"
assert res2 == "[1764230425] WARNING - Медленный GET-запрос"
assert res3 == "40, 1764230410: Ошибка подключения к БД"