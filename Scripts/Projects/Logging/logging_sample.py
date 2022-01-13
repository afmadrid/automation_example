from Logger import Logger, DebugLogger, InfoLogger, WarningLogger, ErrorLogger, CriticalLogger

logger = Logger()
logger.print_log('Root text!!!')
logger = DebugLogger()
logger.print_log('Debugging text!!!')
logger = InfoLogger()
logger.print_log('Information text!!!')
logger = WarningLogger()
logger.print_log('Warning text!!!')
logger = ErrorLogger()
logger.print_log('Error text!!!')
logger = CriticalLogger()
logger.print_log('Critical text!!!')
