

class BackupSystem(object):

    def backup(self, backupPaths, options):
        raise NotImplemented
    
    def restore(self, destinyBackupPath, time, options):
        raise NotImplemented       