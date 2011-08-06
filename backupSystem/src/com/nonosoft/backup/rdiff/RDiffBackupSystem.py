from com.nonosoft.backup.BackupPath import BackupPath
from com.nonosoft.backup.BackupSystem import BackupSystem
from com.nonosoft.backup.ErrorToBackupPathsException import ErrorToBackupPathsException
from com.nonosoft.backup.ErrorToRestorePathException import ErrorToRestorePathException
from com.nonosoft.util.Log import Log
from com.nonosoft.util.OSUtils import OSUtils
#
#
#
# ------------------------------------------------------------------------------
# RDiffBackupSystem Class.
# ------------------------------------------------------------------------------
#  This is a helper class and give backup service.
# ------------------------------------------------------------------------------
class RDiffBackupSystem(BackupSystem):
#
#
#
# -----------------------------------------------------------------------------
# Attributes:
# -----------------------------------------------------------------------------

    __DEFAULT_BACKUP_OPTIONS = '--force --print-statistics --terminal-verbosity 1'

    __DEFAULT_RESTORE_OPTIONS = '--force'
#
#
#
# ------------------------------------------------------------------------------
# Constructors:
# ------------------------------------------------------------------------------

    def __init__(self, repositoryPath, priority=19):
        self.__repositoryPath = repositoryPath
        self.__priority = priority
        self.__log = Log(self.__class__)
#
#
#
# ------------------------------------------------------------------------------
# Private methods:
# ------------------------------------------------------------------------------

    def __transformToBackupPathList(self, value):
        if value.__class__ == BackupPath:
            return [value]
        return value



    def __isRemoteRepository(self):
        return self.__repositoryPath.count('::') != 0



    def __createBackupPathsInLocalRepository(self, backupPaths):
        for backupPath in self.__transformToBackupPathList(backupPaths):
            if not self.__isRemoteRepository():
                OSUtils().createDirectory(self.__repositoryPath + backupPath.path)



    def __getRestoreCommand(self, restorePath, options):        
        if options.strip().__len__() == 0:
            options = self.__DEFAULT_RESTORE_OPTIONS

        return 'nice -' + str(self.__priority) + ' rdiff-backup ' + options + ' ' + self.__repositoryPath + restorePath + ' ' + 
                restorePath



    def __getBackupCommand(self, sourceBackupPaths, options):        
        isFirst = True
        sourcePaths = ''

        # Get all source backup paths...
        for sourceBackupPath in self.__transformToBackupPathList(sourceBackupPaths):
            if isFirst:
                # Get destinyPäth. This is the first of paths...
                destinyPath = self.__repositoryPath + sourceBackupPath.path
                isFirst = False

            # Add source path...
            sourcePaths = sourcePaths + ' ' + sourceBackupPath.__str__()

        sourcePaths = sourcePaths.strip()

        # Add default options...
        if options.__len__() == 0:
            options = self.__DEFAULT_BACKUP_OPTIONS

        # Return rdiff-baclup command...
        self.__log.info('Backup "' + sourcePaths.strip() + '" To "' + destinyPath + '" Repository.')
        return 'nice -' + str(self.__priority) + ' rdiff-backup ' + options + ' ' + sourcePaths + ' ' + destinyPath



    def __executeCommand(self, command):
            # Execure command...
            result = OSUtils().execute(command)

            # log command output...
            for line in result.stdout:
                self.__log.info(bytes.decode(line))
#
#
#
# ------------------------------------------------------------------------------
# Public methods:
# ------------------------------------------------------------------------------
#
#
# Backup Method
# --------------------------------------------------------------------------
#    @param backupPaths: Backup paths.
#    @param options: Usefull for add custom options for rdiffbackup command.
# --------------------------------------------------------------------------
    def backup(self, backupPaths, options=__DEFAULT_BACKUP_OPTIONS):
        self.__log.reset()
        
        self.__createBackupPathsInLocalRepository(backupPaths)

        ## Build backup command...
        command = self.__getBackupCommand(backupPaths, options)

        # Run backup command...
        try:
            self.__log.debug('command: ' + command)
            self.__executeCommand(command)
        except Exception as e:
            raise ErrorToBackupPathsException(self.__transformToBackupPathList(backupPaths), e)

        return self.__log.output
#
#
#
# Restore Method
# -----------------------------------------------------------------------
#    @param destinyBackupPath: The path of file/directory to restore.
#    @param time: The time.
#    @param options: Option used to restore backup. back time and others
#                    aditional options.
# -----------------------------------------------------------------------
    def restore(self, restorePath, time, options=__DEFAULT_RESTORE_OPTIONS):
        self.__log.reset()

        OSUtils().createDirectory(restorePath)
 
        # Build restore command...
        command = self.__getRestoreCommand(restorePath, '-r ' + time + ' ' + options)

        # Run restore command...
        try:
            self.__log.debug('command: ' + command)
            self.__executeCommand(command)
        except Exception as e:
            raise ErrorToRestorePathException(restorePath, e)
        else:
            self.__log.info('...restored ' + restorePath + ' path.')
        return self.__log.output


