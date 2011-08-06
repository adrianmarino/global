from com.nonosoft.util.ListUtils import ListUtils

class ErrorToBackupPathsException(Exception):
    def __init__(self, backupPaths, e):
        self.message = 'Error to backup ' + ListUtils().concat(backupPaths) + ' paths. ' + e.message

