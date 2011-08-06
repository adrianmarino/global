from com.nonosoft.metaclass.pattern.Singleton import Singleton
import os
import subprocess

# -----------------------------------------------------------------------------
# OSUtils
#
# -----------------------------------------------------------------------------
class OSUtils(object):

    __metaclass__ = Singleton

# Remove Directory. This method remove directory of recursive form. 
# Equivalent to rm -rf path.
#
# @param path: parh to remove.
# 
    def removeDirectory(self,path):
        if os.path.exists(path):
            for fullSubPath in os.listdir(path):
                fullSubPath = path + "/" + fullSubPath
                if os.path.isdir(fullSubPath):
                    self.removeDirectory(fullSubPath)
                else:
                    os.remove(fullSubPath)
            os.rmdir(path)

# Create directory if not exist.
#
# @param path: the path of directory.
#
    def createDirectory(self, path) :        
        if not os.path.exists(path):
            os.makedirs(path)

#
# Execute. Run system command. this include
# your parameters un the same commant string.
# By esample: 'ls -la'
#
# @param command: the command to run
# @return: The command output string from strout.
#
    def execute(self, command):
        if len(command) > 0:
            return subprocess.Popen(command.split(),
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)


    createDirectory = classmethod(createDirectory)
    execute = classmethod(execute)
