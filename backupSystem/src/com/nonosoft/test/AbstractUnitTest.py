'''
Created on 15/03/2010

@author: adrian
'''
from unittest import TestCase

class AbstractUnitTest(TestCase):


# -----------------------------------------------------------------------------
# Attributes methods
# -----------------------------------------------------------------------------

    _baseTestPath = "/home/adrian/development/backupTest"

    _component = None
    
# -----------------------------------------------------------------------------
# Protected methods
# -----------------------------------------------------------------------------
    def _getCompletePath(self, relativePath):
        return self._baseTestPath + relativePath
            
