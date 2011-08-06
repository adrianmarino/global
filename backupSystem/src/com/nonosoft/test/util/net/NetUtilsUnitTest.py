'''
Created on 15/03/2010

@author: adrian
'''
from com.nonosoft.test.AbstractUnitTest import AbstractUnitTest
from com.nonosoft.util.net.NetUtils import NetUtils

class NetUtilsUnitTest(AbstractUnitTest):

# -----------------------------------------------------------------------------
# Test methods
# -----------------------------------------------------------------------------

    def testGetLocalHostname(self):
        hostname = NetUtils().getLocalHostname();

        self.assertFalse(len(hostname) == 0, 'hostname not exit!!')
        print('\nHostname is...' + hostname)
        
        
        
        
