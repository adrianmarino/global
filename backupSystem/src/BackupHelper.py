'''
Created on 13/03/2010

@author: adrian
'''
from com.nonosoft.backup.rdiff.RDiffBackupSystem import RDiffBackupSystem
from com.nonosoft.metaclass.pattern.Singleton import Singleton
from com.nonosoft.util.Log import Log
from com.nonosoft.util.net.Mailer import Mailer
from com.nonosoft.util.net.NetUtils import NetUtils
from test.test_import import os
import configuration
import sys

#
#
#
# ------------------------------------------------------------------------------
# BackupHelper
# ------------------------------------------------------------------------------
class BackupHelper(object):

# -----------------------------------------------------------------------------
# Attributes methods
# -----------------------------------------------------------------------------

    __metaclass__ = Singleton

# -----------------------------------------------------------------------------
# Constructors
# -----------------------------------------------------------------------------

    def __init__(self):
        self.__log = Log(self.__class__)


# -----------------------------------------------------------------------------
# Private methods
# -----------------------------------------------------------------------------

    def __sendReport(self, report):
        mailer = Mailer(configuration.MAIL_SERVER,
                        configuration.MAIL_LOGIN_USER,
                        configuration.MAIL_LOGIN_PASSWORD,
                        configuration.MAIL_ADDRESS,
                        configuration.MAIL_ADDRESS,
                        '')

        subject = 'Backup Report from ' + NetUtils().getLocalHostname() + " hostname." 
        try:
            mailer.send(subject, report)
            self.__log.info('...Report mail was sended...')
        except Exception as e:
            print('Error to send report mail.')
            print(e.args)

    def __generateLocaleReport(self, results):
        # Delete old report...
        if os.path.exists(configuration.REPORT_PATH):
            os.remove(configuration.REPORT_PATH)

        file = open(configuration.REPORT_PATH, 'a')
        file.write(results)
        file.close()
        self.__log.info('...Local report was generated...')



# -----------------------------------------------------------------------------
# Public methods
# -----------------------------------------------------------------------------
    
    def generateLocaleReport(self, results):
        if configuration.ENABLE_LOCAL_REPORT:
            self.__generateLocaleReport(results)

    def generateReport(self, report):
        self.generateLocaleReport(report)

        if configuration.ENABLE_MAIL_REPORT:
            self.__sendReport(report)

    def existHelpArg(self, args):
        return len(args) == 2 and args[1] == '--help'

    def existBackupArgs(self, args):
        return len(args) >= 2 and sys.argv[1] == 'backup'

    def existRestoreArgs(self, args):
        return len(args) >= 3 and sys.argv[1] == 'restore'

    def getOptionArgs(self, args, startPos):
        optionsArgs = ''
        if len(args) >= startPos:
            for option in args[startPos:]:
                optionsArgs = optionsArgs + ' ' + option
        return optionsArgs.strip()

    def __backupPath(self, backupPath, options): 
        return self.getBackupSystem().backup(backupPath, options)

    def backup(self, options):
        output = ''
        for backupPath in configuration.BACKUP_PATHS:
            output = output + self.__backupPath(backupPath, options)
        return output

    def restore(self, path, time, options):
        return self.getBackupSystem().restore(path, time, options)

    def getBackupSystem(self):
        return RDiffBackupSystem(configuration.REPOSITORY_PATH, configuration.PROCESS_PRIORITY)

