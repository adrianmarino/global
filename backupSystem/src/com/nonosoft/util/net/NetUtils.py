# -----------------------------------------------------------------------------
# ListUtils
#
# -----------------------------------------------------------------------------
from com.nonosoft.metaclass.pattern.Singleton import Singleton
from com.nonosoft.util.OSUtils import OSUtils

class NetUtils(object):

    __metaclass__ = Singleton

# Get local hostname
#
# @return: hostname
#
    def getLocalHostname(self):
        hostname = ''
        for line in OSUtils().execute('hostname').stdout:
            hostname = hostname + bytes.decode(line).strip();
        return hostname