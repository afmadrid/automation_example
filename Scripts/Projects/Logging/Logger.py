import logging


class Logger:
    _PRINT_FORMAT = '%(asctime)s:%(levelname)s:%(message)s'
    _FILE_MODE = 'a'
    _LOG_FOLDER_PATH = 'logging_files/'

    def __init__(self):
        self._name = 'root'
        self._create_valid_logger()

    def _create_valid_logger(self):
        self._logger = logging.getLogger(self._name)
        self._set_logger_level()
        self._setup_logger()

    def _set_logger_level(self):
        if self._name == 'debug':
            level = logging.DEBUG
        elif self._name == 'info' or self._name == 'root':
            level = logging.INFO
        elif self._name == 'warning':
            level = logging.WARNING
        elif self._name == 'error':
            level = logging.ERROR
        elif self._name == 'critical':
            level = logging.CRITICAL
        else:
            level = logging.NOTSET
        self._logger.setLevel(level)
        
    def _setup_logger(self):
        formatter = logging.Formatter(self._PRINT_FORMAT)
        file_handler = logging.FileHandler(self._LOG_FOLDER_PATH + self._name + '.log', mode=self._FILE_MODE)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)

    def print_log(self, text):
        self._logger.info(text)


class DebugLogger(Logger):
    def __init__(self):
        self._name = 'debug'
        self._create_valid_logger()

    def print_log(self, text):
        self._logger.debug(text)


class InfoLogger(Logger):
    def __init__(self):
        self._name = 'info'
        self._create_valid_logger()

    def print_log(self, text):
        self._logger.info(text)


class WarningLogger(Logger):
    def __init__(self):
        self._name = 'warning'
        self._create_valid_logger()

    def print_log(self, text):
        self._logger.warning(text)


class ErrorLogger(Logger):
    def __init__(self):
        self._name = 'error'
        self._create_valid_logger()

    def print_log(self, text):
        self._logger.error(text)


class CriticalLogger(Logger):
    def __init__(self):
        self._name = 'critical'
        self._create_valid_logger()

    def print_log(self, text):
        self._logger.critical(text)
