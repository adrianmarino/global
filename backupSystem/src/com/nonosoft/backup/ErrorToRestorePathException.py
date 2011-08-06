
class ErrorToRestorePathException(Exception):
    def __init__(self, path, e):
        self.message = 'Error to restore ' + path + ' path. ' + e.message
