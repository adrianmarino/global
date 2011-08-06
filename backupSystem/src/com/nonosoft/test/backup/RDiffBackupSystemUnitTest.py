'''
Created on 16/03/2010

@author: adrian
'''
from com.nonosoft.backup.BackupPath import BackupPath
from com.nonosoft.backup.rdiff.RDiffBackupSystem import RDiffBackupSystem, \
    ErrorToBackupPathsException
from com.nonosoft.test.AbstractUnitTest import AbstractUnitTest
from com.nonosoft.util.OSUtils import OSUtils
from test.test_import import os





class RDiffBackupSystemUnitTest(AbstractUnitTest):

# -----------------------------------------------------------------------------
# Private methods
# -----------------------------------------------------------------------------

    # Lamda methods...
    def __transformToCompletePath(self, path): return self._getCompletePath(path) 

    def __transformToBackupPath(self, path): return BackupPath(path + '/')

    def __removePath(self, path): OSUtils().removeDirectory(path)

    def __transformToSourcePath(self, path): return '/source' + path

    def __transformToRepositoryPath(self, path): return '/repository' + path

    def __createDirectory(self, path): OSUtils().createDirectory(path)

    def __createFile(self, path): 
        if not os.path.isfile(path): 
            try:
                open(path, 'a')
            except IOError:
                pass

    def __getPaths(self): 
        return ['/etc', '/src']

    def __getSourcePaths(self):
        return map(self.__transformToSourcePath, self.__getPaths())

    def __getRepositoryPaths(self):
        return map(self.__transformToRepositoryPath, self.__getPaths())

    def __getCompleteSourcePaths(self):
        return map(self.__transformToCompletePath, self.__getSourcePaths())

    def __getCompleteRepositoryPaths(self):
        return map(self.__transformToCompletePath, self.__getRepositoryPaths())

    def __getSourceBackupPaths(self):
        return map(self.__transformToBackupPath, self.__getCompleteSourcePaths())

    def __removeCompleteRepositoryPaths(self):
        map(self.__removePath, self.__getCompleteRepositoryPaths())

    def __generateEnvironmet(self):
        OSUtils().removeDirectory(self._getCompletePath('/repository'))
        OSUtils().removeDirectory(self._getCompletePath('/source'))

        OSUtils().createDirectory(self._getCompletePath('/source/etc/cron.deny'))
        self.__createFile(self._getCompletePath('/source/etc/cron.deny/aaaaa'))
        self.__createFile(self._getCompletePath('/source/etc/cron.deny/bbbbb'))
        OSUtils().createDirectory(self._getCompletePath('/source/etc/cron.daily'))
        self.__createFile(self._getCompletePath('/source/etc/cron.hourly/ccccc'))
        OSUtils().createDirectory(self._getCompletePath('/source/etc/cron.hourly'))
        OSUtils().createDirectory(self._getCompletePath('/source/etc/cron.weekly'))
        self.__createFile(self._getCompletePath('/source/etc/xxxxx'))
        self.__createFile(self._getCompletePath('/source/etc/yyyyy'))
        self.__createFile(self._getCompletePath('/source/etc/zzzzz'))

        self.__createFile(self._getCompletePath('/source/etc/vim/vimrc'))
        self.__createFile(self._getCompletePath('/source/etc/vim/vimrc.tiny'))     
        self.__createFile(self._getCompletePath('/source/etc/vim/crontab'))
        self.__createFile(self._getCompletePath('/source/etc/sssss'))
        self.__createFile(self._getCompletePath('/source/etc/qqqqq'))

        OSUtils().createDirectory(self._getCompletePath('/source/src/linux'))
        self.__createFile(self._getCompletePath('/source/src/uuuuu'))
        self.__createFile(self._getCompletePath('/source/src/ooooo'))
        self.__createFile(self._getCompletePath('/source/src/linux/.config'))
        self.__createFile(self._getCompletePath('/source/src/linux/Makefile'))
        self.__createFile(self._getCompletePath('/source/src/linux/configure'))

# -----------------------------------------------------------------------------
# Override methods
# -----------------------------------------------------------------------------

    def setUp(self):
        self.__generateEnvironmet()
        self._component = RDiffBackupSystem(self._getCompletePath('/repository'))

# -----------------------------------------------------------------------------
# Public methods
# -----------------------------------------------------------------------------

    def testDefaultBackup(self):
        for backupPath in self.__getSourceBackupPaths():
            try:
                self._component.backup(backupPath)
            except ErrorToBackupPathsException as e:
                self.fail(e.message)

            # Check if exist path into repository...
            self.assertTrue(
                    os.path.exists(self._getCompletePath('/repository') + 
                                   backupPath.path))

    def testExcludeOnlyBackup(self):
        pass

    def testIncludeOnlyBackup(self):
        pass

    def testExcludeAndIncludeBackup(self):
        pass

    def testRestore(self):
        pass
        # Generate backup...
#        for backupPath in self.__getSourceBackupPaths():
#            try:
#                self._component.backup(backupPath)
#            except ErrorToBackupPathsException as e:
#                self.fail(e.message)

        # Remove all source paths...
#       OSUtils().removeDirectory(self._getCompletePath('/source'))

        # restore all source paths
#        for path in self.__getCompleteSourcePaths():
#            try:
#                self._component.restore(path, 'now')
#            except ErrorToRestorePathException as e:
#                self.fail(e.message)