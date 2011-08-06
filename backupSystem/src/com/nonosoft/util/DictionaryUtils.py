from com.nonosoft.metaclass.pattern.Singleton import Singleton

# -----------------------------------------------------------------------------
# DictionaryUtils. This class give property file service. The prrroperty
# format into the file is:
#     propertyname=propertyValue
#
# the property name must be unic into the file.
# -----------------------------------------------------------------------------
class DictionaryUtils(object):

    __metaclass__ = Singleton

#    getPropertiesFromFile
#
#    @param propertyFile: the path of property file. 
#
    def getPropertiesFromFile(self, propertyFile):
        objFile = open(propertyFile)
        dict([(key.strip(), value.strip()) \
            for (key, value) in [line.split('=') \
                    for line in objFile]])
