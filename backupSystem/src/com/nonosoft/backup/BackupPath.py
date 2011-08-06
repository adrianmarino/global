'''
Created on 23/03/2010

@author: adrian
'''

from com.nonosoft.util.DirectoryUtil import DirectoryUtil

class Action(object):
    def __str__(self):
        raise NotImplemented

class ExcludeAction(Action):
    def __str__(self):
        return '--exclude'

class IncludeAction(Action):
    def __str__(self):
        return '--include'

class NullAction(Action):
    def __str__(self):
        return ''
#
#
#
#
# BackuoPath class
#
class BackupPath(object):

# -----------------------------------------------------------------------------
# Constructors
# -----------------------------------------------------------------------------

    def __init__(self, path, action = NullAction()):
        self.__action = action
        self.__path = DirectoryUtil().formatPath(path)

# -----------------------------------------------------------------------------
# Override methods
# -----------------------------------------------------------------------------
    def __str__(self):
        return self.action.__str__() + ' ' + self.path 

# -----------------------------------------------------------------------------
# Public methods
# -----------------------------------------------------------------------------

    def isExcluded(self):
        return self.action.__class__ == ExcludeAction

    def isIncluded(self):
        return self.action.__class__ == IncludeAction

# -----------------------------------------------------------------------------
# Getters and Setters
# -----------------------------------------------------------------------------

    def get_action(self):
        return self.__action


    def get_path(self):
        return self.__path


    def set_action(self, value):
        self.__action = value


    def set_path(self, value):
        self.__path = value


    def del_action(self):
        del self.__action


    def del_path(self):
        del self.__path

    action = property(get_action, set_action, del_action, "action's docstring")
    path = property(get_path, set_path, del_path, "path's docstring")
        

        

