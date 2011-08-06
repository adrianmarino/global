from com.nonosoft.util.LogLevel import LogLevel, ErrorLogLevel, DebugLogLevel, \
    InfoLogLevel, WarnLogLevel
import configuration
import datetime

#
#
#
# -----------------------------------------------------------------------------
# Log Class
#
# -----------------------------------------------------------------------------
class Log(object):
#
#
#
# -----------------------------------------------------------------------------
# Constructors
# -----------------------------------------------------------------------------
    def __init__(self, componentClass):
        self.reset()
        self.__componentClass = componentClass

        if not configuration.LOG_LEVEL == None and isinstance(configuration.LOG_LEVEL, LogLevel):
            self.__level = configuration.LOG_LEVEL
        else:
            self.__level = ErrorLogLevel()
            print('Error: Invalid LogLevel. Set ErrorLogLevel by default')
#
#
#
# -----------------------------------------------------------------------------
# Private methods
# -----------------------------------------------------------------------------
    def __getFormatedOutPutMessage(self, message):
        return datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S') + ' - ' + self.__componentClass.__name__ + ' - ' + message.strip()
    
    def __show(self, message):
        result = self.__getFormatedOutPutMessage(message)
        print(result)
        self.output = self.output + result + '\n'
#
#
#
# -----------------------------------------------------------------------------
# Public methods
# -----------------------------------------------------------------------------

    def error(self, message):
        if isinstance(self.__level, DebugLogLevel) or \
            isinstance(self.__level, InfoLogLevel) or \
            isinstance(self.__level, WarnLogLevel)  or \
            isinstance(self.__level, ErrorLogLevel):
            self.__show('ERROR - ' + message)

    def warn(self, message):
        if isinstance(self.__level, DebugLogLevel) or \
            isinstance(self.__level, InfoLogLevel) or \
            isinstance(self.__level, WarnLogLevel):
            self.__show('WARN - ' + message)

    def info(self, message):
        if isinstance(self.__level, DebugLogLevel) or \
            isinstance(self.__level, InfoLogLevel):
            self.__show('INFO - ' + message)

    def debug(self, message):
        if isinstance(self.__level, DebugLogLevel):
            self.__show('DEBUG - ' + message)

    def reset(self):
        self.output = ''
#
#
#
# -----------------------------------------------------------------------------
# Getters and Setters
# -----------------------------------------------------------------------------

    def get_output(self):
        return  self.__output

    def set_output(self, value):
        self.__output = value

    def del_output(self):
        del self.__output

    output = property(get_output, set_output, del_output, "output's docstring")


