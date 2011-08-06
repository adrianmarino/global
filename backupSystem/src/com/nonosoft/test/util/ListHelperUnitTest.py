'''
Created on 15/03/2010

@author: adrian
'''
from com.nonosoft.test.AbstractUnitTest import AbstractUnitTest
from com.nonosoft.util.ListUtils import ListUtils


class ListHelperUnitTest(AbstractUnitTest):
    
# -----------------------------------------------------------------------------
# Constructors
# -----------------------------------------------------------------------------

    def setUp(self):
        self.__listFromFile = self._baseTestPath + "/listHelper.getListFromFile" 

# -----------------------------------------------------------------------------
# Test methods
# -----------------------------------------------------------------------------

    def testGetListFromFile(self):
        list = ListUtils().getListFromFile(self.__listFromFile)

        self.assertTrue( list != None,"Warn: No exist Test File...")

        self.assertTrue(list.__len__() > 0,"Warn: Empty Test File...")

        for item in list:
            self.assertTrue(item.__len__() > 0,"Warn: Empty File Line...")

    def testContains(self):
        list = ["Hello", "Greek"]
        
        self.assertTrue(ListUtils().contains(list, "Hello"))

        self.assertFalse(ListUtils().contains(list, "Gleek"))

