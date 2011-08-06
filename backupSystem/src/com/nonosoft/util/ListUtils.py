# -----------------------------------------------------------------------------
# ListUtils
#
# -----------------------------------------------------------------------------
from com.nonosoft.metaclass.pattern.Singleton import Singleton

class ListUtils(object):

    __metaclass__ = Singleton
    
# getListFromFile
#  Get a list if lines from text file.
#
# @param file: the file
#
    def getListFromFile(self, file):
        results = []
        try:
            for line in open(file):
                results.append(line.strip())
        except IOError as e:
            results = None
            print('Error to read ' + file + ' file.' + e.__str__())

        return results
#
# The list contains this value?
# @param list: the list.
# @param value: the value.
#
    def contains(self,list,value):
        try:
            list.index(value)
            return True
        except:
            return False

    def concat(self,list):
        result = ''
        for item in list:
            result += str(item)
        return result
        
        