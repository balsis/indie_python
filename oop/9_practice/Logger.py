class Logger:
    DEBUG = 5
    INFO = 4
    WARN = 3
    ERROR = 2
    FATAL = 1
    _level = DEBUG

    def __init__(self):
        Logger._level = Logger.DEBUG

    @classmethod
    def is_level(cls, level):
        return cls._level >= level

    @classmethod
    def debug(cls, message):
        if cls.is_level(Logger.DEBUG):
            print(f"DEBUG: {message}")

    @classmethod
    def info(cls, message):
        if cls.is_level(Logger.INFO):
            print(f"INFO: {message}")

    @classmethod
    def warn(cls, message):
        if cls.is_level(Logger.WARN):
            print(f"WARN: {message}")

    @classmethod
    def error(cls, message):
        if cls.is_level(Logger.ERROR):
            print(f"ERROR: {message}")

    @classmethod
    def fatal(cls, message):
        if cls.is_level(Logger.FATAL):
            print(f"FATAL: {message}")


def log_all():
    Logger.debug("This is a Debug message.")
    Logger.info("This is a Info message.")
    Logger.warn("This is a Warn message.")
    Logger.error("This is an Error message.")
    Logger.fatal("This is a Fatal message.")


Logger._level = Logger.DEBUG
log_all()