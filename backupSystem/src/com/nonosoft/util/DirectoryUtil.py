'''
Created on 23/03/2010

@author: adrian
'''
from com.nonosoft.metaclass.pattern.Singleton import Singleton

class DirectoryUtil(object):

    __metaclass__ = Singleton

    def formatPath(self, path):
        if path.endswith('/'):
            path = path[0:path.rindex('/')]
        return path

    def formatPathList(self, list):
        results = []
        for path in list:
            path = self.__formatPath(path)
            results.append(path)
        return results
            